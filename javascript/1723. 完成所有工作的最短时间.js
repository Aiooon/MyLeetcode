/**
 * @param {number[]} jobs
 * @param {number} k
 * @return {number}
 */
var minimumTimeRequired = function (jobs, k) {
    /* 
    思路：回溯 + 剪枝
    尽可能平均地将 jobs 分为 k 份
     */
    if (jobs.length === k){
        return Math.max(...jobs);
    }
    const n = jobs.length;
    let ans = Number.MAX_VALUE;
    let sum = new Array(k).fill(0);
    /**
     * @param {number} u       当前处理到哪个 job
     * @param {number} used    当前已经给多少个工人分配工作
     * @param {number []} sum  sum[i] = j 表示第 i 个工人的工作时间为 j
     * @param {number} max     当前的最大工作时间
     */
    var dfs = function (u, used, sum, max) {
        if (max > ans)  return ;
        if (u === n) {
            ans = max;
            return ;
        }
        // 当还有空闲的工人时，优先分配给空闲的工人
        if (used < k) {
            sum[used] = jobs[u];
            dfs(u + 1, used + 1, sum, Math.max(sum[used], max));
            sum[used] = 0;
        }
        for (let i = 0; i < used; i++) {
            sum[i] += jobs[u];
            dfs(u + 1, used, sum, Math.max(sum[i], max));
            sum[i] -= jobs[u];
        }
    }

    dfs(0, 0, sum, 0);
    return ans;
};