from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

def run_verification(nums: List[int], target: int) -> None:
    sol = Solution()
    print(f"Testing nums = {nums}, target = {target}")
    
    n = len(nums)
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = nums[i] + nums[j]
            print(f"  Checking indices ({i}, {j}): {nums[i]} + {nums[j]} = {current_sum}", end="")
            if current_sum == target:
                print(" -> MATCH FOUND!")
                found = True
                break
            else:
                print(" -> No match")
        if found:
            break
            
    result = sol.twoSum(nums, target)
    print(f"Result: {result}\n" + "-"*40)

if __name__ == "__main__":
    run_verification([2, 7, 11, 15], 9)
    run_verification([3, 2, 4], 6)
    run_verification([3, 3], 6)