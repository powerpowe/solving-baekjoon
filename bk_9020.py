"""
    백준 9020번. 골드바흐의 추측
    난이도: 실버 1
    알고리즘: 수학, 정수론, 소수 판정, 에라토스테네스의 체
"""

from sys import stdin
input = stdin.readline

prime = [False, False, True] + [True, False] * 5000  # 0을 포함하며, 이미 2를 실행시킨 에라토스테네스의 체
for i in range(3, 101, 2):  # 3~99의 홀수들에 대해
    prime[2 * i::i] = [False] * (len(prime[2 * i::i]))


def goldbach(n):
    if n == 4:
        print(2, 2)
        return 0
    test_num = n // 2 if n % 4 == 2 else n // 2 - 1
    while (not prime[test_num]) or (not prime[n - test_num]): test_num -= 2
    print(test_num, n - test_num)


for i in range(int(input())):
    goldbach(int(input()))
