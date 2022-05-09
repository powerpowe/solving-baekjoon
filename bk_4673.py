"""
    백준 4673번. 셀프 넘버
    난이도: 실버 5
    알고리즘: 수학, 구현, 브루트포스 알고리즘
"""


num, self = set(range(1, 10001)), set()
for i in range(1, 10001):  # 1에서 10000까지의 숫자에 대해 d(n)을 구하여 self에 넣는다.
    self.add(i+sum(map(int, list(str(i)))))
for i in sorted(num-self):
    print(i)
