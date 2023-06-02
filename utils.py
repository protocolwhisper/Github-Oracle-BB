import urllib.parse

def transform_url(url):
    parsed_url = urllib.parse.urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")
    
    # Validate that the URL has the expected format
    if len(path_parts) != 4 or path_parts[2] != "issues":
        raise ValueError("Invalid URL format")
    
    owner, repo = path_parts[:2]
    new_path = f"/repos/{owner}/{repo}/pulls/"
    
    new_url = urllib.parse.urlunparse(parsed_url._replace(scheme="https", netloc="api.github.com", path=new_path, query="", fragment=""))
    
    return new_url


