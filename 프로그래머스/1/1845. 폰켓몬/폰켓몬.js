function solution(nums) {
  var answer = 0;
  const mons = {};
  nums.forEach(n => {
    mons[n] = 1;
  });
  console.log(mons);

  answer = Math.min(Object.keys(mons).length, nums.length / 2);
  return answer;
}