/* 
781. 森林中的兔子
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。

返回森林中兔子的最少数量。

示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0
说明:

answers 的长度最大为1000。
answers[i] 是在 [0, 999] 范围内的整数。

date: 2021年4月4日
*/

/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function (answers) {
    if (answers.length == 0) {
        return 0;
    }
    // 用 map 记录每个数字出现的次数
    let res = 0;
    let map = new Map();
    for (let i = 0; i < answers.length; i++) {
        let num = answers[i]
        if (map.has(num)) {
            map.set(num, map.get(num) + 1);
        } else {
            map.set(num, 1);
        }
    }
    map.forEach((val, key) => {
        if (key == 0) {
            res += val;
        } else {
            if (val % (key + 1) == 0) {
                res += Math.floor(val / (key + 1)) * (key + 1);
            } else {
                res += (Math.floor(val / (key + 1)) + 1) * (key + 1)
            }
        }
    })
    return res;
};

var answers = [2,1,2,2,2,2,2,2,1,1];
console.log(numRabbits(answers));