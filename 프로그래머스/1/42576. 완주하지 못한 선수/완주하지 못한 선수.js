function solution(participant, completion) {
  let answer = '';
  const dict = {}
  participant.forEach(element => {
    dict[element] = (dict[element] || 0) + 1;
  });
  completion.forEach(element => dict[element]--);
  Object.keys(dict).forEach((item) => {
    if (dict[item]) answer = item;
  })
  return answer;
}