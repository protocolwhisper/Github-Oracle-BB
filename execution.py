from bs4 import BeautifulSoup
import requests
import schedule
import time
from pull import get_pull_request_author
from utils import transform_url
def job():
    url = "https://github.com/FuelLabs/fuels-ts/issues/648"
    pull_request, author = get_pr_from_issue(url)
    if author is not None:
        # Stop the scheduled job
        schedule.clear('job')

def get_pr_from_issue(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the div that contains the information you want
    info_div = soup.find("div", class_="gh-header-meta")

    # Extract the text from the div
    info_text = info_div.get_text(strip=True)
    number = info_text.split("#")[-1].strip()

    # Check if a number was found before the #
    if not number.isdigit():
        return "Error: PR is not merged yet or not found.", None

    pull_request = transform_url(url) + number
    author = get_pull_request_author(pull_request)

    return pull_request, author

# Schedule the job to run every 5 minutes
schedule.every(5).minutes.do(job).tag('job')

while True:
    # Run pending scheduled jobs
    schedule.run_pending()
    # Sleep for 1 second
    time.sleep(1)
