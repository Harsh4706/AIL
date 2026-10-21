
# Smart Parking Allocation

# Input parking slots
n = int(input("Enter number of parking slots: "))
slots = {}

for i in range(n):
    print("\nEnter details for slot", i + 1)
    slot_id = input("Slot ID: ")
    slot_type = input("Slot type (Car/Bike/EV/Accessible): ")
    distance = int(input("Distance from entrance: "))
    available = input("Available? (Yes/No): ").lower()

    slots[slot_id] = {
        "type": slot_type,
        "distance": distance,
        "available": available == "yes"
    }

# Input vehicles
v = int(input("\nEnter number of vehicles: "))
vehicles = []

for i in range(v):
    print("\nEnter details for vehicle", i + 1)
    vehicle_id = input("Vehicle ID: ")
    vehicle_type = input("Vehicle type (Car/Bike/EV/Accessible): ")

    vehicles.append({
        "id": vehicle_id,
        "type": vehicle_type
    })

# Find the nearest suitable slot
def find_slot(vehicle):
    best_slot = None
    shortest_distance = float("inf")

    for slot_id, details in slots.items():
        if not details["available"]:
            continue

        if details["type"].lower() != vehicle["type"].lower():
            continue

        if details["distance"] < shortest_distance:
            shortest_distance = details["distance"]
            best_slot = slot_id

    return best_slot

# Allocate parking slots
print("\n--- Parking Allocation ---")

for vehicle in vehicles:
    slot = find_slot(vehicle)

    if slot is not None:
        print(vehicle["id"], "->", slot)
        slots[slot]["available"] = False
    else:
        print(vehicle["id"], "-> No suitable slot available")

# Display remaining available slots
print("\n--- Remaining Available Slots ---")

for slot_id, details in slots.items():
    if details["available"]:
        print(slot_id, "-", details["type"])
