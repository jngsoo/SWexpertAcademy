/*
입력
1
3
A 10
B 7
C 5  

출력
#1
AAAAAAAAAA
BBBBBBBCCC
CC
*/

#include <iostream>
using namespace std;

int main() {
    
    int T,N,count10;

    cin >> T;       //Test case 개수 (1)

    for (int i=0; i<T; i++) {
        
        cin >> N;               //각 테스트 케이스의 줄 개수 N  (3)
        char c[N];              //{A,B,C}
        int n[N];               //{10,7,5}  1<=n<=20

        for (int j=0; j<N; j++) {
            cin >> c[j];       // 알파벳    (A,B,C)
            cin >> n[j];       // 알파벳 개수   (10,7,5)
        }
        

        cout << "#" << (i+1) << "\n";
        count10 = 0;
        for (int i=0; i<N; i++) {
            while (n[i] != 0){

                cout << c[i];
                n[i]--;
                count10++;

                if (count10==10) {
                    cout << "\n";
                    count10 = 0;
                }
            }
        
        cout << "\n";
        

        }
    cout << "\n";
    }
    return 0;
}

/*
2            
4
A 15
B 3
C 18
D 9
3
A 10
B 7
C 5

*/