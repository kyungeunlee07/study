# 003 구간 합 구하기 1 https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
prefix_sum = [0]    # init prefix_sum

temp = 0
for i in data:    # accumulate arr section
    temp += i
    prefix_sum.append(temp)


for i in range(M):
    start, end = map(int, input().split())
    result = prefix_sum[end] - prefix_sum[start-1]
    print(result)

'''
!! 이 문제는 반복문 안에서 input()을 사용하므로 "input = sys.stdin.readline"을 사용 해야 한다. !!
input()은 하나씩 가공, sys.stdin.readline()은 한 번에 문자열 입력받아서 가공 그래서 더 빠름!
i~j 번째 수의 합은 (s[j] - s[i-1])이다.
이때 s[i] = a[0] + a[1] +...+ a[i]이다.
'''
