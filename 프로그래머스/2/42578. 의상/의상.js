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

  if (nums.length === 1) return nums[0];
  answer = fashion(nums, 0, 0);

  return answer[0] + answer[1];
}

function fashion(nums, idx) {
  if (idx === nums.length - 1) {
    return [0,  nums[idx]];
  }
  const res = fashion(nums, idx + 1);
  return [res[0] + res[1], (res[0] + 1 + res[1]) * nums[idx]];
}