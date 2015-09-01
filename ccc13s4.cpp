#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, m, x, y, p, q;

	cin >> n >> m;

	vector<int>* taller;
	taller = new vector<int>[1000000];

	for (int i = 0; i < m; i++) {
		cin >> x >> y;

		taller[x].push_back(y);
	}

	cin >> p >> q;

	stack<int>* stk;
	stk = new stack<int>;
	stk->push(p);

	int s;

	while (!stk->empty()) {
		s = stk->top();
		stk->pop();
		// cout << s;


		for (int i = 0; i < taller[s].size(); i++) {
			stk->push(taller[s][i]);
		}

		if (s == q) {
			cout << "yes" << endl;
			return 0;
		}
	}


	stack<int>* stk2;
	stk2 = new stack<int>;
	stk2->push(q);

	while (!stk2->empty()) {
		s = stk2->top();
		stk2->pop();

		for (int i = 0; i < taller[s].size(); i++) {
			stk2->push(taller[s][i]);
		}

		if (s == p) {
			cout << "no" << endl;
			return 0;
		}
	}

	cout << "unknown" << endl;
	return 0;
}