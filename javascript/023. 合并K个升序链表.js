/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

printList = function (ListNode){
    let vals = [];
    let tail = ListNode;
    while (tail) {
        vals.push(tail.val);
        tail = tail.next;
    }
    return vals.join('->');
}

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    const k = lists.length;
    if (k == 0) {
        return null;
    }

    let merge_head = new ListNode();
    let tail = merge_head;
    while(true) {
        let min_node = null;
        let min_idx = -1;
        for (let i = 0; i < k; i++) {   // 找到当前值最小的那个头节点
            if (lists[i] == null) continue;
            if (min_node == null || min_node.val > lists[i].val) {
                min_node = lists[i];
                min_idx = i;
            }
        }
        if (min_idx == -1) break;
        tail.next = min_node;
        tail = tail.next;
        lists[min_idx] = lists[min_idx].next;
    }

    return merge_head.next;
};


lists = [[1,4,5],[1,3,4],[2,6]]
head = mergeKLists(lists)
console.log();

