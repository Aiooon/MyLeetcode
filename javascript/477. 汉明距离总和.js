/**
 * @param {number[]} nums
 * @return {number}
 */
var totalHammingDistance = function (nums) {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i <= 30; i++) {
        let c = 0;
        for (num of nums) {
            if ((num >> i) & 1) {
                c++;
            } 
        }
        ans += c * (n - c);
    }
    return ans;
};

let nums = [4, 14, 2];
console.log(totalHammingDistance(nums));