def solution(myString, pat):
    answer = 0
    pat_len = len(pat)
    for i in range(len(myString)):
        try:
            test_str = myString[i:i + pat_len]
            if pat == test_str:
                answer += 1
        except:
            break
    return answer