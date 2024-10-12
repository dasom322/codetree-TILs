N, M, P, C, D = map(int, input().split())
rudolf = list(map(int, input().split()))
santa = [ list(map(int, input().split()))+[1, 0] for _ in range(P)]

grid = [[0]*(N+1) for _ in range(N+1) ]
dY=[-1, 0, 1, 0]
dX=[0, 1, 0, -1]

grid[rudolf[0]][rudolf[1]] = -1
santa.append([0,0,0,0,0])
santa.sort()
for i in range(1,P+1):
    grid[santa[i][1]][santa[i][2]] = santa[i][0]

def rudolf_go(dy, dx):
    grid[rudolf[0]][rudolf[1]] = 0
    rudolf[0] += dy
    rudolf[1] += dx
    
    #충돌1
    if grid[rudolf[0]][rudolf[1]] != 0:
        santa_number = grid[rudolf[0]][rudolf[1]]
        santa[santa_number][4] += C
        santa[santa_number][3] = 3 #기절
        santa[santa_number][1] += (C*dy)
        santa[santa_number][2] += (C*dx)

        while True: # 상호작용
            if not (0 < santa[santa_number][1] < N+1 and 0 < santa[santa_number][2] < N+1):
                santa[santa_number][3] = 0 #탈락
                break

            new_santa = grid[santa[santa_number][1]][santa[santa_number][2]]
            grid[santa[santa_number][1]][santa[santa_number][2]] = santa_number
            
            if new_santa == 0:
                break
            santa_number = new_santa
            santa[santa_number][1] -= dy
            santa[santa_number][2] -= dx
    grid[rudolf[0]][rudolf[1]] = -1
    


def santa_alive():
    for s in santa:
        if s[3] != 0:
            return True
    return False

def santa_go(p, dy, dx):
    grid[santa[p][1]][santa[p][2]] = 0
    santa[p][1] += dy
    santa[p][2] += dx
    
    #충돌1
    if grid[santa[p][1]][santa[p][2]] == -1:
        santa_number = p
        santa[santa_number][4] += D
        santa[santa_number][3] = 3 #기절
        santa[santa_number][1] -= (D*dy)
        santa[santa_number][2] -= (D*dx)

        while True: # 상호작용
            if not (0 < santa[santa_number][1] < N+1 and 0 < santa[santa_number][2] < N+1):
                santa[santa_number][3] = 0 #탈락
                break

            new_santa = grid[santa[santa_number][1]][santa[santa_number][2]]
            grid[santa[santa_number][1]][santa[santa_number][2]] = santa_number
            
            if new_santa == 0:
                break
            santa_number = new_santa
            santa[santa_number][1] -= dy
            santa[santa_number][2] -= dx
    else:
        grid[santa[p][1]][santa[p][2]] = p

for _ in range(M):
    #print(1)

    #(2)루돌프의 움직임
    #루돌프의 거리계산
    dis = []
    for x in santa:
        if x[3] == 0:
            continue
        dis.append([(rudolf[0] - x[1])**2 + (rudolf[1] - x[2])**2, x[1], x[2]])
    
    dis.sort(key = lambda x: (x[0], -x[1], -x[2]))

    #루돌프 돌진
    if dis[0][1] != rudolf[0]:
        dy = int((dis[0][1] - rudolf[0])/abs(dis[0][1] - rudolf[0]))
    else:
        dy = 0
    if dis[0][2] != rudolf[1]:
        dx = int((dis[0][2] - rudolf[1])/abs(dis[0][2] - rudolf[1]))
    else:
        dx = 0
    rudolf_go(dy, dx)
    if not santa_alive: #산타 모두 탈락
        break
    
    for s in santa:
        if s[3] != 1:
            continue
        #방향 계산
        dis = [] #(거리, 방향)
        for i in range(4):
            yy = s[1] + dY[i]
            xx = s[2] + dX[i]
            if not (0 < xx < N+1 and 0< yy < N+1):
                continue
            if grid[yy][xx] not in [0, -1]:
                continue
            dis.append([ (rudolf[0] - yy)**2 + (rudolf[1] - xx)**2, i])

        if len(dis) == 0:
            continue
        dis.sort()
        dy = dY[dis[0][1]]
        dx = dX[dis[0][1]]
        santa_go(s[0], dy, dx)

    if not santa_alive: #산타 모두 탈락
        break

    #턴 종료 산타 +1점
    for s in santa:
        if s[3] != 0:
            santa[s[0]][4] += 1
        if s[3] > 1:
            santa[s[0]][3] -= 1

for i in range(1, P+1):
    print(santa[i][4], end=" ")