T = int(input())                    # 테스트 케이스 갯수 T

for i in range(T):
    s = input()                     # KOREAKOREAKOREAKOREAKOREAKOREA
    for j in range(1, len(s)):
        if s[j] == s[0] and s[j + 1] == s[1]:   #s[j],s[j+1] = OR, RE, EA, AK, KO, ......
            LenOfPattern = j
            break
    print("#"+str(i+1),LenOfPattern)

                                    # AAAAAEAAAAAEAAAAAEAAAAAE ?
