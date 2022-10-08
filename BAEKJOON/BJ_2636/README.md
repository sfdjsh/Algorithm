## 치즈 (BAEKJOON_2636)

### 문제 출저

https://www.acmicpc.net/problem/2636



### 문제

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다. 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어진다. 

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.



```
처음엔 visited 배열을 while문 밖으로 만들어서 한시간이 지나면 더 이상 행렬을 진행할 수 없었다.
그래서 while문 안에 visited을 만들면서 while이 돌 때마다 visited 배열을 초기화하는 식으로 진행하였다.
```
