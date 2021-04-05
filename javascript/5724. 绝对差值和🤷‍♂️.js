/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minAbsoluteSumDiff = function(nums1, nums2) {
    let flag = true;
    for (let i = 0; i < nums1.length; i++) {
        if (nums1[i] != nums2[i]) flag = false;
    }
    if (flag) return 0;

    let max = 0, idx = -1;
    for (let i = 0; i < nums1.length; i++){     // 找到差值最大的那一对数
        let a = Math.abs(nums1[i] - nums2[i]);
        if (a > max) {
            max = a;
            idx = i;
        }
    }
    // 找到一个数替换 nums1[idx]
    let min = max, min_idx = -1;
    for (let i = 0; i < nums1.length; i++){
        if (Math.abs(nums1[i] - nums2[idx]) < min) {
            min = Math.abs(nums1[i] - nums2[idx]);
            min_idx = i;
        }
    }
    if (idx != min_idx) {
        nums1[idx] = nums1[min_idx];
    }
    let res = 0;
    for (let i = 0; i < nums1.length; i++){
        res += Math.abs(nums1[i] - nums2[i]);
        res = res % 1000000007
    }
    return res;
};

let nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4];
console.log(minAbsoluteSumDiff(nums1, nums2));