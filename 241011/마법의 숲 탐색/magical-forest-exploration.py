R, C, K = map(int, input().split())
golam = [list(map(int, input().split())) for _ in range(K)]
soop = [[0] * (C + 1) for _ in range(R + 1)]
dX_s = [-1, 0, 1]
dY_s = [1, 2, 1]
dX_w = [-1, -2, -2, -1, -1]
dY_w = [-1, 0, 1, 1, 2]
dX_e = [1, 2, 2, 1, 1]
dY_e = [-1, 0, 1, 1, 2]
dX = [0, 1, 0, -1, 0]
dY = [-1, 0, 1, 0, 0]
score = [0] * K
result = 0


def reset():
    global soop, score
    soop = [[0] * (C + 1) for _ in range(R + 1)]
    score = [0] * K


def check_s(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(3):
        dx = x + dX_s[j]
        dy = y + dY_s[j]
        if dy <= 0:
            continue
        if 0 < dx < C + 1 and 0 < dy < R + 1:
            if soop[dy][dx] != 0:
                break
        else:
            break
    else:
        golam[i][2], golam[i][3] = y + 1, x
        return True
    return False


def check_w(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(5):
        dx = x + dX_w[j]
        dy = y + dY_w[j]
        if dy <= 0:
            continue
        if 0 < dx < C + 1 and 0 < dy < R + 1:
            if soop[dy][dx] != 0:
                break
        else:
            break
    else:
        golam[i][2], golam[i][3] = y + 1, x - 1
        golam[i][1] += 3
        golam[i][1] %= 4
        return True
    return False


def check_e(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(5):
        dx = x + dX_e[j]
        dy = y + dY_e[j]
        if dy <= 0:
            continue
        if 0 < dx < C + 1 and 0 < dy < R + 1:
            if soop[dy][dx] != 0:
                break
        else:
            break
    else:
        golam[i][2], golam[i][3] = y + 1, x + 1
        golam[i][1] += 5
        golam[i][1] %= 4
        return True
    return False


def point(i):
    y, x = golam[i][2], golam[i][3]
    for j in range(5):
        dx = x + dX[j]
        dy = y + dY[j]
        if 0 < dx < C + 1 and 0 < dy < R + 1:
            soop[dy][dx] = i + 1

    cx, cy = x + dX[golam[i][1]], y + dY[golam[i][1]]
    score[i] = y + 1

    for j in range(4):
        dx = cx + dX[j]
        dy = cy + dY[j]
        if 0 < dx < C + 1 and 0 < dy < R + 1 and soop[dy][dx] != 0 and soop[dy][dx] != i + 1:
            score[i] = max(score[i], score[soop[dy][dx] - 1])

    return score[i]


for i in range(K):
    c, d = golam[i]
    if soop[1][c] != 0:
        reset()
        continue
    golam[i].append(0)  # y
    golam[i].append(c)  # x

    while True:
        if check_s(i):
            continue
        if check_w(i):
            continue
        if check_e(i):
            continue
        break
    if golam[i][2] < 2:
        reset()
        continue
    result += point(i)

print(result)