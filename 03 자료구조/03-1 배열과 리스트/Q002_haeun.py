# 002 평균 구하기 (백준 1546번)

n = int(input("과목의 개수 : "))
nums = [int(input("과목의 점수 : ")) for _ in range(n)]
max_num=nums[0] 

for i in nums:
    if i > max_num:
        max_num = i

def cal(nums):   
    sum = 0
    for n in nums:
        sum = sum + n
    return sum

sum = cal(nums)

print("새로운 평균 값 : ", sum/max_num*100/n)

# 책 코드
# n = input()
# mylist = list(map(int, input().split()))
# mymax = max(mylist)
# sum = sum(mylist)

# print(sum * 100 / mymax / int(n))
    
