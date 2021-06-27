/*
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000

date: 2021年6月26日
*/

/* 
Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
} 
*/

/**
 * @param {ListNode} head
 * @return {number[]}
 */
var reversePrint = function(head) {
    if (head == null) {
        return [];
    }
    let ans = new Array();
    let cur = head;
    while(cur != null) {
        ans.unshift(cur.val);
        cur = cur.next;
    }
    return ans;
};