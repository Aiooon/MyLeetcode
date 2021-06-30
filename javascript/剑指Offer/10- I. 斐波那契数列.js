/* 
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：1

示例 2：
输入：n = 5
输出：5

提示：

0 <= n <= 100 

date: 2021年6月27日
*/
/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n === 0) {
        return 0;
    }
    if (n === 1 || n === 2) {
        return 1;
    }
    let a = 1, b = 1;   // a = fib(1),  b = fib(2)   
    let c = 0;
    while(n > 2) {
        c = (a + b) % 1000000007;
        a = b;
        b = c;
        n--;
    }
    return c;
};

// 0 1 1 2 3 5 8
console.log(fib(100));