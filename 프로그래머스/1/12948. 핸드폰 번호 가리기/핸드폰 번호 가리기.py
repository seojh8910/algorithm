def solution(phone_number):
    answer = '*'*(len(phone_number) - 4) + ''.join(str(number) for number in phone_number[-4:])
    return answer