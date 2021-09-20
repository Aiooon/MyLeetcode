
function TreeNode(x) {
  this.val = x;
  this.left = null;
  this.right = null;
}



function preorder(root) {
  let res = [];
  const dfs = (root) => {
    if(!root) {
      return null;
    }
    res.push(root.val);
    dfs(root.left);
    dfs(root.right);
  }
  dfs(root);
  return res;
}

function midorder(root) {
  let res = [];
  const dfs = (root) => {
    if(!root) {
      return null;
    }
    dfs(root.left);
    res.push(root.val);
    dfs(root.right);
  }
  dfs(root);
  return res;
}

function postorder(root) {
  let res = [];
  const dfs = (root) => {
    if(!root) {
      return null;
    }
    dfs(root.left);
    dfs(root.right);
    res.push(root.val);
  }
  dfs(root);
  return res;
}

