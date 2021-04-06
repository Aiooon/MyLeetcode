/* 
2. 乐团站位
某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。

为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。例如当 num = 5 时，站位如图所示


请返回位于场地坐标 [Xpos,Ypos] 的成员所持乐器编号。

示例 1：

输入：num = 3, Xpos = 0, Ypos = 2

输出：3


示例 2：

输入：num = 4, Xpos = 1, Ypos = 2

输出：5

提示：

1 <= num <= 10^9
0 <= Xpos, Ypos < num
*/
/**
 * @param {number} num
 * @param {number} xPos
 * @param {number} yPos
 * @return {number}
 */
var orchestraLayout = function (num, xPos, yPos) {
    let m = 0;
    let a = 1;
    let arr = new Array(num).fill(0).map(() => new Array(num).fill(0));
    while (m < num / 2) {
        for (let r = m; r < num - m; r++) {
            arr[m][r] = a++;
            if (a == 10) a = 1;
        }
        for (let d = m; d < num - m - 1; d++) {
            arr[d + 1][num - m - 1] = a++;
            if (a == 10) a = 1;
        }
        for (let z = m; z < num - m - 1; z++) {
            arr[num - m - 1][num - 1 - (z + 1)] = a++;
            if (a==10) a = 1;
        }
        for (let u = m; u < num - m - 2; u++) {
            arr[num - (u + 1) - 1][m] = a++;
            if (a==10) a = 1;
        }
        m = m + 1;
    }
    return arr[xPos][yPos];
};

console.log(orchestraLayout(4, 1, 2));