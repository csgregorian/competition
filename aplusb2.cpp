#include <iostream>
#include <string>

using namespace std;

int main() {
	string astring, bstring;
	cin >> astring >> bstring;

	int length = max(astring.length(), bstring.length());

	int a[length+1];
	int b[length+1];
	int c[length+1];

	for (int i = 0; i < length; i++) {
		a[i] = astring[i] - '0';
		//cout << a[i];
	}

	//cout << endl;

	for (int i = 0; i < length; i++) {
		b[i] = bstring[i] - '0'; 
		//cout << b[i];
	}

	//cout << endl;


	int carry = 0;

	for (int i = length - 1; i >= 0; i--) {
		c[i] = (a[i] + b[i] + carry) % 10;
		carry = (a[i] + b[i] + carry) / 10;
	}

	for (int i = 0; i < length; i++)
		cout << c[i];

	cout << endl;




	return 0;
}
