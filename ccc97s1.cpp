#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    scanf("%d", n);

    for (int i = 0; i < n; ++i) {
        int sub, verb, obj;
        scanf("%d %s %s", sub, verb, obj);

        vector<string> subs, verbs, objs;

        int cnt = 0;

        string input = "";
        for (int s = 0; s < sub; s++) {
            getline(cin, input);
            subs.push_back(input);
        }

        for (int v = 0; v < verb; v++) {
            getline(cin, input);
            verbs.push_back(input);
        }

        for (int o = 0; o < obj; o++) {
            getline(cin, input);
            objs.push_back(input);
        }

        for (string s : subs) {
            for (string v : verbs) {
                for (string o : objs) {
                    cout << s << " " << v << " " << o << "." << endl;
                }
            }
        }
    }
}
