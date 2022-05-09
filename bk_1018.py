"""
    백준 1018번. 체스판 다시 칠하기
    난이도: 실버 5
    알고리즘: 브루트포스 알고리즘
"""
M, N = map(int, input().split())
board = []
minturn = 10000  # 임의로 큰 수 지정해둠
for i in range(M):
    board.append(input())
for j in range(0, N-7):  # 가로줄
    for k in range(0, M-7):  # 세로줄
        bft, wft, turn = 0, 0, 0
        for a in range(8):
            odd = board[k+a][j]+board[k+a][j+2]+board[k+a][j+4]+board[k+a][j+6]
            even = board[k+a][j+1]+board[k+a][j+3]+board[k+a][j+5]+board[k+a][j+7]
            bft = bft + odd.count('W') + even.count('B') if a % 2 == 0 else bft + odd.count('B') + even.count('W')
            wft = wft + odd.count('B') + even.count('W') if a % 2 == 0 else wft + odd.count('W') + even.count('B')
        turn = min(bft, wft)
        if turn < minturn:
            minturn = turn
print(minturn)
