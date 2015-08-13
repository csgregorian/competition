#include <bits/stdc++.h>

using namespace std;

int main() {
	int J, A;
	cin >> J >> A;

	vector<char> sizes, a_size;
	vector<int> a_num;

	for (int i = 0; i < J; ++i) {
		char size;
		cin >> size;
		sizes.push_back(size);
	}

	for (int i = 0; i < A; ++i) {
		char size;
		int num;
		cin >> size >> num;
		num--;

		a_size.push_back(size);
		a_num.push_back(num);
	}

	int requests = 0;

	for (int i = 0; i < A; i++) {
		char size = a_size[i];
		int num = a_num[i];

		char j = sizes[num];

		if (size == 'S') {
			if (j != 'X') {
				requests++;
				sizes[num] = 'X';
			}
		} else
		if (size == 'M') {
			if (j == 'M' || j == 'L') {
				requests++;
				sizes[num] = 'X';
			}
		} else
		if (size == 'L') {
			if (j == 'L') {
				requests++;
				sizes[num] = 'X';
			}
		}
	}

	cout << requests << endl;


}



















