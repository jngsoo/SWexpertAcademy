#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    
    int T,N,M;                                  //Test case, CardN, CardM
    int min,max;                //N,M 중 큰 값은 max, 작은 값은 min 으로
    scanf("%d",&T);
    
    for(int test_case=1; test_case <= T; test_case++){   //Test case T만큼 반복
        
        scanf("%d %d",&N,&M);
        min = N<=M ? N : M;         //N,M 입력받아 작은 값은 N에
        
        if (min==N) max=M;          //큰 값은 M에 할당
        else max=N;
        
        printf("#%d ",test_case);                     //min에 1부터 (max-min+1) 한 값까지 1씩 더해가며 출력
        for (int j=1; j<=max-min+1; j++) {
            printf("%d ",min+j);
           
        }
        printf("\n");
    }
    
    
}



