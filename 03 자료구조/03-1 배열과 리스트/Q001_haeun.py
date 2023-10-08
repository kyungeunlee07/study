# 001 숫자의 합 구하기 (백준 11720번)

n=input("숫자의 개수 :")
nums = list(input("각 자릿수 더할 N개의 숫자 :"))
sum = 0

for i in nums:
    sum = sum+int(float(i)) # 형변환 오류
    
print(sum)
