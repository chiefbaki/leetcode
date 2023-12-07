# Brute Force
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Dart code
"""class Solution {
  List<int> twoSum(List<int> nums, int target) {
    for(int i = 0; i < nums.length; i++){
        for(int j = i + 1; j < nums.length; j++){
            if(nums[i] + nums[j] == target){
                return [i, j];
            }
        }
    } 
    return [];
  }
}"""
