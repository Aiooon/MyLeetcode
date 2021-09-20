function layerOrder(root) {
  if (!root) {
    return [];
  }
  let res = [];
  let queue = [root];
  while (queue.length !== 0) {
    let layer = [];
    let n = queue.length;
    while (n > 0) {
      n--;
      let node = queue.shift();
      layer.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    res.push(layer);
  }
  return res;
}