def solution(A, B):
    answer = 0

    A.sort()    # 오름차순 정렬
    B.sort()    # 오름차순 정렬

    ai, bi = 0, 0
    while bi < len(B):      # 인덱스가 B의 길이보다 커지면 종료
        # A[인덱스] 숫자가 B[인덱스] 숫자보다 작으면,
        # 결과값 A인덱스 B인덱스 1 더하기
        if A[ai] < B[bi]:
            answer += 1
            ai += 1
            bi += 1
        # A[인덱스] 숫자가 B[인덱스] 숫자보다 작지 않다면, B인덱스만 더하기
        else:
            bi += 1

    return answer