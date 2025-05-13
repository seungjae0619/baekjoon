h, m = map(int, input().split())
time = int(input())

m += time % 60
if m > 59:
    m -= 60
    h += 1
h += time // 60
if h > 23:
    h -= 24

print(h, m)