/*
ID: csgregorian
PROG: friday
LANG: C++
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	ofstream fout("friday.out");
	ifstream fin("friday.in");

	int n;
	fin >> n;

	int start_year = 1900;
	int current_day = 2; // Monday

	int months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

	int frequency[7] = {0};

	int days;

	for (int year = 1900; year < start_year + n; year++) {
		for (int month = 0; month < 12; month++) {
			days = months[month];

			if (month == 1) { // february
				if (year % 4 == 0 && (!(year % 100 == 0) || year % 400 == 0)) {
					days++;
				}
			}

			for (int day = 0; day < days; day++) {
				if (day == 12)
					frequency[current_day]++;

				current_day++;
				current_day %= 7;
			}
		}
	}

	for (int i = 0; i < 6; i++) {
		fout << frequency[i] << " ";
	}

	fout << frequency[6] << endl;

	return 0;
}