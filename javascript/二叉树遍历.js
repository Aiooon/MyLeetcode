function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

let a = new TreeNode(4), b = new TreeNode(2), c = new TreeNode(6), d = new TreeNode(1), e = new TreeNode(3);
a.left = b;
a.right = c;
b.left = d;
b.right = e;
let root = a;

/* 
       4
      / \
     2   6
    / \
   1   3
*/

// 前序遍历  根 左 右
console.log("preOrder:");
// 递归
var preOrder1 = function (root) {
    let res = [];
    var dfs = function (root) {
        if (root === null) {
            return null;
        }
        res.push(root.val);
        dfs(root.left);
        dfs(root.right);
    }
    dfs(root);
    return res;
}
console.log("递归：" + preOrder1(root));

// 迭代
var preOrder2 = function (root) {
    if (root === null) {
        return 
    }
    let cur = root;
    let res = [], stack = [];
    while (cur !== null || stack.length != 0) {
        if (cur != null) {
            res.push(cur.val);
            stack.push(cur);
            cur = cur.left;
        } else {
            cur = stack.pop();
            cur = cur.right;
        }
    }
    return res;
}
console.log("迭代：" + preOrder2(root));

// 中序遍历  左 根 右
console.log("inOrder:");
// 递归
var inOrder1 = function (root) {
    let res = [];
    var dfs = function (root) {
        if (root === null) {
            return
        }
        dfs(root.left);
        res.push(root.val);
        dfs(root.right);
    }
    dfs(root);
    return res;
}
console.log("递归：" + inOrder1(root));

// 迭代
var inOrder2 = function (root) {
    if (root === null) {
        return 
    }
    let cur = root;
    let res = [], stack = [];
    while (cur !== null || stack.length != 0) {
        if (cur != null) {
            stack.push(cur);
            cur = cur.left;
        } else {
            cur = stack.pop();
            res.push(cur.val);
            cur = cur.right;
        }
    }
    return res;
}
console.log("迭代：" + inOrder2(root));

// 后序遍历  左 右 根
console.log("postOrder:");
// 递归
var postOrder1 = function (root) {
    let res = [];
    var dfs = function (root) {
        if (root === null) {
            return
        }
        dfs(root.left);
        dfs(root.right);
        res.push(root.val);
    }
    dfs(root);
    return res;
}
console.log("递归：" + postOrder1(root));

// 迭代
// 把先序顺序中的 ‘根左右’ 转换为 ‘根右左’，然后反过来就变成了‘左右根’。
var postOrder2 = function (root) {
    if (root === null) {
        return 
    }
    let cur = root;
    let res = [], stack = [];
    while (cur !== null || stack.length != 0) {
        if (cur != null) {
            res.push(cur.val);
            stack.push(cur);
            cur = cur.right;
        } else {
            cur = stack.pop();
            cur = cur.left;
        }
    }
    res.reverse();
    return res;
}
console.log("迭代：" + postOrder2(root));

// 层序遍历
console.log("layerOrder:");
var layerOrder1 = function (root) {
    if (root == null) {
        return 
    }
    let res = [], queue = [];
    queue.push(root);
    while (queue.length != 0) {
        let cur = queue.shift();
        res.push(cur.val);
        if (cur.left != null){
            queue.push(cur.left);
        }
        if (cur.right != null){
            queue.push(cur.right);
        }
    }
    return res;
}
console.log("迭代：" + layerOrder1(root));

// 每层一个数组
var layerOrder2 = function (root) {
    if (root == null) {
        return [];
    }
    let res = [], queue = [];
    queue.push(root);
    while (queue.length != 0) {
        n = queue.length;
        let level = [];
        for (let i = 0; i < n; i++) {
            let cur = queue.shift();
            level.push(cur.val);
            if (cur.left != null){
                queue.push(cur.left);
            }
            if (cur.right != null){
                queue.push(cur.right);
            }
        }
        res.push(level);
    }
    return res;
}
console.log("迭代：", layerOrder2(root));