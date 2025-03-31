import requests

def get_newest_melbourne_user():
    url = "https://api.github.com/search/users"
    params = {
        "q": "location:Melbourne followers:>50",
        "sort": "joined",
        "order": "desc",
        "per_page": 1
    }
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("items"):
            newest_user = data["items"][0]
            username = newest_user["login"]
            user_url = newest_user["url"]
            user_response = requests.get(user_url, headers=headers)
            
            if user_response.status_code == 200:
                user_data = user_response.json()
                return user_data["created_at"]
    
    return None