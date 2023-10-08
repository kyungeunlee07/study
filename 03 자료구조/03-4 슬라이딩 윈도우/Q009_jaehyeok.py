# 009 슬라이딩 윈도우 https://www.acmicpc.net/problem/12891

myList = [0]*4
checkList = [0]*4
checkSecret = 0


def myadd(c):   # 새로 들어온 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


def myremove(c):    # 제거되는 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


S, P = map(int, input().split())
data = list(input())
checkList = list(map(int, input().split()))
count = 0

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myadd(data[i])

if checkSecret == 4:
    count += 1

for i in range(P, S):
    j = i - P
    myadd(data[i])
    myremove(data[j])
    if checkSecret == 4:
        count += 1

print(count)

'''
매번 모든 문자열을 확인하는 것은 너무 오래걸린다.
최초 상태 리스트에 A,C,G,T가 몇개 있는지 확인하고
한 칸씩 이동하면서(체크 리스트에서 맨 앞 글자는 제거하고, 새로운 글자는 추가한다.) 비밀번호가 유효한지 확인한다.
'''
