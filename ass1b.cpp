#include <bits/stdc++.h>
using namespace std;

int heuristic(vector<int> &state, int n)
{
    int d = 0;

    for (int i = 0; i < n * n; i++)
    {
        int x = state[i];

        if (x != 0)
        {
            int goal = x - 1;
            d += abs(i / n - goal / n) + abs(i % n - goal % n);
        }
    }

    return d;
}

vector<vector<int>> astar(vector<int> start, int n)
{
    vector<int> goal;

    for (int i = 1; i < n * n; i++)
        goal.push_back(i);
    goal.push_back(0);

    using Node = tuple<int, int, vector<int>, vector<vector<int>>>;

    priority_queue<Node, vector<Node>, greater<Node>> pq;

    pq.push({heuristic(start, n), 0, start, {}});
    set<vector<int>> visited;

    while (!pq.empty())
    {
        int f = get<0>(pq.top());
        int g = get<1>(pq.top());
        vector<int> state = get<2>(pq.top());
        vector<vector<int>> path = get<3>(pq.top());
        pq.pop();

        if (state == goal)
        {
            path.push_back(state);
            return path;
        }

        if (visited.count(state))
            continue;

        visited.insert(state);

        int z = find(state.begin(), state.end(), 0) - state.begin();
        int r = z / n, c = z % n;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        for (int k = 0; k < 4; k++)
        {
            int nr = r + dr[k];
            int nc = c + dc[k];

            if (nr >= 0 && nr < n && nc >= 0 && nc < n)
            {
                int nz = nr * n + nc;

                vector<int> s = state;
                swap(s[z], s[nz]);

                if (!visited.count(s))
                {
                    vector<vector<int>> newPath = path;
                    newPath.push_back(state);

                    pq.push({g + 1 + heuristic(s, n),
                             g + 1,
                             s,
                             newPath});
                }
            }
        }
    }

    return {};
}

int main()
{
    int n;
    cout << "Enter N: ";
    cin >> n;

    vector<int> start;

    cout << "Enter puzzle row by row (0 for blank):\n";

    for (int i = 0; i < n * n; i++)
    {
        int x;
        cin >> x;
        start.push_back(x);
    }

    vector<vector<int>> solution = astar(start, n);

    if (!solution.empty())
    {
        cout << "Solution found in " << solution.size() - 1 << " moves\n";

        for (auto state : solution)
        {
            for (int i = 0; i < n * n; i++)
            {
                cout << state[i] << " ";

                if ((i + 1) % n == 0)
                    cout << "\n";
            }
            cout << "\n";
        }
    }
    else
    {
        cout << "No solution found\n";
    }

    return 0;
}