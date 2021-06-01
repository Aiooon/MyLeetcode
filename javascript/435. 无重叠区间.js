/*
435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

date: 2021年6月1日
*/

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
    /* 思路：
    在选择要保留区间时，区间的结尾十分重要：选择的区间结尾越小，余留给其它区间的空间就越大，就越能保留更多的区间。
    因此，我们采取的贪心策略为，优先保留结尾小且不相交的区间。
    首先将数组按右边界的大小升序排列，每次选择结尾最小且和前一个选择的区间不重叠的区间。
     */
    intervals.sort((a, b) => a[1] - b[1]);
    const n = intervals.length;
    // let range = [intervals[0]];
    // for (let i = 1; i < n; i++) {
    //     if (intervals[i][0] >= range[range.length - 1][1]) {
    //         range.push(intervals[i]);
    //     }
    // }
    // return n - range.length;
    let ans = 0, pre = intervals[0][1];
    for (let i = 1; i < n; i++) {
        if (intervals[i][0] < pre) {
            ans++;
        } else {
            pre = intervals[i][1];
        }
    }
    return ans;
};

let intervals = [[1, 2], [2, 3]];
console.log(eraseOverlapIntervals(intervals));