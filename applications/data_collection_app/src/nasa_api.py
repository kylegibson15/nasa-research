import requests
import os
from dotenv import load_dotenv

load_dotenv()

mission_id = "GPM"
nasa_base_url = "https://api.nasa.gov"
nasa_techport_url = f"{nasa_base_url}/techport/projects"
api_key = os.getenv("NASA_API_KEY")

mission_url = f"{nasa_techport_url}/{mission_id}?api_key={api_key}"
response = requests.get(mission_url)

if response.status_code == 200:
    data = response.json()

    print(f"Mission Name: {data['name']}")
    print(f"Mission Description: {data['description']}")
else:
    print(f"Error: API request failed with status code {response.status_code}")

