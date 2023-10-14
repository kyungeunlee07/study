# 002 평균 구하기 (백준 1546번)

n = int(input()) # n 처음 입력받을 때 int형으로

score = list(map(int,input().split()))

max_score = max(score) # score의 최댓값 저장
sum_score = sum(score) # score의 합 저장

print(sum_score*100/max_score/n)