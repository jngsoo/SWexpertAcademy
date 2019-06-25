# (10 <= N <= 1000)

N = input()
tsn = ["3","6","9"]

#1부터 N까지 수를 차례대로 i
for i in range(1,int(N)+1):     #1부터 N(까지 포함)
    clap = 0                    # - 갯수 몇개 찍을지
    res = ""                    # res 는 숫자이거나 하이픈으로 될 것
    for j in str(i):            # j는 수 i의 백의자리, 십의자리, 일의자리...
        if j in tsn:            # 3,6,9 가 들어가잇다면
            clap += 1

    if clap != 0:               # 박수 쳐야되면 박수 갯수만큼 -을 출력 결과 단어 res에 추가
        res += "-"*clap
    else:                       # 3,6,9 하나도 포함 안되있다면 그대로 출력
        res = str(i)

    print(res, end=" ")
