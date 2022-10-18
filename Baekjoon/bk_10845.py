"""
    백준 10845번. 큐
    난이도: 실버 4
    알고리즘: 자료 구조, 큐
    추가 설명:
        큐를 만들어 보는 문제로, deque 모듈을 이용하여 popleft()를 O(1)만에 가능하게 함.
        특이사항으로는 시간 제한이 깐깐하므로 input() 대신 sys.stdin.readline()을 필수로 사용해야 함.
        파이썬의 len(list)는 O(1)만에 작동하므로 그냥 사용하여도 무방하다.
"""
from collections import deque
import sys

data = deque([])

input = sys.stdin.readline
for _ in range(int(input())):  # O(N)
    temp = input().split()

    if len(temp) == 2:  # O(1)
        data.append(temp[1])

    else:
        order = temp[0]

        if order == 'pop':  # O(1)
            if len(data):
                print(data.popleft())

            else:
                print(-1)

        elif order == 'size':  # O(1)
            print(len(data))

        elif order == 'empty':  # O(1)
            print(0 if len(data) else 1)

        elif order == 'front':  # O(1)
            if len(data):
                print(data[0])

            else:
                print(-1)

        elif order == 'back':  # O(1)
            if len(data):
                print(data[-1])

            else:
                print(-1)