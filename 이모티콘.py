from collections import deque

s = int(input())
# visited[화면][클립보드]: 해당 상태에서의 최소 연산 횟수
visited = [[-1] * (s + 1) for _ in range(s + 1)]
q = deque([(1, 0)])  # 화면 이모티콘 수, 클립보드 이모티콘 수
visited[1][0] = 0

while q:
    screen, clipboard = q.popleft()

    # 목표 개수에 도달하면 종료
    if screen == s:
        print(visited[screen][clipboard])
        break

    # 복사하기 (화면 -> 클립보드)
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clipboard] + 1
        q.append((screen, screen))

    # 붙여넣기 (클립보드 -> 화면)
    if clipboard > 0 and screen + clipboard <= s and visited[screen + clipboard][clipboard] == -1:
        visited[screen + clipboard][clipboard] = visited[screen][clipboard] + 1
        q.append((screen + clipboard, clipboard))

    # 삭제하기 (화면 - 1)
    if screen > 0 and visited[screen - 1][clipboard] == -1:
        visited[screen - 1][clipboard] = visited[screen][clipboard] + 1
        q.append((screen - 1, clipboard))
