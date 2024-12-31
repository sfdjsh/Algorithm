function solution(numbers) {
    const number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    return number_list.filter((val) => !numbers.includes(val)).reduce((acc, val) => acc + val, 0)
}