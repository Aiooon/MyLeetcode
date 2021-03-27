/**
 * 
 *  
 * */

// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let dum_head = new ListNode(-1, head);
    let cur = dum_head.next;
    while (cur){
        let next_n = cur.next;
        if (!next_n) break;
        if (cur.val == next_n.val){
            while(next_n && cur.val == next_n.val) {
                next_n = next_n.next;
            }
            cur.next = next_n;
        } else {
            cur = cur.next;
        }
    }
    return dum_head.next;
};