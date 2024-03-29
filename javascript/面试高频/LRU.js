

var LRUCache = function (capacity) {
  this.capacity = capacity;
  this.map = new Map();
}

LRUCache.prototype.get = function (key) {
  if (this.map.has(key)){
    let tmp = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, tmp);
    return tmp;
  } else {
    return -1;
  }
}


LRUCache.prototype.put = function (key, val) {
  if (this.map.has(key)) {
    this.map.delete(key);
  }
  this.map.set(key, val);
  if(this.map.size > this.capacity) {
    this.map.delete(this.map.keys().next().value);
  }
}

