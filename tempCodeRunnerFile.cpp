#include<bits/stdc++.h>
using namespace std;

int main()
{
    
    int a[5][5];
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            cin>>a[i][j];
        }
    }

    int ans = 0 ; 

    for(int i = 1 ; i<=5;i++){
        for(int j = 1; j<=5;j++){
             if(a[i][j] ==1 ){
                ans = abs(3-i) + abs(3-j);
                break;
             }

        }
    }

    cout<<ans<<endl;


}