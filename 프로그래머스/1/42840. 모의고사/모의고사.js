function solution(answers) {
    let answer = [];
    
    let cors = [[1, no1(answers)],[2, no2(answers)],[3, no3(answers)]];
    
    const maxCor = Math.max(...(cors.map(ans => ans[1])));
    
    cors.map(ans => {
        if (ans[1] === maxCor) answer.push(ans[0]);
        return;
    })
    
    
    return answer;
}

function no1(answers) {
    let cnt = 0;
    let pick = [1, 2, 3, 4, 5];
    for (let i=0; i < answers.length; i++) {
        if (pick[i % 5] === answers[i]) cnt++;
    }
    return cnt;
}

function no2(answers) {
    let cnt = 0;
    let pick = [2,1,2,3,2,4,2,5];
    for (let i=0; i < answers.length; i++) {
        if (pick[i % 8] === answers[i]) cnt++;
    }
    return cnt;
}

function no3(answers) {
    let cnt = 0;
    let pick = [3,3,1,1,2,2,4,4,5,5];
    for (let i=0; i < answers.length; i++) {
        if (pick[i % 10] === answers[i]) cnt++;
    }
    return cnt;
}
