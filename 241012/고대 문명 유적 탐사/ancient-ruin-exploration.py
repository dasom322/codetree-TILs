from collections import deque
import copy

K, _ = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(5)]
num = list(map(int, input().split()))
dX = [-1, 0, 1, 1, 1, 0, -1, -1]
dY = [-1, -1, -1, 0, 1, 1, 1, 0]
score_list = []
num = deque(num)


def function_1(i, j, k):
    list1 = []
    for idx in range(len(dX)):
        y, x = j + dY[idx], i + dX[idx]
        list1.append(_map[y][x])

    map1 = copy.deepcopy(_map)
    for idx in range(len(dX)):
        iidx = (idx + (k + 1)*2) % 8
        y, x = j + dY[iidx], i + dX[iidx]
        map1[y][x] = list1[idx]

    # used = [[0]*5 for _ in range(5)]
    result = 0
    for x in range(5):
        for y in range(5):
            if map1[y][x] == 0:
                break
            queue = deque([(y, x, map1[y][x])])
            map1[y][x] = 0
            cnt = 1
            while queue:
                jj, ii, ss = queue.popleft()
                for iii in range(1, 8, 2):
                    dx = dX[iii] + ii
                    dy = dY[iii] + jj
                    if 0 <= dx < 5 and 0 <= dy < 5 and map1[dy][dx] == ss:
                        queue.append((dy, dx, map1[dy][dx]))
                        map1[dy][dx] = 0
                        cnt += 1
            if cnt > 2:
                result += cnt
    return result


def function_2(i, j, k):
    list1 = []
    for idx in range(len(dX)):
        y, x = j + dY[idx], i + dX[idx]
        list1.append(_map[y][x])
    
    for idx in range(len(dX)):
        iidx = (idx + (k + 1)*2) % 8
        y, x = j + dY[iidx], i + dX[iidx]
        _map[y][x] = list1[idx]

    #map1 = copy.deepcopy(_map)
    list1 = []
    result = 0
    flag = True
    while flag:
        flag = False
        map1 = copy.deepcopy(_map)
        for x in range(5):
            for y in range(5):
                if map1[y][x] == 0:
                    break
                queue = deque([(y, x, map1[y][x])])
                map1[y][x] = 0
                cnt = 1
                list1 = [(x, y)]
                # list1.append()
                while queue:
                    jj, ii, ss = queue.popleft()
                    for iii in range(1, 8, 2):
                        dx = dX[iii] + ii
                        dy = dY[iii] + jj
                        if 0 <= dx < 5 and 0 <= dy < 5 and map1[dy][dx] == ss:
                            queue.append((dy, dx, map1[dy][dx]))
                            map1[dy][dx] = 0
                            list1.append((dx, dy))
                            cnt += 1
                if cnt > 2:
                    flag = True
                    list1.sort(key=lambda x: (x[0], -x[1]))
                    for xx, yy in list1:
                        _map[yy][xx] = num.popleft()
                    result += cnt

    return result


for _ in range(K):
    case_list = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(3):
                case_list.append([function_1(i, j, k), k, i, j])
    case_list.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    if case_list[0][0] == 0:
        break
    # 1차
    i, j, k = case_list[0][2], case_list[0][3], case_list[0][1]

    score = function_2(i, j, k)

    score_list.append(score)

print(" ".join(map(str, score_list)))