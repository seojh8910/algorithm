def solution(n, control):
    answer = n
    for str in control:
        if str == "w":
            answer += 1
        elif str == "s":
            answer += -1
        elif str == "d":
            answer += 10
        else:
            answer += -10
    return answer