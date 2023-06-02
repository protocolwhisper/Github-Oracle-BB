import requests
def get_pull_request_author(url):
    response = requests.get(url)
    response_json = response.json()
    
    if "user" in response_json and "login" in response_json["user"]:
        return response_json["user"]["login"]
    else:
        raise ValueError("Could not find author in the response")
