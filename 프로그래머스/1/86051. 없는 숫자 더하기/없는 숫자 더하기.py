def solution(numbers):
    all_num = [1,2,3,4,5,6,7,8,9,0]
    num = list(set(all_num)-set(numbers))
    answer = 0
    for i in num:
        answer += i

    return answer