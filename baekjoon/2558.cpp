// https://www.acmicpc.net/problem/2558
#include <iostream>
#include <string>
using namespace std;

int main(){
    string a, b;
    getline(cin, a);
    getline(cin, b);

    cout << stoi(a) + stoi(b) << endl;
    return 0;
}