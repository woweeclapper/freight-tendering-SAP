import json
from models import FreightUnit, Carrier
from tendering import run_tendering
from distance import DistanceService


distance_service = DistanceService()

# Load shipment, carrier, and distance data from JSON files
shipments = json.load(open("data/shipments.json"))
carriers_data = json.load(open("data/carriers.json"))
#distances_data = json.load(open("data/distances.json"))

carriers = [Carrier(c["name"], c["coverage"], c["capacity_kg"], c["modes"], c["rates"]) for c in carriers_data]


#TODO: Get realisitic distances using an API
#TODO: Create a function to generate reports after tendering (Shipment X = Y Carrier)
#TODO: Create a bidding  for shipment that does not have a prenegotiated carrier, then evaluate the bids


# Example using a mock function (replace with actual API calls if needed)


# Run tendering for each shipment
for s in shipments:

    origin = s["origin"]
    destination = s["destination"]

    # Get real distance using DistanceService
    distance_km = distance_service.get_distance_km(origin, destination)

    #build freight unit
    fu = FreightUnit(s["id"], origin, destination, s["weight_kg"], 20, s["deadline"], s["mode"])
    
    run_tendering(fu, carriers, {(origin, destination): distance_km})




# Save updated distances to distances.json
print("Saved distance_cache.json with real distances.")
