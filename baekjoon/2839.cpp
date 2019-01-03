// https://www.acmicpc.net/problem/2839
#include <iostream>
using namespace std;

int main() {
    int n, five, min=-1;
    cin >> n;
    if(n%5==0) min=n/5;
    else five = n/5;
    while(min==-1 && five>=0){
        if((n-5*five)%3==0) min = five+(n-5*five)/3;
        five -= 1;
    }
    cout << min << endl;

    return 0;
}