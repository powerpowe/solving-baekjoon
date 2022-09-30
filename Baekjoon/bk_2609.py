"""
    백준 2609번. 최대공약수와 최소공배수
    난이도: 실버 5
    알고리즘: 수학, 정수론, 유클리드 호제법
"""


def gcd(x, y):
    x, y = max(x, y), min(x, y)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


m, n = map(int, input().split())
print(gcd(m, n))
print(m * n // gcd(m, n))  # gcd(m, n)*lcm(m, n) = m * n임을 이용
