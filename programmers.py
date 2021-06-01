def solution(numbers, hand):
    answer = ''
    currentlkey = [0, 3]
    currentrkey = [2, 3]
    key = [0,0]
    nklist = []
    lk = [1,4,7]
    rk = [3,6,9]
    nk = [2,5,8,0]
    for i in numbers:
        if i in lk:
            answer+='L'
            currentlkey = [0, lk.index(i)]
        elif i in rk:
            answer+='R'
            currentrkey = [2, rk.index(i)]
        elif i in nk:
            nklist = [1,nk.index(i)]
            rdistance = abs(nklist[0]- currentrkey[0]) + abs(nklist[1] - currentrkey[1])
            ldistance = abs(nklist[0]- currentlkey[0]) + abs(nklist[1] - currentlkey[1])
            if rdistance == ldistance:
                if hand == "right":
                    answer+='R'
                    currentrkey = nklist
                else:
                    answer+='L'
                    currentlkey = nklist
            elif rdistance > ldistance:
                answer+='L'
                currentlkey = nklist
            else:
                answer+='R'
                currentrkey = nklist
    return answer
