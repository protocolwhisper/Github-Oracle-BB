from fastapi import FastAPI, BackgroundTasks, Query, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from celery.result import AsyncResult
from tasker import poll_github_api
from pydantic import BaseModel
from tasker import celery_app
from typing import Optional

app = FastAPI()

tasks = {}

API_KEY_NAME = "access_token"
api_key_start = APIKeyHeader(name=API_KEY_NAME)
api_key_other = APIKeyHeader(name=API_KEY_NAME)

# Change these to your actual API keys
API_KEY_START = "3e9bd24a88d140c29926d8c96453a39b"
API_KEY_OTHER = "gottarefactor123456"


class TaskRequest(BaseModel):
    user_id: str
    url_input: str
    task_index: int


def validate_start_api_key(api_key_start_header: str = Depends(api_key_start)):
    if api_key_start_header != API_KEY_START:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key_start_header


def validate_other_api_key(api_key_other_header: str = Depends(api_key_other)):
    if api_key_other_header != API_KEY_OTHER:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key_other_header


@app.get("/status", dependencies=[Depends(validate_start_api_key)])
async def get_task_status(user_id: str = Query(...), url_input: str = Query(...)):
    # Rest of the code remains the same
    user_tasks = tasks.get(user_id)
    if user_tasks:
        task = user_tasks.get(url_input)
        if task:
            task_status = AsyncResult(task.id, app=poll_github_api)
            if task_status.state == 'SUCCESS':
                del user_tasks[url_input]
                return {"message": f"Task completed for user {user_id} for URL {url_input}"}
            else:
                return {"message": f"Task status for user {user_id} for URL {url_input}: {task_status.state}"}
    return {"message": f"No active task for user {user_id} for URL {url_input}"}


@app.post("/start", dependencies=[Depends(validate_start_api_key)])
async def start_polling(task_request: TaskRequest):
    user_id = task_request.user_id
    url_input = task_request.url_input
    user_tasks = tasks.get(user_id, {})
    if url_input not in user_tasks:
        user_tasks[url_input] = poll_github_api.delay(url_input)
        tasks[user_id] = user_tasks
        return {"message": f"Started polling for user {user_id} for URL {url_input}"}
    else:
        return {"message": f"Polling already in progress for user {user_id} for URL {url_input}"}


@app.post("/stop/{user_id}/{url_input}", dependencies=[Depends(validate_other_api_key)])
async def stop_polling(user_id: str, url_input: str):
    user_tasks = tasks.get(user_id)
    if user_tasks:
        task = user_tasks.get(url_input)
        if task:
            celery_app.control.revoke(
                task.id, terminate=True, signal='SIGKILL')
            del user_tasks[url_input]
            return {"message": f"Stopped polling for user {user_id} for URL {url_input}"}
    return {"message": f"No active polling for user {user_id} for URL {url_input}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
