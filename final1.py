v_inp = input().split(',')
m = int(v_inp[0])
n = int(v_inp[1])

data = list()
for i in range(m):
    sub = list()
    input1 = input().split(',')
    for j in range(n):
        sub.append(int(input1[j]))
    data.append(sub)

distance_list = []
for j in range(m - 1):
    for k in range(j + 1, m):
        distance = 0
        for r in range(n):
            distance += (data[j][r] - data[k][r]) ** (2)
        distance_list.append(distance)
            

print(min(distance_list))
