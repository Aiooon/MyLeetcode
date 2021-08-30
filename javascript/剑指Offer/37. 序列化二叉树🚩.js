
// Definition for a binary tree node.
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
  return _serialize(root, '')
};

const _serialize = (root, str) => {
  if (!root) {
    str += 'Null,';
  } else {
    str += root.val + '' + ',';
    str = _serialize(root.left, str);
    str = _serialize(root.right, str);
  }
  return str;
};


/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
  const dataArr = data.split(',');
  return _deserialize(dataArr);
};

const _deserialize = (dataArr) => {
  if (dataArr[0] === 'Null') {
    dataArr.shift();
    return null;
  }

  const root = new TreeNode(parseInt(dataArr[0]));
  dataArr.shift();
  root.left = _deserialize(dataArr);
  root.right = _deserialize(dataArr);
  return root;
}



/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

