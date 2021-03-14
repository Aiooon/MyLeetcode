/**
 * Initialize your data structure here.
 */
var MyHashSet = function() {
    this.base = 769;
    this.data = new Array(this.base).fill(0).map(() => new Array());
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
    const h = this.hash(key);
    for (const num of this.data[h]) {
        if (num === key) return;
    }
    this.data[h].push(key);
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
    const h = this.hash(key);
    const chain = this.data[h];
    for (let i = 0; i < chain.length; i++) {
        if (chain[i] === key){
            chain.splice(i, 1);
            return;
        }
    }
};

/**
 * Returns true if this set contains the specified element 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
    const h = this.hash(key);
    for (const num of this.data[h]) {
        if (num === key) return true;
    }
    return false;
};

MyHashSet.prototype.hash = function (key) {
    return key % this.base;
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */



// test
var data = new Array(5).fill(0).map(() => new Array());
console.log(data);