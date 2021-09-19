function findWhetherExistsPath( n ,  graph ,  start ,  end ) {
  // write code here
  graph.sort((a, b) => a[0] - b[0]);
  const g = [];
  for (let i = 0; i < n; i++) {
    g.push(graph.filter((e) => e[0] === i));
  }
  const node_s = g[start];
  let dfs = (node, end) => {
    if (!node || node.length === 0) {
      return false;
    }
    const len = node.length;
    for (let i = 0; i < len; i++) {
      if (node[i][1] === end) {
        return true;
      } else {
        return dfs(g[node[i][1]], end);
      }
    }
  }
  return dfs(node_s, end);
}

const graph = [[0, 1], [0, 2], [1, 2], [1, 2]];
console.log(findWhetherExistsPath(3, graph, 0, 2));