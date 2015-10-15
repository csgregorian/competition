#include <bits/stdc++.h>

using namespace std;

int main() {
	int t, ymax, xmax;

	cin >> t;

	array<array<char, 20>, 20> grid;

	struct node {
		int x;
		int y;
		int depth;
	};


	for (int i = 0; i < t; i++) {
		cin >> ymax >> xmax;
		for (int y = 0; y < ymax; y++) {
			for (int x = 0; x < xmax; x++) {
				cin >> grid[x][y];
				// cout << grid[x][y];
			}
		}

		// cout << "input done" << endl;

		queue<node> q;

		node n;
		n.x = 0;
		n.y = 0;
		n.depth = 1;

		q.push(n);

		while (!q.empty()) {
			n = q.front();
			q.pop();

			char c = grid[n.x][n.y];
			grid[n.x][n.y] = '*';
			int x = n.x;
			int y = n.y;

			// cout << x << " " << y << endl;

			if (x == xmax-1 && y == ymax-1) {
				if (c == '*') {
					break;
				}

				cout << n.depth << endl;
				goto label;
			}

			if (c == '*') {
				continue;
			}

			if (c == '-' || c == '+') {
				if (x > 0) {
					node left = n;
					left.x--;
					left.depth++;
					q.push(left);
				}

				if (x < xmax-1) {
					node right = n;
					right.x++;
					right.depth++;
					q.push(right);
				}
			}

			if (c == '|' || c == '+') {
				if (y > 0) {
					node up = n;
					up.y--;
					up.depth++;
					q.push(up);
				}

				if (y < ymax-1) {
					node down = n;
					down.y++;
					down.depth++;
					q.push(down);
				}
			}
		}

		cout << -1 << endl;

		label:;

		
	}
}