# 시그널(BAEKJOON_16113)



## 문제 출저

https://www.acmicpc.net/problem/16113



## 문제

zxcvber는 외계인을 연구하는 과학자다. 그는 지난 10년간 우주에서 오는 시그널를 연구했지만, 아무런 성과가 없었다. 그러던 어느 날, 갑자기 우주에서 이상한 시그널이 오기 시작했다. zxcvber는 매우 기뻐하며 시그널을 받아서 분석해보았다. 시그널은 0과 1로 이루어져 있는데, 여기서는 편의상 0을 "`.`", 1을 "`#`"으로 표시한다. 시그널은 다음과 같았다.

```
###.....###.#..####.#.......#.#....####.....###.#....##.#.......#.#....####.....###.#....#
```

다른 여러 시그널들을 분석해본 결과, zxcvber는 시그널의 길이가 항상 5의 배수라는 것을 알게 되었다. 시그널을 다섯 개로 쪼개면 뭔가 규칙이 보이지 않을까 생각한 zxcvber는 시그널을 같은 길이의 5개의 시그널로 쪼갰다. 그러자 놀라운 일이 벌어졌다. 아래는 시그널을 쪼갠 뒤 "`#`"을 검은색, "`.`"을 흰색으로 표시한 그림이다.

![img](https://upload.acmicpc.net/4a8010ac-92da-4b26-8d97-9c9bce4cf931/-/preview/)

시그널은 디지털 숫자를 나타내고 있었다! 1-3열에 8, 9-11열에 3, 13열에 1, 그리고 16-18열에 7이 나타난 것이다. 이 숫자들이 특별한 의미를 갖고 있을 것이라 생각한 zxcvber는 다른 시그널들도 해독을 하기 시작했다. 하지만 시그널들의 길이가 너무 길어서, 일일히 손으로 확인하기에는 한계가 있었다. 다만, 짧은 시그널들을 분석하면서 zxcvber는 시그널의 규칙들을 파악할 수 있었다.

\1. 시그널은 "`.`"과 "`#`"으로 이루어져 있다.
\2. 시그널을 해독한 결과에는 반드시 숫자가 1개 이상 있다.
\3. 시그널에 등장하는 모든 "`#`"은 올바른 숫자 패턴에 포함되어 있다.
\4. 숫자와 숫자 사이에는 1열 이상의 공백이 있다. 여기서 공백은, 열의 성분이 모두 "`.`"인 열을 의미한다.
\5. 0부터 9는 아래와 같이 나타난다. 역시 "`#`"을 검은색, "`.`"을 흰색으로 표시했다.

![img](https://upload.acmicpc.net/309fd7f3-22b9-452e-95f6-e3f4828c0f9a/-/preview/)

주의할 점은, 1은 다른 숫자들과는 다르게 1열을 차지한다는 것이다. zxcvber를 도와 시그널을 해독해보자!



## 입력

입력의 첫 줄에는 시그널의 길이 *N*(5 ≤ *N* ≤ 100,000, *N*은 5의 배수)이 주어진다.

다음 줄에 시그널이 주어진다. zxcvber가 찾아낸 규칙을 따르는 시그널만이 입력으로 주어진다.



## 출력

첫 번째 줄에 시그널을 해독하여 나오는 숫자들을 순서대로 출력한다.