"""
그러니까, 뒤로갈 때, 앞으로갈 때, 순간이동할 때 3가지가 있고, 한번 움직이면 그 안에서 또 세번의 경우의 수가 있고...
근데 이러면 완탐 아냐?? 괜찮나?? 근데 이거 이미 방문한거면 안가겠다는 건가??
그러면 방문 리스트를 만들어?근데 뒤로도 가야하면... 음 0이면 뒤로 못가게 해야겠네?
그럼 리스트 크기가... N부터 K까지? 근데, N이 꼭 K보다 작다는 보장 있어? 그럼 크기는 0부터 K까지?... 아니지 N이 크면 N까지??
그냥 십만으로 해? 메모리 너무 많이 쓰는거 아냐? 상관없나? 모르겠따... 0ㅇ0

그러면 N이 K보다 크면 뒤로 가야하고(근데 0이면 뒤로 못감. 애초에 N이 0이면 K가 뒤에 있을 수 없지)
N이 K보다 작은데,
N * 2 가 K보다 작으면 순간이동을 해야하잖아...
N * 2 보다 K가 작으면 순간이동은 안하겠지...
그러면 언제 앞으로 가고 언제 뒤로 가지?? 그냥 둘다 가??
근데 이거 방문 한거 체크 해도 되는거야?? 이미 방문 했으면 안가?? 하긴 그래도 되겠다. 어차피 거기 갔으면 그 이후 진행 했을텐데. 우린 빠른걸 찾는거잖아?


조건에 따라 순간이동을 하니 마니 뒤로 가니 마니 따지려다가 코드를 못 짰다. 그냥 그것과 상관없이 묻고 갔으면 되는 것....
dfs만 하다보니 갑자기 dfs로 가서 계속 뒤로만 가길래 어 뭔가 이상함을 느끼고 보니 bfs를 그새 까먹음
queue 부르고 코드 다시 짬ㅎㅎ.. bfs 잘 짜다가 또 끝내는 조건 위치 정하느라 오래걸림. 나는 next가 동생 위치면 끝내고 싶었는데
visited 계산 이후에 하려다가 또 방법 못찾고 그냥 도착 위치에 왔을 때 끝냄...
"""
from collections import deque  # bfs를 위해 queue 사용
N, K = map(int, input().split())
visited = [0] * 100001  # 100000 했다가 index error...ㅎ
answer = 0
queue = deque()


def bfs():
    global answer

    while queue:
        subin = queue.popleft()  # 현재 수빈의 위치를 보면서
        if subin == K:  # 동생을 잡았어요!
            if visited[subin] == 0:  # 우린 같은 자리에 있었어...
                answer = 1
            else:
                answer = visited[subin]  # 왜 이거 else처리 안했는데 맞았지? 수빈과 동생이 같은 위치인 경우가 한번도 없었나...
            return  # 찾았으니 끝!끝!
        for route in range(3):
            # 다음 갈 곳 route 값으로 설정하기 ㅜ 이딴식으로밖에 못해? 느껴진다 코드 이거 이렇게까지 길 필요가 없다.
            if route == 0:  # 그냥 3 방법 중 순서대로 진행
                next_subin = subin - 1  # 뒤로 가는 경우
            elif route == 1:
                next_subin = subin + 1  # 앞으로 가는 경우
            elif route == 2:
                next_subin = subin * 2  # 순간이동 하는 경우

            # 못갈 위치는 처리를 했으니 안심하라구
            if next_subin < 0 or next_subin > 100000:
                continue
            if visited[next_subin]: # 방문했으면 먼저 왔다 간거고 우린 최소 시간을 찾는거니 또 갈 필요가 없다.
                continue

            visited[next_subin] = visited[subin] + 1  # 걸린 시간을 추출해내기 위해서~
            queue.append(next_subin) # 다음 위치로 간다

queue.append(N) # 현재 수빈의 위치를 queue에 넣고
visited[N] = 1 # 방문 표시를 해준다음(안하면 또 감)
bfs() # 탐색 시작
print(answer - 1) # 처음 위치는 0초인데 visited가 1부터 시작했으니 1을 빼준다.


