var MaxQueue = function() {
  this.que1 = [];
  this.que2 = [];
};

/**
 * @return {number}
 */
MaxQueue.prototype.max_value = function() {
  return this.que2.length === 0 ? -1 : this.que2[0];
};

/** 
 * @param {number} value
 * @return {void}
 */
MaxQueue.prototype.push_back = function(value) {
  this.que1.push(value);
  while (this.que2.length !== 0 && this.que2[this.que2.length - 1] < value) {
    this.que2.pop();
  }
  this.que2.push(value);
};

/**
 * @return {number}
 */
MaxQueue.prototype.pop_front = function() {
  if (this.que1.length === 0) {
    return -1;
  }
  const p = this.que1.shift();
  if (p === this.que2[0]) {
    this.que2.shift();
  }
  return p;
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * var obj = new MaxQueue()
 * var param_1 = obj.max_value()
 * obj.push_back(value)
 * var param_3 = obj.pop_front()
 */