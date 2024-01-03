def solution(str1, str2):
    count = str1.count(str2)
    if count > 0:
        answer = 1
    else: 
        answer = 2
    return answer