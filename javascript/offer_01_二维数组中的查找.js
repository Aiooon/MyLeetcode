/* 题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例1
输入:
7,
[[1,2, 8, 9],
 [2,4, 9,12],
 [4,7,10,13],
 [6,8,11,15]]
返回值:true

date: 2021年3月10日
*/

function Find(target, array) {
    /* 
    思路：
    选择右上角的数作为标志数
    若大于 target，则左移一列，若小于 target，则下移一行
    返回条件：找到 target  /  超出矩阵范围
    */
    const rows = array.length;
    const cols = array[0].length;
    let row = 0;
    let col = cols - 1;
    while (row < rows && col >= 0) {
        if (array[row][col] > target){
            col -= 1;
        } else if (array[row][col] < target){
            row += 1;
        } else if (array[row][col] === target){
            return true;
        }
    }
    return false;
}

array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
console.log(Find(1, array))