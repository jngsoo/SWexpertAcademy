'''

1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)

2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)

3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.

'''

grades = ['A+','A0','A-',
          'B+','B0','B-',
          'C+','C0','C-',
          'D0']


T = int(input())        #테스트 케이스 갯수


for t in range(T):
    N, K = input().split()  # 학생 수 N, 학점을 알고싶은 학생 번호 K
    N, K = int(N), int(K)

    totalScores = []  # 중간, 기말, 과제 점수 반영 비율 합산한 최종 점수 담을 배열 (len(totalScores) == T)
    for i in range(N):

        mid, fin, assign = input().split()
        totalScores.append(int(mid)*0.35 + int(fin)*0.45 + int(assign)*0.2)

    Kscore = totalScores[K-1]

    biggerThan_K = 0

    for score in totalScores:
        if score > Kscore:
            biggerThan_K += 1

    divider = int(biggerThan_K / (N/10)%10)
    print("#"+str(t+1),grades[divider])