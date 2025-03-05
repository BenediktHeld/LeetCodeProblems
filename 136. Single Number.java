import java.util.ArrayList;

class Solution {
 public int singleNumber(int[] nums) {
        List<Integer> numbers = new ArrayList<>();
        
        for(int i=0;i<nums.length;i++){
        int currentNum = nums[i];
        if (numbers.contains(currentNum) == true){
			int positionOfNum = numbers.indexOf(currentNum);
            numbers.remove(positionOfNum);
        	}
        else{
        	numbers.add(nums[i]);
        }
      }
      return numbers.get(0);
    }
}
