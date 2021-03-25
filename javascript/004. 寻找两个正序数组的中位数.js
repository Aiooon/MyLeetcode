/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    const l1 = nums1.length, l2 = nums2.length;
    if (l1 == 0 && l2 == 0){
        return 0;
    }
    if (l1 == 0){
        return (l2 % 2) == 0 ?  (nums2[l2 / 2] + nums2[(l2 / 2)-1]) / 2: nums2[Math.floor(l2 / 2)];
    } else if (l2 == 0) {
        return (l1 % 2) == 0 ?  (nums1[l1 / 2] + nums1[(l1 / 2)-1]) / 2: nums1[Math.floor(l1 / 2)];
    }
    // 总长为偶数 flag 为 true， 奇数为 false
    let flag = ((l1 + l2) % 2) == 0 ? true : false;
    const midlen = flag ? Math.ceil((l1 + l2) / 2) + 1 : Math.ceil((l1 + l2) / 2);
    let mix = [];
    let i = j = 0;
    while (i<l1 && j<l2 && mix.length < midlen) {
        if (nums1[i] <= nums2[j]) {
            mix.push(nums1[i]);
            i++;
        } else {
            mix.push(nums2[j]);
            j++;
        }
    }
    if (i < l1){
        while(mix.length < midlen) {
            mix.push(nums1[i]);
            i++;
        }
    } else if (j < l2) {
        while(mix.length < midlen) {
            mix.push(nums2[j]);
            j++;
        }
    }

    return flag ? (mix[mix.length - 1] + mix[mix.length - 2]) / 2 : mix[mix.length - 1];
};

const nums1 =[1], nums2 = [2,3,4]
console.log(findMedianSortedArrays(nums1, nums2));