"""
    백준 11653. 소인수분해
    난이도: 실버 5
    알고리즘: 수학, 정수론, 소수 판정
"""

n = int(input())
i = 2
upper_bound = int(n ** 0.5)  # sqrt(n) 이하의 소수에 대해서만 체크해도 된다.

while i <= upper_bound:
    while not n % i:  # 안 나뉠 때까지 나눠 본다.
        print(i)
        n = n // i
    # 다 나뉜 후에, 나누는 숫자를 1 증가시킨다.
    # 만약 i가 합성수라면, 반드시 앞에서 그 합성수를 나누는 수로 다 나눠졌으므로 나눠지지 않는다.
    i += 1
if n > 1:
    print(n)
