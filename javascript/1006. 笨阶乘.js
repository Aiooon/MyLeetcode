/* 
1006. 笨阶乘
通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。

例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。

另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。

示例 1：
输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1

示例 2：
输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

提示：

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  （答案保证符合 32 位整数。）

date: 2021年4月1日
*/

/* 思路: 栈
当遇到乘法或除法的时候，将栈顶元素弹出，计算后入栈
当遇到减法，将当前数的相反数入栈
当遇到加法，直接入栈
计算栈内所有元素的和
*/
/**
 * @param {number} N
 * @return {number}
 */
var clumsy = function(N) {
    let stack = [N--];
    let count = 0;
    while (N > 0) {
        if (count % 4 == 0){           // 乘法
            stack.push(stack.pop() * N);
        } else if (count % 4 == 1){    // 除法
            let num1 = stack.pop();
            stack.push(num1 > 0 ? Math.floor(num1 / N): Math.ceil(num1 / N));
        } else if (count % 4 == 2){    // 加法
            stack.push(N);
        } else if (count % 4 == 3){    // 减法
            stack.push(-N);
        }
        count++;
        N--;
    }
    let res = 0;
    /* while(stack.length > 0){
        res += stack.pop();
    } */
    stack.forEach((element) => {
        res += element;
    })
    return res;
};

var clumsy_ = function (N) {
    if (N === 1) {
        return 1;
    } else if (N === 2) {
        return 2;
    } else if (N === 3) {
        return 6;
    } else if (N === 4) {
        return 7;
    }

    if (N % 4 === 0) {
        return N + 1;
    } else if (N % 4 <= 2) {
        return N + 2;
    } else {
        return N - 1;
    }
}

console.log(clumsy_(10));