/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.staA = [];
  this.staB = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
  this.staA.push(x);
  if (this.staB.length === 0 || x <= this.staB[this.staB.length - 1]) {
    this.staB.push(x);
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  let p = this.staA.pop();
  if (p === this.staB[this.staB.length - 1]) {
    this.staB.pop();
  }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.staA[this.staA.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.min = function() {
  return this.staB[this.staB.length - 1]
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.min()
 */