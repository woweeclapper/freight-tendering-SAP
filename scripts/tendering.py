from models import FreightUnit, Carrier, CarrierResponse, FreightOrder


def run_tendering(freight_unit, carriers, distances):

    """
    Run the tendering process for a given FreightUnit.

    Parameters:
    freight_unit (FreightUnit): The FreightUnit to tender
    carriers (list of Carrier): The list of Carriers to tender to
    distances (dict): A dictionary of distances between two points

    Returns:
    FreightOrder: The winning FreightOrder
    """
    responses = []
    # Loop through each carrier


#testing 
    if carriers is None or len(carriers) == 0:
        print("No carriers available for tendering.")
        return None
    
    for carrier in carriers:
        # Check if the freight unit's weight is less than or equal to the carrier's capacity
        if freight_unit.weight <= carrier.capacity:


            # Get the state from the freight unit's destination
            state = freight_unit.destination.split(",")[1].strip()

            # Check if the state is in the carrier's coverage and if the freight unit's mode is in the carrier's modes
            if state in carrier.coverage and freight_unit.mode in carrier.modes:

                
                # Get the distance from the distances dictionary
                distance = distances.get((freight_unit.origin, freight_unit.destination), 0)




                # Get the key from the carrier's rates dictionary
                key = f"({freight_unit.origin}, {freight_unit.destination})"

                # Get the rate from the carrier's rates dictionary
                rate = carrier.rates.get(key, 1.0)

      
                # Calculate the cost
                cost = distance * rate

                #TODO: Make the output cost into float with 2 decimal places
                print(f"{carrier.name} eligible: cost = ${cost:.2f}")

                # Append the response to the list of responses
                responses.append(CarrierResponse(carrier, True, cost, 2))

    # If there are no responses, print a message and return None
    if not responses:
        print("No carrier accepted for Freight Unit: " + freight_unit.id)
        return None
        
    # Find the winner by getting the minimum cost from the list of responses
    winner = min(responses, key=lambda r: r.cost)
    # Create a new FreightOrder with the winner
    order = FreightOrder(freight_unit, winner.carrier, winner.cost)
    order.confirm()
    return order


