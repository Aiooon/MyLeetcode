

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
    let m = haystack.length, n = needle.length;
    if (n === 0) {
        return 0;
    }
    if (m < n) {
        return -1;
    }
    for (let i = 0; i < m; i++) {
        let cur = haystack.slice(i, i + n);
        if (cur === needle) {
            return i;
        }
    }
    return -1;
};

let haystack = "hello", needle = "ll";
console.log(strStr(haystack, needle));