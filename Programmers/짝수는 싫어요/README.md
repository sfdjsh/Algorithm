# 짝수는 싫어요



## 문제 출저

https://school.programmers.co.kr/learn/courses/30/lessons/120813



###### 문제 설명

정수 `n`이 매개변수로 주어질 때, `n` 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.



## CODE

```javascript
function solution(n) {
    var answer = [];
    
    for (let i=0; i <= n; i++) {
        if (i % 2 === 1) {
            answer.push(i)
        }
    }
        
    return answer;
}
```



