/*
ID: csgregorian
PROG: ride
LANG: C++
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	ofstream fout("ride.out");
	ifstream fin("ride.in");

	string astr, bstr;
	fin >> astr >> bstr;

	int a, b;
	a = 1;
	b = 1;

	for (int i = 0; i < astr.length(); i++) {
		a *= astr[i] - int('A') + 1;
	}

	for (int i = 0; i < bstr.length(); i++) {
		b *= bstr[i] - int('A') + 1;
	}

	if (a % 47 == b % 47) {
		fout << "GO" << endl;
	} else {
		fout << "STAY" << endl;
	}


	
	return 0;

}