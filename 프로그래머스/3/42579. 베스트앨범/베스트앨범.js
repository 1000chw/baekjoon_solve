function solution(genres, plays) {
  var answer = [];

  const map = new Map();
  const sumPlays = new Map();

  for (let i = 0; i < genres.length; i++) {
    sumPlays.set(genres[i], (sumPlays.get(genres[i]) || 0) + plays[i]);
    if (map.has(genres[i])) {
      const curPlays = map.get(genres[i]);
      if (curPlays.length === 1) {
        curPlays.push([plays[i], i]);
        curPlays.sort((a, b) => b[0] - a[0]);
      }
      else {
        if (curPlays[0][0] < plays[i]) {
          curPlays[1] = [...curPlays[0]];
          curPlays[0] = [plays[i], i];
        }
        else if (curPlays[1][0] < plays[i]) {
          curPlays[1] = [plays[i], i];
        }
      }
    }
    else {
      map.set(genres[i], [[plays[i], i]]);
    }
  }

  const sps = [...sumPlays.keys()];
  sps.sort((a, b) => sumPlays.get(b) - sumPlays.get(a));

  sps.forEach(s => {
    map.get(s).forEach(p => answer.push(p[1]));
  });

  return answer;
}