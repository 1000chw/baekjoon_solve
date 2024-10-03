function solution(clothes) {
  let answer = 0;
  const map = new Map();

  clothes.forEach(clothe => {
    map.set(clothe[1], [...(map.get(clothe[1]) || []), clothe[0]]);
  })

  const nums = [];

  Array.from(map.values()).forEach((value) => {
    nums.push(value.length);
  })

  answer = fashion(nums, 0) - 1;

  return answer;
}

function fashion(nums, idx) {
  if (idx === nums.length) {
    return 1;
  }
  const res = fashion(nums, idx + 1);
  return res * (nums[idx] + 1);
}