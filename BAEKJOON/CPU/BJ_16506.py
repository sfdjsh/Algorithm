cpu = {'ADD': 0, 'ADDC': 1, 'SUB': 2, 'SUBC': 3, 'MOV': 4, 'MOVC': 5, 'AND': 6, 'ANDC': 7, 'OR': 8, 'ORC': 9,
       'NOT': 10, 'MULT': 12, 'MULTC': 13, 'LSFTL': 14, 'LSFTLC': 15, 'LSFTR': 16, 'LSFTRC': 17, 'ASFTR': 18,
       'ASFTRC': 19, 'RL': 20, 'RLC': 21, 'RR': 22, 'RRC': 23}

N = int(input())
for _ in range(N):
    result = ''

    opcode, rD, rA, rBC = input().split()

    result += bin(cpu[opcode])[2:].zfill(5) + '0'
    result += bin(int(rD))[2:].zfill(3)
    result += bin(int(rA))[2:].zfill(3)

    if cpu[opcode] % 2 == 0:
        result += bin(int(rBC))[2:].zfill(3) + '0'
    else:
        result += bin(int(rBC))[2:].zfill(4)

    print(result)

