from fastapi import FastAPI, BackgroundTasks, Query
from celery.result import AsyncResult
from tasker import poll_github_api
from pydantic import BaseModel
from tasker import celery_app
app = FastAPI()

tasks = {}


class TaskRequest(BaseModel):
    user_id: int #Instead of this we need to have the wallet address
    url_input: str


@app.get("/status/{user_id}/task")
async def get_task_status(user_id: int):
    task = tasks.get(user_id)
    if task:
        task_status = AsyncResult(task.id, app=poll_github_api)
        if task_status.state == 'SUCCESS':
            del tasks[user_id]
            return {"message": f"Task completed for user {user_id}"}
        else:
            return {"message": f"Task status for user {user_id}: {task_status.state}"}
    else:
        return {"message": f"No active task for user {user_id}"}


@app.post("/start")
async def start_polling(task_request: TaskRequest):
    user_id = task_request.user_id
    # Maybe we will need a unique hash to indentify the correct task
    url_input = task_request.url_input
    if user_id not in tasks:
        tasks[user_id] = poll_github_api.delay(url_input)
        print(tasks)
        return {"message": f"Started polling for user {user_id}"}
    else:
        return {"message": f"Polling already in progress for user {user_id}"}


@app.post("/stop/{user_id}")
async def stop_polling(user_id: int):
    if user_id in tasks:
        celery_app.control.revoke(
            tasks[user_id].id, terminate=True, signal='SIGKILL')
        del tasks[user_id]
        return {"message": f"Stopped polling for user {user_id}"}
    else:
        return {"message": f"No active polling for user {user_id}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
