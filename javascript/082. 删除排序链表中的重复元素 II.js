/* 82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

date: 2021年3月25日
*/


/**
 * Definition for singly-linked list.
 *  */
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
    let pre = dum_head;
    while (pre){
        let cur = pre.next;
        if (!cur) break;
        let next_n = cur.next;  // 找到删除当前所有重复节点后的下一个节点
        if (next_n && next_n.val == cur.val) {
            while (next_n && next_n.val == cur.val){
                next_n = next_n.next;
            }
            pre.next = next_n;
        } else {
            pre = pre.next;
        }
    }
    return dum_head;
};