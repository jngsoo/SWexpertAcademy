#날짜별 매매가를 담은 리스트를 입력받으면 이익을 return

def calc(costs):
    profit = 0          #계산할 이익값
    costs.reverse()     #매매가를 날짜 역순으로 뒤집음 (배열 costs)      [1,1,3,1,2] => [2,1,3,1,1]
    curcost = costs[0]      #2
    for i in range(1,len(costs)):
        if costs[i] < curcost:          #curcost 보다 과거날짜의 매매가가 저렴하다면 판매, 이익
            profit += curcost-costs[i]
        elif costs[i] > curcost:        #과거 날짜의 매매가가 더 높다면 curcost를 해당 날짜의 매매가로 재할당
            curcost = costs[i]

    return(profit)



T = int(input())        # 테이스 케이스 수 T

for i in range(T):

    N = int(input())        #입력받으나 사용하진 않음

    prices = input().split()    #['10','7','6'] 형태의 문자열 담은 리스트

    for j in range(len(prices)):        #위 문자열 리스트를 [10,7,6]의 정수형 원소를 갖는 리스트로 변환
        prices[j] = int(prices[j])

    print("#"+str(i+1),calc(prices))
