"""
    백준 2292번. 벌집
    난이도: 브론즈 2
    알고리즘: 수학
"""

N = int(input())
n = 1
while N > 1 + 3*n*(n-1):
    n += 1
print(n)
