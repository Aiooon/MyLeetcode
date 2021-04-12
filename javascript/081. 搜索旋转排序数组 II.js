/* date: 2021年4月7日 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    let left = 0, right = nums.length - 1;

    // 将数组尾部与 nums[0] 相同的项删除，回复二段性
    while (left < right && nums[0] == nums[right]) right--;

    let len = right
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (nums[mid] == target) {
            return true;
        }
        // 左半边有序
        if (nums[0] <= nums[mid]) {
            if (nums[0] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {    // 右半边有序
            if (nums[mid] < target && target <= nums[len]){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return false;
};

let nums = [2,2,0,1,1,2], target = 2;
console.log(search(nums, target));