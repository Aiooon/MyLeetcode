/* 
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

提示：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109

date: 2021年4月5日
*/
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
// 反向遍历
var merge = function(nums1, m, nums2, n) {
    let i = m - 1, j = n - 1;
    let tail = m + n - 1;
    let cur = 0;
    while (i >= 0 || j >= 0) {
        if (i === -1) {
            cur = nums2[j--];
        } else if (j === -1) {
            cur = nums1[i--];
        } else if (nums1[i] > nums2[j]) {
            cur = nums1[i--];
        } else {
            cur = nums2[j--];
        }
        nums1[tail--] = cur;
    }
};

let nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3;
merge(nums1, m, nums2, n);
console.log(nums1);