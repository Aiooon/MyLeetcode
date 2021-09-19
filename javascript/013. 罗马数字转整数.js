/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let syb2val = new Map();
    syb2val.set('I', 1);
    syb2val.set('V', 5);
    syb2val.set('X', 10);
    syb2val.set('L', 50);
    syb2val.set('C', 100);
    syb2val.set('D', 500);
    syb2val.set('M', 1000);
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const val = syb2val.get(s[i]);
        if (i < n - 1 && val < syb2val.get(s[i+1])) {
            ans -= val;
        } else {
            ans += val;
        }
    }
    return ans;
};

console.log(romanToInt('LVIII'));