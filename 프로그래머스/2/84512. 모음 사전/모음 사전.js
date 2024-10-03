function solution(word) {
  let answer = 0;
  const gather = ['A', 'E', 'I', 'O', 'U'];
  const dict = [];
  makeDict(gather, dict, '', 0);
  answer = dict.indexOf(word) + 1;
  return answer;
}

function makeDict(gather, dict, curWord, length) {
  if (length === 5) return;
  for (let i = 0; i < 5; i++) {
    const newWord = curWord + gather[i];
    dict.push(newWord);
    makeDict(gather, dict, newWord, length+1);
  }
}