#include <bits/stdc++.h>
using namespace std;

void selection_sort(vector<int>& v, int n) {

    for(int i = 0 ; i < n ; i++){
        int min  = i ; 
        for(int j =i+1 ; j <n; j++){
            if(v[j]<v[min]){
                min = j ; 
            }
        }

        swap(v[i],v[min]);
    }
}


void print_array(vector<int>& v) {

    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << ' ';
    }
    cout<<'\n';
}

int main() {

    int n;
    cin >> n;

    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    selection_sort(v, n);

    print_array(v);

    return 0;
}