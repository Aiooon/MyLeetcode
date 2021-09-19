function getLinkNodeIdList(nodeList) {
  // write code here
  let path = [];
  const dfs = (node, path) => {
    if (!node || node.length === 1) {
      return;
    }
    path.push(node[0]);
    const l = node.length;
    for (let i = 1; i < l; i++) {
      
    }
  }
  dfs(nodeList[0], path);
  return path;
}

const nodeList = [[1, 2, 3], [2, 4], [3], [4]];
const output = [1, 2, 4];
