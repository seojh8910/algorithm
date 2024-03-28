# a, b = map(int, input().strip().split(' '))
# garo = '*'* a
# for i in range(b):
#     print(garo)
# print(input().split(' '))
input_n_m_list = input().split(' ')
n = int(input_n_m_list[0])
m = int(input_n_m_list[-1])

width = '*' * n
for i in range(m):
    print(width)