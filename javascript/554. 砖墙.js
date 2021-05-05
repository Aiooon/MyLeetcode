/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function (wall) {
    const count = new Map();
    for (const wids of wall) {
        const n = wids.length;
        let sum = 0;
        for (let i = 0; i < n - 1; i++) {
            sum += wids[i];
            count.set(sum, (count.get(sum) || 0) + 1);
        }
    }
    let max = 0;
    for (const [_, c] of count.entries()) {
        max = Math.max(max, c);
    }
    return wall.length - max;
};