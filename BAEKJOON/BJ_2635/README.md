## 수 이어가기

### 문제 링크

https://www.acmicpc.net/problem/2635



### 문제

다음과 같은 규칙에 따라 수들을 만들려고 한다.

1. 첫 번째 수로 양의 정수가 주어진다.
2. 두 번째 수는 양의 정수 중에서 하나를 선택한다.
3. 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.



### INPUT

```
100
```



### OUTPUT

```
8
100 62 38 24 14 10 4 6
```