def solution(num_list):
    even = ''
    odd = ''
    for num in num_list:
        if num % 2 == 1:
            even += str(num)
        else:
            odd += str(num)
    answer = int(even) + int(odd)
    return answer