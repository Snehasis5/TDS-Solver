import re
import requests

def extract_url_and_params(question):
    # Extract URL
    url_match = re.search(r"https://[^\s]+", question)
    url = url_match.group(0) if url_match else None

    # Extract parameters
    param_match = re.search(r"email set to (\S+)", question)
    email = param_match.group(1) if param_match else None

    return url, {"email": email} if email else {}

def send_request_and_get_json(question):
    url, params = extract_url_and_params(question)
    if not url:
        return {"error": "URL not found in question"}

    response = requests.get(url, params=params)
    return response.json()

# Given question
question = """Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.

Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 24f1000142@ds.study.iitm.ac.in

What is the JSON output of the command? (Paste only the JSON body, not the headers)"""

# Get and print the JSON response
json_response = send_request_and_get_json(question)
print(json_response)
