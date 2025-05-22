a = int(input())

for i in range(0, a, 1):
    for j in range(0, i+1, 1):
        print("*", end="")
    print("")