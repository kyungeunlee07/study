# 11720. 숫자의 합 구하기

n = int(input())
s = int(input())


num_list=sum(list(map(int, str(s)))) # list로 바뀐 뒤, sum

print(num_list)