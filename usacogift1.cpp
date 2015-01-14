/*
ID: csgregorian
PROG: gift1
LANG: C++
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
	ofstream fout("gift1.out");
	ifstream fin("gift1.in");

	int np;
	fin >> np;

	map<string, int> people;
	string people1[np+1];

	for (int i = 0; i < np; i++) {
		string person;
		fin >> person;
		people1[i] = person;
		people[person] = 0;
	}

	for (int i = 0; i < np; i++) {
		string giver;
		fin >> giver;

		int total;
		fin >> total;
		// cout << giver << " has " << total << endl;

		int receivers;
		fin >> receivers;
		for (int x = 0; x < receivers; x++) {
			string receiver;
			fin >> receiver;

			// cout << giver << " gives " << total/receivers << " to " << receiver << endl;


			people[receiver] += total / receivers;
			people[giver] -= total / receivers;
		}
	}

	for (int i = 0; i < np; i++) {
		fout << people1[i] << " " << people[people1[i]] << endl;
	}


	return 0;

}