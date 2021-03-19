/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function(big, medium, small) {
    this.park = [0, big, medium, small];
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    if (this.park[carType] > 0) {
        this.park[carType]--;
        return true;
    }
    return false;
    // if (carType == 1) {
    //     if (this.park[0] > 0){
    //         this.park[0]--;
    //         return true;
    //     }
    // } else if (carType == 2) {
    //     if (this.park[1] > 0){
    //         this.park[1]--;
    //         return true;
    //     }
    // } else if (carType == 3) {
    //     if (this.park[2] > 0){
    //         this.park[2]--;
    //         return true;
    //     }
    // }
    // return false;
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */