# 007 주몽 https://www.acmicpc.net/problem/1940

N = int(input())
M = int(input())
data = list(map(int, input().split()))
start_index = 0
end_index = N-1
count = 0

data.sort()

while start_index < end_index:
    sum = data[start_index] + data[end_index]
    if sum < M:
        start_index += 1
    elif sum == M:
        count += 1
        start_index += 1
        end_index -= 1
    else:
        end_index -= 1

print(count)
