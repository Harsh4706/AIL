
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;

    cout << "Enter number of roads: ";
    cin >> n;

    string roads[n];
    int traffic[n], waitingTime[n], greenTime[n];
    int priority[n];

    for (int i = 0; i < n; i++) {
        cout << "\nEnter road name: ";
        cin >> roads[i];

        cout << "Enter traffic density (0-100): ";
        cin >> traffic[i];

        cout << "Enter waiting time (seconds): ";
        cin >> waitingTime[i];

        if (traffic[i] < 0 || traffic[i] > 100 ||
            waitingTime[i] < 0) {
            cout << "Invalid input!\n";
            return 1;
        }

        // Determine green signal time
        if (traffic[i] < 20 && waitingTime[i] < 20)
            greenTime[i] = 15;
        else if (traffic[i] < 20)
            greenTime[i] = 25;
        else if (traffic[i] < 60 && waitingTime[i] < 30)
            greenTime[i] = 35;
        else if (traffic[i] < 60)
            greenTime[i] = 45;
        else if (waitingTime[i] < 30)
            greenTime[i] = 50;
        else
            greenTime[i] = 60;

        // Extra adjustment for long waiting times
        if (waitingTime[i] > 60)
            greenTime[i] += 10;

        // Keep green time within limits
        if (greenTime[i] > 60)
            greenTime[i] = 60;
        if (greenTime[i] < 10)
            greenTime[i] = 10;

        // Calculate priority
        priority[i] = traffic[i] + waitingTime[i];
    }

    cout << "\n===== TRAFFIC SIGNAL RESULTS =====\n";

    int highestPriority = 0;

    for (int i = 0; i < n; i++) {
        cout << "\nRoad: " << roads[i];
        cout << "\nTraffic Density: " << traffic[i] << "%";
        cout << "\nWaiting Time: " << waitingTime[i] << " seconds";
        cout << "\nGreen Signal Time: " << greenTime[i] << " seconds\n";

        if (priority[i] > priority[highestPriority])
            highestPriority = i;
    }

    cout << "\nRoad receiving priority: "
         << roads[highestPriority] << '\n';

    return 0;
}
