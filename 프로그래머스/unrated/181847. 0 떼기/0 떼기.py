def solution(n_str):
    for i, n in enumerate(n_str):
        if n != "0":
            break
    return n_str[i:]