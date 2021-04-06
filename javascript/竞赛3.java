import java.util.PriorityQueue;

class Solution {
    public int magicTower(int[] nums) {
        int sum = 1;
        for(int i = 0 ; i < nums.length ; i ++){
            sum += nums[i];
        }
        if(sum <= 0) return -1; //算出所有回合后的血量是否为正数

        //开始模拟
        long blood = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int last = 0;
        for(int i = 0 ; i < nums.length ; i ++){
            if(nums[i] < 0){
                pq.offer(nums[i]);
                if(blood + nums[i] <= 0){ //这回合过后就要死了，需要把前面扣最多的血移到最后去
                    last ++; //记录移动的次数
                    blood -= pq.poll(); //加回之前扣除最多的血量
                }
            }
            blood += nums[i];
        }
        return last;
    }
}
