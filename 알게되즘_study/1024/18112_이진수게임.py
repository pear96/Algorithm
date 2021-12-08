from collections import deque

start_binary = int(input().rstrip(), 2)
goal_binary = int(input().rstrip(), 2)

visited = [0] * 2048

queue = deque()
queue.append(start_binary)
visited[start_binary] = 1


while queue:
    now_binary = queue.popleft()
    if now_binary == goal_binary:
        print(visited[now_binary]-1)
        break

    for i in range(3):
        new_binary = now_binary
        # if start_binary == 1:
        if i == 0:
            for j in range(1, len(bin(now_binary)[2:])):
                new_binary = list(bin(new_binary)[2:])
                if j >= len(new_binary):
                    break
                if new_binary[j] == '1':
                    new_binary[j] = '0'
                else:
                    new_binary[j] = '1'
                new_binary = ''.join(new_binary)

                new_binary = int(new_binary, 2)
                if new_binary < 0 or new_binary >= 2048:
                    continue
                if visited[new_binary]:
                    continue
                visited[new_binary] = visited[now_binary] + 1
                queue.append(new_binary)
            continue
        elif i == 1:
            new_binary += 1
            new_binary = bin(new_binary)[2:]
        elif i == 2:
            new_binary -= 1
            new_binary = bin(new_binary)[2:]

        new_binary = int(new_binary, 2)

        if new_binary <= 0 or new_binary >= 2048:
            continue
        if visited[new_binary]:
            continue
        visited[new_binary] = visited[now_binary] + 1
        queue.append(new_binary)