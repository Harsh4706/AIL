import random
import time


class TrafficController:

    def __init__(self):
        self.min_green = 10
        self.max_green = 60

    def calculate_green_time(self, traffic_density, waiting_time):

        # Traffic density: 0 to 100
        # Waiting time: seconds

        if traffic_density < 20:
            density_level = "Low"

        elif traffic_density < 60:
            density_level = "Medium"

        else:
            density_level = "High"

        # Fuzzy-style decision rules

        if density_level == "Low" and waiting_time < 20:
            green_time = 15

        elif density_level == "Low" and waiting_time >= 20:
            green_time = 25

        elif density_level == "Medium" and waiting_time < 30:
            green_time = 35

        elif density_level == "Medium" and waiting_time >= 30:
            green_time = 45

        elif density_level == "High" and waiting_time < 30:
            green_time = 50

        else:
            green_time = 60

        # Extra adjustment for waiting vehicles

        if waiting_time > 60:
            green_time += 10

        green_time = min(green_time, self.max_green)

        return density_level, green_time


def get_traffic_data():

    # Simulated uncertain traffic data

    density = random.randint(0, 100)
    waiting_time = random.randint(0, 90)

    return density, waiting_time


def main():

    controller = TrafficController()

    signals = [
        "North-South",
        "East-West"
    ]

    print("INTELLIGENT TRAFFIC CONTROL SYSTEM")
    print("------------------------------------")

    for cycle in range(10):

        print(f"\nCycle {cycle + 1}")

        for signal in signals:

            density, waiting_time = get_traffic_data()

            level, green_time = controller.calculate_green_time(
                density,
                waiting_time
            )

            print(f"\nSignal: {signal}")
            print(f"Traffic Density: {density}%")
            print(f"Waiting Time: {waiting_time} seconds")
            print(f"Traffic Level: {level}")
            print(f"Green Light Time: {green_time} seconds")

            print("Signal is GREEN")

            # For demonstration, don't actually wait full duration.
            time.sleep(1)

            print("Signal is RED")


if __name__ == "__main__":
    main()