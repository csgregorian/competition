/*
ID: csgregorian
PROG: beads
LANG: C++
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	ofstream fout("beads.out");
	ifstream fin("beads.in");

	int n; string s;
	fin >> n >> s;

	int max = 0;

	for (int i = 0; i < n; i++) {
		int count = 0;

		char begin = s[0];
		int it = 0;

		while (it < n) {
			count++;
			it++;
			if (begin == 'w') {
				begin = s[it];
			} else {
				if (s[it] != begin && s[it] != 'w') {
					break;
				}
			}
		}

		char end = s[n-1];
		int it2 = n-1;

		while (it2 > it) {
			count++;
			it2--;
			if (end == 'w') {
				end = s[it2];
			} else {
				if (s[it2] != end && s[it2] != 'w') {
					break;
				}
			}
		}

		if (max < count) {
			max = count;
		}

		char first = s[0];
		s.erase(s.begin());
		s += first;
	}

	fout << max << endl;

	return 0;
}