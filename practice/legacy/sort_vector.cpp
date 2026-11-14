#include<bits/stdc++.h>
using namespace std; 

int main(){

    int n;cin>>n;

    vector<int>v(n);
    for(int i = 0 ; i < n ; i++){
        cin>>v[i];
    }
    int low , high , mid , targeted_value = 30; 
    low = 0 ;
    high = v.size() -1 ;
    mid = v.size() / 2 ; 
    while(low <=high){
        mid = (low + high);
        if(v[mid] == targeted_value){
            cout<<mid<<endl;
        }

        else if (v[mid] > targeted_value){
            high = mid  - 1 ;
        }
        else{
            low = mid  +1 ;
        }
        
    }

    return 0;
}