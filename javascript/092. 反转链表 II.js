/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    const dum_head = new ListNode();
    dum_head.next = head;
    let pre = dum_head;

    for (let i = 0; i < left - 1; i++) {
        pre = pre.next;
    }

    let cur = pre.next;
    for (let i = 0; i < right - left; i++) {
        const next_n = cur.next;
        cur.next = next_n.next;
        next_n.next = pre.next;
        pre.next = next_n;
    }

    return dum_head.next;
};