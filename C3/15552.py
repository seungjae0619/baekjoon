import sys
T = int(sys.stdin.readline())
for i in range(0, T, 1):
    A, B = map(int, sys.stdin.readline().split())
    C = A + B
    print(C)