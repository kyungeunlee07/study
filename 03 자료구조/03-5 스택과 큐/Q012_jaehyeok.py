# 012 오큰수 구하기 https://www.acmicpc.net/problem/17298

N = int(input())
data = list(map(int, input().split()))
answer = [0]*N
stack = []

for i in range(N):
    # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while stack and data[stack[-1]] < data[i]:
        answer[stack.pop()] = data[i]   # 정답 리스트에 오큰수를 현재 수열로 저장하기
    stack.append(i)

# 스택에 남은 것들에 -1넣기
while stack:
    answer[stack.pop()] = -1

for i in range(N):
    print(answer[i], end=' ')
