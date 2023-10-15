# 11658. 구간 합 구하기 

# 시간 초과 원인 2가지 
# 1. 누적 합을 이용하지 않고 단순 합계를 이용하면 시간초과 ( 총 합에서 이전까지 합 빼기 )
# 2. input() 으로 입력을 받아서 시간 초과 (sys 사용 )

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
result_list=[0]
sum = 0

for i in range(n): # 차례로 더한 값들을 리스트에 저장
    sum += num_list[i]
    result_list.append(sum)

for i in range(m):  # ex) 2~4 까지 합 = 4까지 더한 값에서 1까지 더한 값을 뺌 
    a, b = map(int, input().split())
    print(result_list[b]-result_list[a-1] )
   