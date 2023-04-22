import sys
import math
input = sys.stdin.readline

T = int(input())

def find_step(d):
    """1 2 . . . peak . . . 2 1 = peak^2
    """
    optim_peak = int(d ** 0.5)
    remain = d - optim_peak
    if remain == 0:
        return optim_peak ** 2
    else:
        extra_step = math.ceil(remain / optim_peak)
        return optim_peak + extra_step
    
for _ in range(T):
    x, y = map(int, input().split())
    sys.stdout.write("%d\n"%(find_step(y - x)))
