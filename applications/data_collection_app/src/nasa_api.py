import requests
import os
from dotenv import load_dotenv

# example response in techtransfer_api_response.json

load_dotenv()
api_key = os.getenv("NASA_API_KEY")
mission_id = "GPM"
nasa_base_url = "https://techport.nasa.gov"

nasa_techport_url = f"{nasa_base_url}/api/projects"
nasa_techtransfer_url = f"https://api.nasa.gov/techtransfer/patent/?engine&api_key={api_key}"


mission_url = f"{nasa_techport_url}/{mission_id}?api_key={api_key}"
# response = requests.get(mission_url)

response = requests.get(nasa_techtransfer_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    # print(f"Mission Name: {data['name']}")
    # print(f"Mission Description: {data['description']}")
else:
    print(f"Error: API request failed with status code {response.status_code}")
    print(f"Error: {response.json()}")

