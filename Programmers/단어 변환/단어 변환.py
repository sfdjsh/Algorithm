def solution(begin, target, words):
    visited = [0] * len(words)  # 방문 체크 리스트

    q = [begin]  # 첫 시작 문자(begin) 추가

    # BFS 시작
    while q:
        word = q.pop(0)

        # 방문 리스트에서 이전 값을 더하기 위해, word와 같은, 방문 리스트 값 구하기
        v_cnt = 0
        for i in range(len(words)):
            if word == words[i]:
                v_cnt = visited[i]

        # 종료 조건
        if word == target:
            return max(visited)

        for w in range(len(words)):
            if not visited[w]:

                # 알파벳을 바꿀 수 있는 단어들 구하기
                cnt = 0
                for i in range(len(word)):
                    if word[i] == words[w][i]:
                        cnt += 1
                if len(word) - cnt == 1:        # 단어를 바꿀 수 있는 조건
                    visited[w] = v_cnt + 1
                    q.append(words[w])

    return 0    # 변환할 수 없는 경우