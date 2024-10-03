function solution(sizes) {
    let left = 0;
    let right = 0;
    for (let i = 0; i < sizes.length; i++) {
        left = Math.max(left, Math.max(...sizes[i]));
        right = Math.max(right, Math.min(...sizes[i]));
    }
    return left * right;
}