R, C, K = map(int, input().split())
golam = [list(map(int, input().split())) for _ in range(K)]
soop = [[0] * C for _ in range(R+3)]
dX_s = [-1, 0, 1, -1, 0, 1, 0]
dY_s = [-1, -1, -1, 0, 0, 0, 1]
dX = [0, 1, 0, -1, 0]
dY = [-1, 0, 1, 0, 0]
score = [0] * K
result = 0


def reset():
    global soop, score
    soop = [[0] * C for _ in range(R+3)]
    score = [0] * K


def check_s(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(len(dX_s)):
        dx = x + dX_s[j]
        dy = y + dY_s[j] +1
        if not ( 0 <= dx < C and dy < R+3):
            break
        if dy < 3:
            continue
        if soop[dy][dx] != 0:
            break
    else:
        golam[i][2], golam[i][3] = y + 1, x
        return True
    return False


def check_w(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(len(dX_s)):
        dx = x + dX_s[j] -1
        dy = y + dY_s[j] +1
        if not ( 0 <= dx < C and dy < R+3):
            break
        if dy < 3:
            continue
        if soop[dy][dx] != 0:
            break
    else:
        golam[i][2], golam[i][3] = y + 1, x - 1
        golam[i][1] += 3
        golam[i][1] %= 4
        return True
    return False


def check_e(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(len(dX_s)):
        dx = x + dX_s[j] +1
        dy = y + dY_s[j] +1
        if not ( 0 <= dx < C and dy < R+3):
            break
        if dy < 3:
            continue
        if soop[dy][dx] != 0:
            break
    else:
        golam[i][2], golam[i][3] = y + 1, x + 1
        golam[i][1] += 1
        golam[i][1] %= 4
        return True
    return False


def point(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(5):
        dx = x + dX[j]
        dy = y + dY[j]
        if 0 <= dx < C and 0 <= dy < R+3:
            soop[dy][dx] = i + 1

    cx, cy = x + dX[golam[i][1]], y + dY[golam[i][1]]
    score[i] = y + 1

    for j in range(4):
        dx = cx + dX[j]
        dy = cy + dY[j]
        if 0 <= dx < C and 0 <= dy < R+3 and soop[dy][dx] != 0 and soop[dy][dx] != i + 1:
            score[i] = max(score[i], score[soop[dy][dx]-1])

    return score[i]-2


for i in range(K):
    c, d = golam[i]

    golam[i].append(1)  # y
    golam[i].append(c-1)  # x

    while True:
        if check_s(i):
            continue
        if check_w(i):
            continue
        if check_e(i):
            continue
        break
    if golam[i][2] < 4:
        reset()
        continue
    result += point(i)

print(result)