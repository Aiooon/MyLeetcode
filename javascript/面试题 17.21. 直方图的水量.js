/**
 * @param {number[]} height
 * @return {number}
 */
// 接雨水 date: 2021年4月2日

// 备忘录
var trap = function(height) {
    const n = height.length;
    if (n == 0) {
        return 0;
    }
    let res = 0;
    let max_left = new Array(n);
    let max_right = new Array(n);
    max_left[0] = height[0];
    max_right[n - 1] = height[n - 1];
    for (let i = 1; i < n; i++) {
        max_left[i] = Math.max(max_left[i-1], height[i]);
    }
    for (let i = n-2; i >= 0; i--) {
        max_right[i] = Math.max(max_right[i+1], height[i]);
    }
    for (let i = 0; i < n; i++) {
        res += Math.min(max_left[i], max_right[i]) - height[i];
    }
    return res;
};

// 双指针
var trap_ = function (height) {
    const n = height.length;
    if (n == 0) {
        return 0;
    }
    let res = 0;
    let left = 0, right = n - 1;
    let max_left = height[left], max_right = height[right];
    while (left <= right) {
        max_left = Math.max(max_left, height[left]);
        max_right = Math.max(max_right, height[right]);

        if (max_left < max_right) {
            res += max_left - height[left];
            left++;
        } else {
            res += max_right - height[right];
            right--;
        }
    }
    return res;
}

height = [0,1,0,2,1,0,1,3,2,1,2,1]
console.log(trap_(height));