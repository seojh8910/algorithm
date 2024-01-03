def solution(a, b):
    first_answer = int(str(a)+str(b))
    second_answer = 2*a*b
    answer = first_answer if first_answer > second_answer else second_answer
    return answer