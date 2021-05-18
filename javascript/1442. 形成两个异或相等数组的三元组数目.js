/**
 * @param {number[]} arr
 * @return {number}
 */
var countTriplets = function (arr) {
    const n = arr.length;
    let s = new Array(n-1);
    s[0] = 0;
    for (let i = 0; i < n; i++) {
        s[i + 1] = arr[i] ^ s[i];
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let k = i + 1; k < n; k++) {
            if (s[i] === s[k+1]) {
                ans += k - i;
            }
        }
    }

    return ans;
};