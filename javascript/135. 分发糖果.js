/*
135. 分发糖果
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1：

输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2：

输入：[1,2,2]
输出：4
解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

date: 2021年6月1日
*/

/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
    /* 思路：
    首先全部初始化为 1，然后两次遍历：
    第一次 从左到右遍历，若右边的评分比左边高，则右边的糖果数更新为左边的+1
    第二次 从右到左遍历，若左边的评分比右边高，且左边糖果数不大于右边的，则左边的糖果数更新为右边的+1
    */
    const n = ratings.length;
    if (n <= 1) {
        return n;
    }
    let num = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            num[i] = num[i - 1] + 1;
        }
    }
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1] && num[i] <= num[i + 1]) {
            num[i] = num[i + 1] + 1;
        }
    }
    let ans = 0;
    for (let c of num) {
        ans += c;
    }
    return ans;
};

let ratings = [1,0,2];
console.log(candy(ratings));