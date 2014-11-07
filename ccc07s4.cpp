#include <iostream>
#include <vector>
#include <array>
#include <string>

using namespace std;

int main() {
	int n;
	cin >> n;

	int paths[9999] = {1};
	paths[1] = 1;

	vector<int> connections[n+1];

	int x, y;

	while (true) {
		cin >> x;
		cin >> y;
		if (x + y == 0) {
			break;
		}
		connections[x].push_back(y);
	}

	for (int i = 1; i != n+1; i++) {
		for (int slide : connections[i]) {
			paths[slide] += paths[i];	

		}

	}

	cout << paths[n] << endl;
	



}

