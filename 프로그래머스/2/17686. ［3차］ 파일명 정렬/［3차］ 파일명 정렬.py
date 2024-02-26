def solution(files):
    answer = []
    file_lst = []
    
    for file in files:
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break
        
        for i in range(len(number)):
            if not number[i].isdigit():
                tail = number[i:]
                number = number[:i]
                break
        
        file_lst.append([head, number, tail])
    
    file_lst.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for f in file_lst:
        answer.append(''.join(f))
                
    return answer