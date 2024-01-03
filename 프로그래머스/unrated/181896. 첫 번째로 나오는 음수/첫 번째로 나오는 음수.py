def solution(num_list):
    minus_index = -1
    for i, n in enumerate(num_list):
        if n < 0:
            minus_index = i
            break
    return minus_index