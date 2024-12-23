function solution(new_id) {
    var answer = ''
    answer = new_id.toLowerCase() // 1단계
    
        .replace(/[^a-z0-9-_.]/g, '') // 2단계
        /*
            [^...] - [^] : 대괄호 안에서 쓰면 제외의 뜻, ex) [^a-z] : 소문자 알파벳을 제외한 모든 문자
                   - 대괄호 안에서 -_. 같은 특수문자는 문자 그대로 해석     
            a-z : 소문자 알파벳 (a부터 z까지)
            0-9 : 숫자(0부터 9까지)
            g : 모든 검색 결과를 반환        
        */
    
        .replace(/\.+/g, '.') // 3단계
        /*
            \. = 문자 그대로 해석
            + = 바로 앞에 요소가 1번 이상 반복
        */
        .replace(/^\.|\.$/g, '') // 4단계
        /*
            ^ : 문자열의 시작
            $ : 문자열의 끝
            | : or 연산
        */
        .replace(/^$/, 'a') // 5단계
        .slice(0, 15).replace(/\.$/, ''); // 6단계
    
    while (answer.length <= 2) answer += answer[answer.length - 1]; // 7단계
    
    return answer
}