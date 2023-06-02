import requests
import argparse
from utils import transform_url
from pull import get_pull_request_author
from bs4 import BeautifulSoup


def get_pr_from_issue(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the div that contains the information you want
    info_div = soup.find("div", class_="gh-header-meta")
    # print(info_div)
    # Extract the text from the div
    info_text = info_div.get_text(strip=True)
    if "may be fixed by" in info_text.lower():
        return "Error: Issue isn't solved yet.", None
    number = info_text.split("#")[-1].strip()
    # Check if a number was found before the #
    if not number.isdigit():
        return "Error: PR is not merged yet or not found.", None

    pull_request = transform_url(url) + number
    author = get_pull_request_author(pull_request)
    return pull_request, author


# # Setup argument parser
# parser = argparse.ArgumentParser(description="Get pull request and author from issue URL")
# parser.add_argument("url", type=str, help="Issue URL")
# args = parser.parse_args()

# # Call the function with the URL argument
# url = "https://github.com/protocolito/TestGithub/issues/5"
# issue_number = get_pr_from_issue(url)  # Tuple
# print(issue_number)
# print(type(issue_number))
