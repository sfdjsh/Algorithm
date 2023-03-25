# 최빈값 구하기



## 문제 출저

https://school.programmers.co.kr/learn/courses/30/lessons/120812



###### 문제 설명

최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 `array`가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.



## CODE

```javascript
function solution(array) {
    
    var answer = [];
    
    let array_count = {}
    array.forEach((n) => {
        array_count[n] = ++array_count[n] || 1 
    })
    
    for (key in array_count) {
        answer.push([key, array_count[key]])
    }
    
    answer.sort((a, b) => b[1] - a[1])
    
    if (answer.length === 1) {
        return Number(answer[0][0])
    } else if (answer[0][1] === answer[1][1]) {
        return -1
    } else {
        return Number(answer[0][0])
    }
}
```

