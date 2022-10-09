def solution(n, s):
    answer = []

    # s가 n보다 작으면 집합으로 나눌 수 없음
    if s < n:
        return [-1]

    # 집합의 차이가 적을수록 집합의 곱은 커짐
    # 원소의 합 s를 자연수 n으로 나눈 수를 n만큼 append
    mid = s // n
    for _ in range(n):
        answer.append(mid)

    # s와 n의 나머지를 총 합이 s가 될 때까지 더해주기
    remin = s % n
    idx = len(answer) - 1
    for _ in range(remin):
        answer[idx] += 1
        idx -= 1    # 오름차순이기 때문에 뒤에서 부터 더해주기

    return answer