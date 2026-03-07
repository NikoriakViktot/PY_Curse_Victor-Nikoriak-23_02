#Task_3

overall_list = list(range(1,101))
result_list = []

i = 0
while i < len(overall_list):
    if overall_list[i] % 7 == 0 and overall_list[i] % 5 != 0:
        result_list.append(overall_list[i])
    i = i + 1

print(result_list)