def solution(msg):
    answer = []

    eng = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
           'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
           'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    def check_eng(cnt, tmp, max_num):
        while msg:
            if tmp in eng:
                cnt = eng[tmp]
                msg.pop(0)
                
                if msg:
                    tmp += msg[0]
                else:
                    break

            else:
                eng[tmp] = max_num
                break

        return cnt

    max_num = 27
    msg = list(msg)

    while msg:
        cnt, tmp = 0, msg[0]
        output = check_eng(cnt, tmp, max_num)
        max_num += 1
        answer.append(output)

    return answer