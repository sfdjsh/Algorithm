## 야근 지수

### 문제 출저

https://school.programmers.co.kr/learn/courses/30/lessons/12927



### 문제 설명

회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

##### 제한 사항

- `works`는 길이 1 이상, 20,000 이하인 배열입니다.
- `works`의 원소는 50000 이하인 자연수입니다.
- `n`은 1,000,000 이하인 자연수입니다.



```python
# 처음 코드

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    cnt = 0
    while cnt < n:
        max_work = max(works)
        for i in range(len(works)):
            if works[i] == max_work:
                works[i] -=1
                cnt += 1
                break
                
    for i in works:
        answer += i**2
        
    return answer
```

```
위와 같은 코드를 작성했으나 효율성 테스트에서 시간 초과가 나왔다.
그래서 heap 자료구조를 이용해 시간 단축을 시켰다.
기본적으로 파이썬의 heap 라이브러리는 최소 힙이나 부호를 바꿔 저장하면 최대 힙과 비슷하게 사용할 수 있다.
```

```
heap 용어

heappush(list, 원소) : 힙에 원소를 추가
list : 원소를 추가할 대상 리스트
원소 : 추가할 원소

heappop(list) : 힙에서 원소를 삭제
- 가장 작은 원소를 삭제 후 그 값의 리스트를 리턴

heapify(list) : 기존의 리스트를 리스트 힙으로 변환
- 리스트 내부가 힙 구조에 맞게 재배치되며 최소값이 0번째 인덱스에 배치
```

