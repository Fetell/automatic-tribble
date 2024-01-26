w = 9
h = 4

for i in range(h):
    for j in range(w):
        if i == 0 or i == 3 or j == 0 or j == w -1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
