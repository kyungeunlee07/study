# 001 숫자의 합 구하기 (백준 11720번)

n = input()
numbers = list(input()) #list함수로 숫자를 한자리씩 나누어 입력받기

sum = 0 

for i in numbers: # for i in range(n) -> n을 활용한 코드
    sum += int(i) # int로 형 변환

print(sum)