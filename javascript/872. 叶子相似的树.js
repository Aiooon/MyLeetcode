
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function (root1, root2) {

    let leaves1 = [], leaves2 = [];
    var dfs = function (root, leaves) {
        if (root.left == null && root.right == null) {
            leaves.push(root.val);
        } else {
            if(root.left) {
                dfs(root.left, leaves)
            }
            if(root.right) {
                dfs(root.right, leaves)
            }
        }
    }
    dfs(root1, leaves1);
    dfs(root2, leaves2); 
    return leaves1.toString() === leaves2.toString();
};

let nums1 = [1,2], nums2 = [1,2];
console.log(nums1.toString() === nums2.toString());