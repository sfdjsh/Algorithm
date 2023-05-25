from itertools import combinations

answer = 0

N = int(input())
lose_hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

idx_lst = [i for i in range(N)]             # N만큼 인덱스 배열 생성
comb = list()
for i in range(1, N + 1):                   # 조합 생성
    comb += combinations(idx_lst, i)

for i in comb:
    hp_cnt = 0      # 체력 변수
    happy_cnt = 0   # 기쁨 변수
    for j in i:
        hp_cnt += lose_hp[j]
        happy_cnt += happy[j]
    if hp_cnt < 100 and happy_cnt > answer:     # 체력이 100 미만이고 기쁨 변수가 최대값일 때
        answer = happy_cnt

print(answer)