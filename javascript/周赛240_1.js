/* 

*/

/**
 * @param {number[][]} logs
 * @return {number}
 */
var maximumPopulation = function(logs) {
    let map = new Map();
    for (let i = 1950; i <= 2050; i++) {
        map.set(i, 0);
    }
    for (let i = 0; i < logs.length; ++i) {
        let b = logs[i][0], d = logs[i][1];
        for (let j = b; j < d; ++j) {
            map.set(j,  map.get(j) + 1);
        }
    }
    let ans = 2051, h = 0;
    for (let [year, count] of map.entries()) {
        if (count > h) {
            h = count;
            ans = year;
        }
    }
    return ans;
};

let logs = [[1950,1961],[1960,1971],[1970,1981]];
console.log(maximumPopulation(logs));