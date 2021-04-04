/**
 * @param {number[][]} logs
 * @param {number} k
 * @return {number[]}
 */
var findingUsersActiveMinutes = function (logs, k) {
    let map = new Map();    // map 记录每个用户操作的分钟数
    for (let i = 0; i < logs.length; i++) {
        let id = logs[i][0], time = logs[i][1];
        if (map.has(id)) {
            let ops = map.get(id);
            if (!(ops.includes(time))) {
                ops.push(time)
                map.set(id, ops.slice());
            }
        } else {
            map.set(id, [time]);
        }
    }
    let ans = new Array(k).fill(0);
    map.forEach((val) => {
        ans[val.length - 1]++;
    })
    return ans;
};

let logs = [[1,1],[2,2],[2,3]], k = 4;
console.log(findingUsersActiveMinutes(logs, k));