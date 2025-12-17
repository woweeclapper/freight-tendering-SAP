from datetime import datetime

class FreightUnit:
    def __init__(self, id, origin, destination, weight, volume, deadline, mode):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.volume = volume
        self.deadline = deadline
        self.mode = mode

class Carrier:
    def __init__(self, name, coverage, capacity, modes, rates):
        self.name = name
        self.coverage = coverage      # list of regions/states
        self.capacity = capacity      # max weight
        self.modes = modes            # e.g. ["Truck", "Rail"]
        self.rates = rates            # dict: {lane: rate_per_km}

class TenderingProfile:
    def __init__(self, strategy="sequential", timeout=60):
        self.strategy = strategy      # "broadcast", "sequential", "rate_based"
        self.timeout = timeout        # seconds to wait for response

class CarrierResponse:
    def __init__(self, carrier, accepted, cost, transit_time):
        self.carrier = carrier
        self.accepted = accepted
        self.cost = cost
        self.transit_time = transit_time
        self.timestamp = datetime.now()

class FreightOrder:
    def __init__(self, freight_unit, carrier, cost):
        self.freight_unit = freight_unit
        self.carrier = carrier
        self.cost = cost
        self.confirmed = False

    def confirm(self):
        self.confirmed = True
        print(f"Freight Order confirmed: {self.freight_unit.id} → {self.carrier.name}")

