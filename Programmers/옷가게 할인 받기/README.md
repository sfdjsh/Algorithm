# 옷가게 할인 받기



## 문제 출저

https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=javascript



###### 문제 설명

머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 `price`가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

------

##### 제한사항

- 10 ≤ `price` ≤ 1,000,000
  - `price`는 10원 단위로(1의 자리가 0) 주어집니다.
- 소수점 이하를 버린 정수를 return합니다.



## CODE

```javascript
function solution(price) {
    var answer = 0;
    
    if (price >= 500000) {
        answer += price * (100 - 20) / 100
    } else if (price >= 300000) {
        answer += price * (100 - 10) / 100
    } else if (price >= 100000) {
        answer += price * (100 - 5) / 100
    } else {
        answer += price
    }
    
    answer = Math.floor(answer)
    
    return answer;
}
```

