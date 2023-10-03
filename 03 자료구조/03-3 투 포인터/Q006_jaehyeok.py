# 006 연속된 자연수의 합 구하기 https://www.acmicpc.net/problem/2018

n = int(input())
count = 1   # 1로 시작하는 이유는 자기 자신을 포함하고 시작하기 때문이다.
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
print(count)

'''
투 포인터 이동 원칙을 잘 생각 해내야 한다.
'''
