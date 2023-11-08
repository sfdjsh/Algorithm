function solution(nums) {
    var answer = 0;
    
    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                let num = nums[i] + nums[j] + nums[k];
                
                flag = true;
                for (let n = 2; n < parseInt(num**(1/2)) + 1; n++) {
                    if (num % n == 0) {
                        flag = false;
                        break
                    }
                }
                
                if (flag) {
                    answer++;
                }
            }
        }
    }
    
    
    return answer;
}