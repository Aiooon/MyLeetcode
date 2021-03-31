/* 
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 
提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

date: 2021年3月31日
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
/* 思路
以 candidates = [2,3,6,7], target = 7 为例：
初始化：res = [], path = []
1. candidates 排序，反向遍历
2. 选择 7，path = [7]，remain = 7 - 7 = 0，当前 path 加入 res
3. 选择 6，path = [6]，remain = 7 - 6 = 1，在 [2,3,6] 中查找 <=1 的数
    无法找到，path.pop() 弹出 6
4. 选择 3，path = [3]，remain = 7 - 3 = 4，在 [2,3] 中查找 <=4 的数
    4.1 选择 3，path = [3,3]，remain = 4 - 4 = 1，在 [2,3] 中查找 <=1 的数
        无法找到，path.pop() 弹出 3
    4.2 选择 2，path = [3,2]，remain = 4 - 2 = 2，在 [2] 中查找 <=2 的数
        4.2.1 选择 2，path = [3,2,2]，remain = 2 - 2 = 0，当前 path 加入 res
5. 选择 2，path = [2]，remain = 7 - 2 = 5，在 [2] 中查找 <=5 的数
    无法找到，path.pop() 弹出 2
6. 遍历结束，返回 res

*/
var combinationSum = function(candidates, target) {
    candidates.sort((a,b) => a-b);
    let res = [], path = [];

    var backtrack = function (path, candidates, end, remain) {
        if (remain == 0) {
            res.push(path.slice());
        }
        for (let i = end; i >= 0; i--) {
            if (candidates[i] <= remain){
                path.push(candidates[i]);
                backtrack(path, candidates, i, remain-candidates[i]);
                path.pop();
            }
        }
    }
    backtrack(path, candidates, candidates.length-1, target);
    return res;
};

let candidates = [2,3,6,7], target = 7;
console.log(combinationSum(candidates, target));