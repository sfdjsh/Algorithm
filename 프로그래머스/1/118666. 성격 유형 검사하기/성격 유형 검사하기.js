function solution(survey, choices) {
    var answer = '';
    const personality = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'];        // 성격 유형
    const personality_score = [0, 0, 0, 0, 0, 0, 0, 0];                  // 유형 별 점수
    const score = [3, 2, 1, 0, 1, 2, 3];                                 // 질문에 따른 점수 배치
  
    for (let i = 0; i < survey.length; i++) {
        const [sur1, sur2] = survey[i].split('');
        let idx = 0;
        if (choices[i] >= 5) idx = personality.indexOf(sur2);   // 5 이상(약간 동의)부터 다음 유형에 점수를 줘야하므로 조건 처리
        else idx = personality.indexOf(sur1);
        personality_score[idx] += score[choices[i] - 1];
    }
    
    for (let i = 0; i < personality_score.length; i += 2) {
        if (personality_score[i] >= personality_score[i + 1]) answer += personality[i];
        else answer += personality[i + 1];
    }
    
    return answer;
}