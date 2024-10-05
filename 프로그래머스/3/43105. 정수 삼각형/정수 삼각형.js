function solution(triangle) {
  return triangle.reduceRight((r, a) => a.map((v, i) => v + Math.max(r[i], r[i+1])))[0]
}