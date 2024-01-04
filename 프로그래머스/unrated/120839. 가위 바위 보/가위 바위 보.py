def solution(rsp):
    win_dict = {"2": "0", "0": "5", "5": "2"}
    answer = ''
    for i in rsp:
        answer += win_dict[i]
    return answer