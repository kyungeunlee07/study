# 010 최솟값 찾기1 https://www.acmicpc.net/problem/11003

from collections import deque

N, L = map(int, input().split())
data = list(map(int, input().split()))
check_list = deque()

for i in range(N):
    while check_list and check_list[-1][0] > data[i]:   # deque에서 들어올 값보다 큰 값 제거
        check_list.pop()
    check_list.append((data[i], i))     # 새로운 값 추가
    if check_list[0][1] <= i-L:     # 범위에서 벗어난 값은 제거
        check_list.popleft()
    print(check_list[0][0], end=' ')

'''
새로운 값이 들어올 때마다 정렬 하는 것은 시간이 오래걸리므로 현재 수보다 큰 값을 덱에서 제거해가는 방식으로 해야한다.
덱(deque)을 생각해내야한다!!!
'''
