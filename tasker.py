from celery import Celery
from opa import get_pr_from_issue
import subprocess

redis_hostname = "redis"
celery_app = Celery("worker", broker=f"redis://localhost:6379/0",
                    backend=f"redis://localhost:6379/0")


@celery_app.task
def poll_github_api(url):
    import time
    # Replace :owner, :repo, and :issue_number with appropriate values

    while True:
        print("querying again")
        data = get_pr_from_issue(url)
        print(data)
        if data[1] is not None:
            # Process the data or store it as needed
            subprocess.run(["npx", "locklift", "run", "--network", "local", "--script", "scripts/writebounty.ts"], cwd="/oracletx/locklift/sample-project-typescript", shell=True)
            # execute
            print("Your watcher works")
            break
        print("Querying again")
        time.sleep(60)  # Wait for 5 minutes (300 seconds)
