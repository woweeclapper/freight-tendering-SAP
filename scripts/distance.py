import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

CACHE_FILE = "distance_cache.json"

class DistanceService:
    def __init__(self):
        self.api_key = os.getenv("ORS_API_KEY")
        if not self.api_key:
            raise ValueError("ORS_API_KEY not found in .env file")

        self.cache = self._load_cache()

    def _load_cache(self):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        with open(CACHE_FILE, "w") as f:
            json.dump(self.cache, f, indent=2)

    def geocode(self, city):
        url = "https://api.openrouteservice.org/geocode/search"
        params = {"api_key": self.api_key, "text": city}
        r = requests.get(url, params=params)
        data = r.json()
        lon, lat = data["features"][0]["geometry"]["coordinates"]
        return lon, lat

    def get_distance_km(self, origin, destination):
        key = f"{origin} -> {destination}"

        # Check cache first
        if key in self.cache:
            return self.cache[key]

        # Geocode both cities
        o_lon, o_lat = self.geocode(origin)
        d_lon, d_lat = self.geocode(destination)

        # Request driving distance
        url = "https://api.openrouteservice.org/v2/directions/driving-car"
        body = {"coordinates": [[o_lon, o_lat], [d_lon, d_lat]]}
        headers = {"Authorization": self.api_key}

        r = requests.post(url, json=body, headers=headers)
        data = r.json()

        meters = data["routes"][0]["summary"]["distance"]
        km = meters / 1000

        # Save to cache
        self.cache[key] = km
        self._save_cache()

        return km
