function solution(participant, completion) {
  let answer = '';
  const dict = {}
  participant.forEach(element => {
    if (dict[element])
      dict[element]++;
    else dict[element] = 1;
  });
  completion.forEach(element => dict[element]--);
  Object.keys(dict).forEach((item) => {
    if (dict[item]) answer = item;
  })
  return answer;
}