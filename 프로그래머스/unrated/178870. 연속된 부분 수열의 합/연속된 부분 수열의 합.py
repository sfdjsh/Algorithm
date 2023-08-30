def solution(sequence, k):
    answer = []

    si = 0
    ni = -1
    sum = 0

    while si <= len(sequence):
        if sum == k:                    # 수열의 합이 k와 같으면 answer에 추가
            answer.append([si, ni])

        if sum < k:                     # 수열의 합이 k보다 작을 때
            ni += 1
            if ni >= len(sequence):
                break
            sum += sequence[ni]
        else:                           # 수열의 합이 k보다 클 때
            sum -= sequence[si]
            if si >= len(sequence):
                break
            si += 1

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))      # 길이가 작은 인덱스, 앞쪽에 나온 인덱스를 기준으로 정렬 
    return answer[0]