/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
  let p1 = l1, p2 = l2;
  let newhead = new ListNode();
  let cur = newhead;
  while (p1 !== null && p2 !== null) {
    if (p1.val <= p2.val) {
      cur.next = p1;
      p1 = p1.next;
    } else {
      cur.next = p2;
      p2 = p2.next;
    }
    cur = cur.next;
  }
  if (p1 !== null) {
    cur.next = p1;
  } else {
    cur.next = p2;
  }
  return newhead.next;
};