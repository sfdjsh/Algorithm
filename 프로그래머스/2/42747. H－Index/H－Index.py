def solution(citations):
    answer = 0

    citations.sort()
    for i in range(len(citations) + 1):
        up_citation, down_citation = 0, 0
        for j in range(len(citations)):
            if i <= citations[j]:
                down_citation = j
                up_citation = len(citations) - j
                break
        if up_citation >= i and down_citation < i:
            answer = i
                   
    return answer