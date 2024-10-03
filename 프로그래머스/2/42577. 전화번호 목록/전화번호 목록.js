function solution(phone_book) {
  let answer = true;
  const map = new Map();
  phone_book.forEach(phone => {
    let cur = map;
    for (let i = 0; i < phone.length; i++) {
      const p = phone.at(i);
      if (cur.get(p) === 1) {
        answer = false;
        break;
      }
      if (i === phone.length - 1) {
        if (cur.get(p)) {
          answer = false;
        }
        cur.set(p, 1);
      }
      else if (cur.get(p)) cur = cur.get(p);
      else {
        cur.set(p, new Map());
        cur = cur.get(p);
      }
    }

  })
  return answer;
}