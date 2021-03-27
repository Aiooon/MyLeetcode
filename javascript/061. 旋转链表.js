/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function (head, k) {
    if (k === 0) {
        return head
    }
    // 判断空链表
    if (!head || !head.next) {
        return head
    }
    //  遍历一次，获取链表长度
    let len = 0;
    let cur = head;
    while (cur) {
        len++;
        cur = cur.next;
    }

    let tail = len - (k % len) - 1;     // tail 表示旋转后最后一个节点在原链表中的位置
    if (tail == len - 1) return head;
    let tail_node = head
    while (tail > 0) {  // 找到 tail 节点
        tail_node = tail_node.next;
        tail--;
    }
    let new_head = tail_node.next;
    cur = new_head;
    while (cur.next) {
        cur = cur.next;
    }
    cur.next = head;
    tail_node.next = null;
    return new_head;
};



var creatList = function (nums) {
    let head = new ListNode(0, null);
    let cur = head;
    for (let i = 0; i < nums.length; i++) {
        let node = new ListNode(nums[i]);
        cur.next = node;
        cur = cur.next;
    }
    return head.next;
}

var printList = function (head) {
    let nums = [];
    let cur = head;
    while (cur) {
        nums.push(cur.val);
        cur = cur.next;
    }
    return nums.join('->');
}


const nums = [1, 2, 3, 4, 5, 6, 7];
head = creatList(nums)
console.log(printList(head));
let new_head = rotateRight(head, 4);
console.log(printList(new_head));
