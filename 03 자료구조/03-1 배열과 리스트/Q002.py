# 002 평균 구하기 https://www.acmicpc.net/problem/1546

N = int(input())
score = [*map(int, input().split())]
score.sort(reverse=True)

M = score[0]
sum = 0.0
for i in range(N):
    sum = sum + score[i]/M*100
avg = sum/N
print(avg)

'''
- map(int, ['1', '2', '3'])는 ['1', '2', '3']의 각 요소에 int() 함수를 적용하여 map 객체 [1, 2, 3]를 생성합니다.
- '*'은 map 객체를 unpacking하여 정수를 각각의 요소로 가지는 리스트를 생성해줍니다.
'*'를 안하면 score에는 map 객체만 들어가게 되어서 *로 unpacking 해줘야 한다.
'''
