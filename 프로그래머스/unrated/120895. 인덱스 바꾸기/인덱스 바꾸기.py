def solution(my_string, num1, num2):
    first_index_str = my_string[num1]
    second_index_str = my_string[num2]
    my_string = list(my_string)
    my_string[num1] = second_index_str
    my_string[num2] = first_index_str
    answer = ''.join(my_string)
    return answer