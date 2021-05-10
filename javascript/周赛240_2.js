/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDistance = function (nums1, nums2) {
    const m = nums1.length, n = nums2.length;
    let ans = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = i; j < n; ++j) {
            if (nums1[i] <= nums2[j]) {
                ans = Math.max(ans, j - i);
            } else {
                break;
            }
        }
    }
    return ans;
};

let nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5];
console.log(maxDistance(nums1, nums2));