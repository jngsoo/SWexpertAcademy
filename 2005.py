T = int(input())

for i in range(T):
    N = int(input())+1  #1 <= N <= 10 (삼각형 변의 길이)
    print("#"+str(i+1))

    for row in range(N):
        start = 1
        toRow = [start]
        print(start, end=" ")

        for digit in range(row):
            start = start * (row-digit) / (digit + 1)
            toRow.append(int(start))

            print(str(int(start)).rjust(3),end=" ")
            # print("\ntoRow = ", toRow)
        print()