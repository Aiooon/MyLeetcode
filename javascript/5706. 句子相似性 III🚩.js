/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2) {
    let wordshort = sentence1.split(' '), wordlong = sentence2.split(' ');
    let short = wordshort.length <= wordlong.length ? wordshort.slice() : wordlong.slice();
    let long  = wordshort.length <= wordlong.length ? wordlong.slice() : wordshort.slice();
    for (let i = 0; i < short.length; i++) {
        word = short[i];
        if (long.includes(word)){
            long.splice(long.indexOf(word), 1)
        } else {
            return false;
        }
    }
    let ol = (short.toString() === wordshort.toString()) ? wordlong : wordshort;
    ol = ol.join(' ');
    long = long.join(' ');
    if (ol.indexOf(long) != -1) {
        return true;
    }
    return false;
};

/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar_ = function(sentence1, sentence2) {
    if (sentence1 === sentence2) {
        return true;
    }
    let short = sentence1, long = sentence2;
    if (short.length > long.length) {    // short 中保存较短的那个句子
        let tmp = short;
        short = long;
        long = tmp;
    }
    let words1 = short.split(' '), words2 = long.split(' ');
    while (words1.length > 0) {
        if (! (words1[0] == words2[0] || words1[words1.length - 1] == words2[words2.length - 1])) {
            return false;
        }
        if (words1[0] == words2[0]) {
            words1.shift();
            words2.shift();
        }
        if (words1.length != 0 && words1[words1.length - 1] == words2[words2.length - 1]) {
            words1.pop();
            words2.pop();
        }
    }
    return true;
};



var sentence1 ="CwFfRo regR";
var sentence2 = "CwFfRo H regR";
console.log(areSentencesSimilar_(sentence1, sentence2));
// console.log("A lot of words".indexOf('A lot words'));
