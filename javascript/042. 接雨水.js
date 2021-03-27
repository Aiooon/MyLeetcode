/* 42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105 

date: 2021年3月27日
*/
/**
 * @param {number[]} height
 * @return {number}
 */
// 暴力法  时间 O(N^2) 空间 O(1)
// var trap = function(height) {
//     if (height.length == 0){
//         return 0;
//     }

//     let res = 0;
//     const l = height.length;
//     for (let i = 1; i < l - 1; i++){
//         let left_max = 0, right_max = 0;
//         for (let j = i; j >= 0; j--) {
//             left_max = Math.max(height[j], left_max);
//         }
//         for (let j = i; j < l; j++) {
//             right_max = Math.max(height[j], right_max);
//         }
//         res +=  Math.min(left_max, right_max) - height[i];
//     }

//     return res;
// };

// 备忘录 时间 O(N) 空间 O(N)
// var trap = function(height) {
//     if (height.length == 0){
//         return 0;
//     }

//     let res = 0;
//     const l = height.length;

//     let left_max = new Array(l);
//     let right_max = new Array(l);

//     left_max[0] = height[0];
//     for (let i = 1; i < l; i++) {
//         left_max[i] = Math.max(left_max[i-1], height[i]);
//     }
//     right_max[l - 1] = height[l - 1];
//     for (let i = l-2; i > 0; i--) {
//         right_max[i] = Math.max(right_max[i+1], height[i]);
//     }

//     for (let i = 1; i < l; i++) {
//         res += Math.min(left_max[i], right_max[i]) - height[i];
//     }

//     return res;
// };

// 双指针法
var trap = function(height) {
    if (height.length == 0){
        return 0;
    }
    let res = 0;
    const n = height.length;
    let left = 0, left_max = height[0];
    let right = n-1, right_max = height[n-1];

    while (left <= right){
        left_max = Math.max(left_max, height[left]);
        right_max = Math.max(right_max, height[right]);

        if (left_max < right_max) {
            res += left_max - height[left];
            left++;
        } else {
            res += right_max - height[right];
            right--;
        }
    }
    return res;
};


height = [0,1,0,2,1,0,1,3,2,1,2,1]
console.log(trap(height))