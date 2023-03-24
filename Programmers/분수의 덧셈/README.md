# 분수의 덧셈(Programmers)



## 문제 출저

https://school.programmers.co.kr/learn/courses/30/lessons/120808



###### 문제 설명

첫 번째 분수의 분자와 분모를 뜻하는 `numer1`, `denom1`, 두 번째 분수의 분자와 분모를 뜻하는 `numer2`, `denom2`가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.



## CODE

```javascript
function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    max_num = 1
    for (i = 2; i <= denom; i++) {
        if (numer % i === 0 && denom % i === 0) {
            max_num = i
        }
    }
    
    answer.push(numer / max_num, denom / max_num)
    
    return answer;
}
```



