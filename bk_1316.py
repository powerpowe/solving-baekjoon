"""
    백준 1316번. 그룹 단어 체커
    난이도: 실버 5
    알고리즘: 구현, 문자열
"""

N = int(input())
group_count = 0
for _ in range(N):
    word = input()
    group = True
    for s in set(word):  # 입력받은 문자의 각 알파벳들에 대해
        if s*word.count(s) not in word:
            group = False
            break
    if group:
        group_count += 1
print(group_count)
