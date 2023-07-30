# input_num = int(input())
# counter = 0
# string_num = ''
# num = abs(input_num)
# if input_num == 0:
#     print('0')
# else:
#     while counter < num:
#         string_num += str(counter) * counter
#         counter += 1
# s = string_num[:num]
# print(*s)

input_num = int(input())
list_0 = []
for i in range(1, input_num + 1):
    for j in range(1, i + 1):
        list_0.append(i)
print(*list_0[:input_num])