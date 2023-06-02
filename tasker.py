from celery import Celery
from opa import get_pr_from_issue
host_ip = "172.17.0.1"
celery_app = Celery("worker", broker=f"redis://{host_ip}:6379/0",
                    backend=f"redis://{host_ip}:6379/0")


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
            print("Your watcher works")
            break
        print("Querying again")
        time.sleep(60)  # Wait for 5 minutes (300 seconds)
