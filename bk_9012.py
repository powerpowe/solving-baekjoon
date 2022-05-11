"""
    백준 9012번. 괄호
    난이도: 실버 4
    알고리즘: 자료 구조, 문자열 ,스택
"""


import sys
T = int(input())
for _ in range(T):
    string = sys.stdin.readline().strip()
    stack = []
    flag = 'YES'
    for s in string:
        if s == '(':
            stack.append('(')
        else:
            if not stack:
                flag = 'NO'
                break
            stack.pop()
    if stack:
        flag = 'NO'
    print(flag)

