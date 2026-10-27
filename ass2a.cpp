#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <climits>
using namespace std;

map<int, string> type;
map<int, int> dist;
map<int, bool> available;

vector<int> vehicleId;
vector<string> vehicleType;

int findSlot(int i) {
    int bestSlot = -1;
    int shortestDistance = INT_MAX;

    for (auto &p : type) {
        int id = p.first;

        if (!available[id])
            continue;

        if (p.second != vehicleType[i])
            continue;

        if (dist[id] < shortestDistance) {
            shortestDistance = dist[id];
            bestSlot = id;
        }
    }

    return bestSlot;
}

int main() {
    int n;
    cout << "Enter number of parking slots: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        int id, d;
        string t;
        bool status;

        cout << "Enter slot ID, type, distance, availability (1/0): ";
        cin >> id >> t >> d >> status;

        type[id] = t;
        dist[id] = d;
        available[id] = status;
    }

    int v;
    cout << "Enter number of vehicles: ";
    cin >> v;

    for (int i = 0; i < v; i++) {
        int id;
        string t;

        cout << "Enter vehicle ID and type: ";
        cin >> id >> t;

        vehicleId.push_back(id);
        vehicleType.push_back(t);
    }

    cout << "\n--- Parking Allocation ---\n";

    for (int i = 0; i < v; i++) {
        int slot = findSlot(i);

        if (slot != -1) {
            cout << vehicleId[i] << " -> Slot " << slot << '\n';
            available[slot] = false;
        } else {
            cout << vehicleId[i]
                 << " -> No suitable slot available\n";
        }
    }

    cout << "\n--- Remaining Available Slots ---\n";

    for (auto &p : type) {
        int id = p.first;

        if (available[id])
            cout << "Slot " << id << " - " << p.second << '\n';
    }

    return 0;
}