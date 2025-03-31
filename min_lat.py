import requests

def get_min_latitude(city, country):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "city": city,
        "country": country,
        "format": "json"
    }
    headers = {
        "User-Agent": "UrbanRide/1.0 (24f1000142@ds.study.iitm.ac.in)"  # Replace with a valid email or identifier
    }
    
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            bounding_box = data[0]["boundingbox"]
            min_latitude = float(bounding_box[0])  # South latitude
            return min_latitude
        else:
            return "City not found"
    else:
        return f"Error: {response.status_code}"
    
min_lat = get_min_latitude("Chennai", "India")
print(f"Retrieved min latitude: {min_lat}")