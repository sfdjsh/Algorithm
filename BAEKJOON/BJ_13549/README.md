## 숨바꼭질 3 (BAEKJOON_13549)

### 문제 출저

https://www.acmicpc.net/problem/13549



### 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.



### 풀이

```
백준에 있는 숨바꼭질(1697)번과 비슷하다고 생각하여 순간이동(2*X)하는 값에는 1을 더하지 않고 동생이 있는 위치를 찾게 했으나 X-1, X+1 이 2*X 보다 먼저 bfs를 돌아서 틀렸다고 나왔다. 
반례가 1 2 인 경우 0이 나와야하는데 리스트를 X-1, X+1 부터 돌면 값이 1이 나오기 때문에 답이 틀린다고 나온다. 그래서 for문을 2*X 먼저 돌게 하여 정답을 맞췄다.
```
