#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;cin>>n;
    if(n > 2 && n% 2 ==0){
        cout<<"YES"<<endl;
    }


    

    else{
        cout<<"NO"<<endl;
    }

    return 0;
}
