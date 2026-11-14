#include<bits/stdc++.h>
using namespace std; 

int main(){

    vector<int>v;
    v.push_back(30);
    v.push_back(10);
    v.push_back(20);
    v.push_back(900);
    v.push_back(1022);
    v.push_back(332);
    v.pop_back();
    v.pop_back();
    v.push_back(100);
    v.push_back(300);
    v.push_back(322333);
    v.push_back(3324434);
    v.pop_back();
    v.pop_back();
    v.pop_back();
    v.pop_back();
    
    for(int i = v.begin(); i !=v.end();i++){
        cout<<v[i]<<endl;
    }

    return 0;
}