/**
 * Initialize your data structure here.
 */
var MyHashMap = function() {
    this.base = 769;
    this.data = new Array(this.base).fill(0).map(() => new Array());
};

MyHashMap.prototype.hash = function (key) {
    return key % this.base;
}

/**
 * value will always be non-negative. 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    const h = this.hash(key);
    for (const m of this.data[h]) {
        if (m[0] === key) {
            m[1] = value;
            return ;
        }
    }
    this.data[h].push([key, value]);
};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    const h = this.hash(key);
    for (const m of this.data[h]) {
        if (m[0] === key) {
            return m[1];
        }
    }
    return -1;
};

/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    const h = this.hash(key);
    for (const m of this.data[h]) {
        if (m[0] === key) {
            let idx = this.data[h].indexOf(m);
            this.data[h].splice(idx, 1);
            return ;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */