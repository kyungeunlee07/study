#1546. 평균 구하기

sum = 0
N = int(input())

list_num = list(map(int, input().split())) 
max = list_num[0]

for i in range(0,N):
    sum += list_num[i]
    if max < list_num[i]:
        max = list_num[i]
    else:
        continue;

result = (sum* (100/max))/N
print(result)