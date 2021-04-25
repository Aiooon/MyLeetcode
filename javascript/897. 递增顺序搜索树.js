// date: 2021年4月25日
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
// 首先中序遍历，存结果，然后重新建树（两次遍历）
// 时间O(n) 空间O(n)
var increasingBST = function (root) {
    if (root == null) {
        return ;
    }
    let seq = [];
    let stack = [];
    let cur = root;
    while (cur != null || stack.length != 0) {
        if (cur != null){
            stack .push(cur);
            cur = cur.left;
        } else {
            cur = stack.pop();
            seq.push(cur.val);
            cur = cur.right;
        }
    }
    let newRoot = new TreeNode(seq.shift());
    cur = newRoot;
    while (seq.length > 0){
        cur.right = new TreeNode(seq.shift());
        cur = cur.right;
    }
    return newRoot;
};

// 一次遍历，在遍历过程中修改节点的指向
// 时间O(n) 空间O(n)
var increasingBST = function (root) {
    let dumRoot = new TreeNode(-1);
    let cur = dumRoot;
    const inorder = ((node) => {
        if (node == null){
            return;
        }
        inorder(node.left);
        cur.right = node;
        node.left = null;
        cur = node;
        inorder(node.right);
    });
    inorder(root);
    return dumRoot.right;
};