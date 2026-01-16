import json
from models import FreightUnit, Carrier
from tendering import run_tendering
import requests 

# Load shipment, carrier, and distance data
shipments = json.load(open("data/shipments.json"))
carriers_data = json.load(open("data/carriers.json"))
distances_data = json.load(open("data/distances.json"))

carriers = [Carrier(c["name"], c["coverage"], c["capacity_kg"], ["Truck"], c["rates"]) for c in carriers_data]


#TODO: Get realisitic distances using an API
#TODO: Create a function to generate reports after tendering (Shipment X = Y Carrier)
#TODO: Create a bidding  for shipment that does not have a prenegotiated carrier, then evaluate the bids


# Example using a mock function (replace with actual API calls if needed)
distances =  {(d["origin"], d["destination"]): d["distance_km"] for d in distances_data}


# Run tendering for each shipment
for s in shipments:
    fu = FreightUnit(s["id"], s["origin"], s["destination"], s["weight_kg"], 20, s["deadline"], s["mode"])

    run_tendering(fu, carriers, distances)

