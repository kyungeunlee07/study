# 001 숫자의 합 구하기 https://www.acmicpc.net/problem/11720

N = int(input())
number = int(input())
result = 0

while number > 0:
    result += number % 10
    number = number // 10
print(result)

'''
'/'는 실수형 리턴 ex) 2/3 = 0.666666
'//'는 몫만 리턴 ex) 3//2 = 1
'%'는 나머지 값만 리턴 ex) 2%3 = 2
'''
