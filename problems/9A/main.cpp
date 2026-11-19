
#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    int Y, W;
    cin >> Y >> W;

    int mx = max(Y, W);

    int numerator = 7 - mx;
    int denominator = 6;

    int g = gcd(numerator, denominator);

    cout << numerator / g << "/" << denominator / g << endl;

    return 0;
}
