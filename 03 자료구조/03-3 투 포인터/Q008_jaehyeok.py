# 008 '좋은 수' 구하기 https://www.acmicpc.net/problem/1253

N = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0

for i in range(N):
    start_index = 0
    end_index = N-1
    while start_index != end_index:
        sum = data[start_index] + data[end_index]
        if data[i] < sum:
            end_index -= 1
        elif data[i] > sum:
            start_index += 1
        else:
            if start_index != i and end_index != i:
                count += 1
                break
            elif start_index == i:
                start_index += 1
            elif end_index == i:
                end_index -= 1
print(count)

'''
if start_index != i and end_index != i:
                count += 1
                break
            elif start_index == i:
                start_index += 1
            elif end_index == i:
                end_index -= 1
이 부분이 핵심이다 다른 수 2개의 합이기 때문에 자기 자신을 제외하는 부분이 있어야 한다!
'''
