
//Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
/* 
思路：
层序遍历，在同一层且不同父节点，则为堂兄弟节点
在深度优先搜索的递归函数中增加表示「深度」以及「父节点」的两个参数
*/
var isCousins = function (root, x, y) {
    if (root == null) {
        return false;
    }
    let x_parent = null, x_depth = null, x_found = false;
    let y_parent = null, y_depth = null, y_found = false;

    var dfs = function (node, parent, depth) {
        if (node == null) {
            return ;
        }
        if (node.val === x) {
            [x_parent, x_depth, x_found] = [parent, depth, true];            
        } else if (node.val === y) {
            [y_parent, y_depth, y_found] = [parent, depth, true];            
        }
        if (x_found && y_found) {
            return ;
        }
        dfs(node.left, node, depth + 1);
        if (x_found && y_found) {
            return ;
        }
        dfs(node.right, node, depth + 1);
    }

    dfs(root, null, 0);
    return x_depth == y_depth && x_parent !== y_parent;
}

let [a,b,c] = [1,new Array(2),3];
console.log(a);
console.log(b);
console.log(c);