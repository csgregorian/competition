#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;

	unsigned long long value;
	vector<unsigned long long> hills;

	for (int i = 0; i < n; ++i) {
		cin >> value;
		hills.push_back(value);
	}

	int minleft = 0;
	int left = 0;

	int count = 1;
	// cout << left << " " << 1 << endl;

	for (int right = 2; right < hills.size(); ++right)
	{
		left = right - 2;
		count++;
		// cout << left << " " << right << endl;
		while (left >= minleft && hills[right] >= hills[right-1]) {
			if (hills[minleft] < hills[left]) {
				minleft = left;
				break;
			}
			left--;
			count++;
			// cout << left << " " << right << endl;
		}
	}

	cout << count << endl;


	return 0;
}