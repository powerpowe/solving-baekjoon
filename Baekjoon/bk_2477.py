"""
    백준 2477번. 참외밭
    난이도: 실버 3
    알고리즘: 수학, 구현, 기하학
    추가 설명:
        직사각형에서 파인 부분의 위치를 구해야 하는데,
         방향이 a b a b 순서로 들어오는 경우, 가운데 a (b a) b 가 파인 부분이다.
         ex) "북 서 남 동 남 동" 의 꼴로 들어오면, 4, 5번째 동 남이 파인 부분이므로
         전체 넓이에서 파인 넓이를 빼면 된다.
         이때, "남 동 북 서 남 동", "동 북 서 남 동 남" 등의 순서로 들어오는 경우
         리스트로 보면 남 동 남 동이 떨어져 있으므로 맨 앞 두 개를 뒤에 이어붙여서
         각각 "남 동 북 서 남 동 남 동", "동 북 서 남 동 남 동 북" 으로 만들어 준 뒤
         찾는다.
"""
K = int(input())

len_memory, dir_memory = [], []
max_width, max_height = 0, 0
concave_area = -1

for i in range(6):
    direction, length = (int(x) for x in input().split())
    dir_memory.append(direction)
    len_memory.append(length)

    # max_width, max_height를 찾아 오목한 부분까지 포함시킨 전체 사각형 넓이 구함.
    if direction in [1, 2]:
        max_width = max(max_width, length)
    else:
        max_height = max(max_height, length)

whole_area = max_width * max_height

# 오목한 부분의 넓이 구하기
len_memory.extend(len_memory[0:2])
dir_memory.extend(dir_memory[0:2])

for j in range(2, 8):
    if dir_memory[j - 2] == dir_memory[j] and dir_memory[j - 3] == dir_memory[j - 1]:
        concave_area = len_memory[j - 1] * len_memory[j - 2]

print(K * (whole_area - concave_area))