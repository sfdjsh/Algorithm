# 배열의 평균값



## 문제 출저

https://school.programmers.co.kr/learn/courses/30/lessons/120817



###### 문제 설명

정수 배열 `numbers`가 매개변수로 주어집니다. `numbers`의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

------

##### 제한사항

- 0 ≤ `numbers`의 원소 ≤ 1,000
- 1 ≤ `numbers`의 길이 ≤ 100
- 정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.



## CODE

```javascript
function solution(numbers) {
    var answer = 0;
    
    let sum_num = 0
    numbers.forEach(n => {
        sum_num += n
    })
    
    answer = sum_num / numbers.length
    
    return answer;
}
```



