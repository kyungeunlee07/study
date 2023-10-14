# 011 스택 수열 https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

n = int(input())
data = [0]*n
stack = []
current = 1
answer = ""
result = True

for i in range(n):
    temp = int(input())
    if temp >= current:     # 현재 수열값 >= 오름차순 자연수 값이 같아질 때까지 append() 진행
        while temp >= current:
            stack.append(current)
            current += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:   # 현재 수열값 < 오름차순 자연수 pop()을 수행해 수열 원소를 꺼냄
        top = stack.pop()
        if top > temp:  # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 불가능함
            result = False
            print("NO")
            break
        else:
            answer += "-\n"

if result:
    print(answer)
