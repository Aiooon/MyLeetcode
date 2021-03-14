/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}


/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function (root) {
    if (!root) {
        return '[]'
    }
    let que = [];
    let res = [];
    que.push(root);
    while (que.length != 0){
        let node = que.shift();
        if (node) {
            res.push(node.val + "");    // 数字转字符串
            que.push(node.left);
            que.push(node.right);
        } else {
            res.push('null');
        }
    }
    return '[' + res.join(',') + ']'    // 注意join的用法和 python 不同
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
    if (data === '[]') {
        return null;
    }
    let vals = data.slice(1, data.length-1).split(',');
    let i = 1;
    let que = [];
    let root = new TreeNode(+vals[0]);  // 字符串转数字
    que.push(root);
    while (que.length > 0) {
        let node = que.shift();
        if (vals[i] !== 'null') {
            node.left = new TreeNode(+vals[i]);
            que.push(node.left);
        }
        i++;
        if (vals[i] !== 'null') {
            node.right = new TreeNode(+vals[i]);
            que.push(node.right);
        }
        i++;
    }
    return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */


let data = "[1,2,3,null,null,4,5,null,null,null,null]"
console.log(deserialize(data))