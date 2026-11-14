#include<bits/stdc++.h>
using namespace std;


int main(){
    vector<int>num =  {1, 2,3 ,45,55,66};
    num.at(1) = 20 ; 
    num.at(2) = 40;
    for(int i =0;i<num.size();i++){
        cout<<num[i]<<endl;
    }
}