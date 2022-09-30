"""
    백준 1004번. 어린 왕자
    난이도: 실버 3
    알고리즘: 기하학
    추가 설명:
        행성끼리 접하지 않으므로, 시작점, 끝점이 모두 어떠한 행성계 안에 있거나, 모든 행성계 밖에 있으면 된다.
        만약 두 점중 한 점만 행성계 안에, 나머지는 밖에 있다면 지나가는 길에 행성계와 무조건 만날 수밖에 없다.
        이를 파악하기 위해 반지름을 이용한다.
"""


def distance(X1, X2, Y1, Y2):
    return ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 0.5


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    meet = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if (distance(x1, cx, y1, cy) > r) != (distance(x2, cx, y2, cy) > r):
            meet += 1
    print(meet)
