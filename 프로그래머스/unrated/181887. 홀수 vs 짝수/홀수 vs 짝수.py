def solution(num_list):
    even_num_sum = 0
    odd_num_sum = 0
    for i, num in enumerate(num_list):
        if i%2 == 1:
            odd_num_sum += num
        else:
            even_num_sum += num
    if odd_num_sum > even_num_sum:
        answer = odd_num_sum
    else: 
        answer = even_num_sum
    return answer