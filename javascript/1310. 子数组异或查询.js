/**
 * @param {number[]} arr
 * @param {number[][]} queries
 * @return {number[]}
 */
var xorQueries = function (arr, queries) {
    /* 思路：
    1. 计算前缀异或数组 xors
    2. 计算每个查询的结果，第 i 个查询的结果为  xors[queries[i][0]] ^ xors[queries[i][1] + 1]
    定义一个前缀异或数组 xors，xors[0] = 0, xors[i+1] = xors[i] ^ arr[i] (0 <= i < n)
    则 xors[i] = arr[0] ^ ... ^ arr[i-1]
    设 queries[0] = left，queries[1] = right，Q(left,right)表示查询结果
    当 left = 0 时，Q(left,right) = xors[right + 1]
    当 left > 0 时，
        Q(left,right)
    = arr[left] ^ ... ^ arr[right]
    = (arr[0] ^ ... ^ arr[left - 1]) ^ (arr[0] ^ ... ^ arr[left - 1]) ^ (arr[left] ^ ... ^ arr[right])
    = (arr[0] ^ ... ^ arr[left - 1]) ^ (arr[0] ^ ... ^ arr[right])
    = xors[left] ^ xors[right + 1]
    */
    const n = arr.length, m = queries.length;
    let xors = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        xors[i + 1] = xors[i] ^ arr[i];
    }
    let ans = new Array(m).fill(0);
    for (let i = 0; i < m; i++) {
        ans[i] = xors[queries[i][0]] ^ xors[queries[i][1] + 1];
    }
    return ans;
};

let arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]];
console.log(xorQueries(arr, queries));