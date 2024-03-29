"""
    백준 10816. 숫자 카드 2
    난이도: 실버 4
    알고리즘: 자료구조, 정렬, 이분 탐색, 해시를 이용한 집합과 맵
    추가 설명:
        그냥 리스트에 넣고 루프돌면서 각각 리스트에서 찾아서 계산 시 O(n^2)이 되어
        시간 초과될 것임. 따라서 딕셔너리를 이용해 O(n)만에 해결함.
"""

N = int(input())
card = [int(x) for x in input().split()]
M = int(input())
find = [int(x) for x in input().split()]

card_dict = {}
for i in card:  #O(n)
    if i in card_dict:  #O(1)
        card_dict[i] += 1
    else:
        card_dict[i] = 1
for i in find:  #O(n)
    print(card_dict[i] if i in card_dict else 0, end=' ')