# Two Sum Problem

## Problem Description

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

### Examples

#### Example 1
- **Input:** `nums = [2, 7, 11, 15]`, `target = 9`
- **Output:** `[0, 1]`
- **Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

#### Example 2
- **Input:** `nums = [3, 2, 4]`, `target = 6`
- **Output:** `[1, 2]`

#### Example 3
- **Input:** `nums = [3, 3]`, `target = 6`
- **Output:** `[0, 1]`

### Constraints
- $2 \le \text{nums.length} \le 10^4$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
- **Only one valid answer exists.**

---

## Core Logic & Intuition

### Key Insight
Instead of checking every pair of numbers (which takes $O(n^2)$ time), we can leverage a **Hash Map (Dictionary)** to look up complement values in **$O(1)$ constant time**.

For any element `x` at index `i`, we need to find if there exists a previously seen element `y` at index `j` such that:
$$x + y = \text{target} \implies y = \text{target} - x$$

### Algorithm Steps (One-Pass Hash Map)
1. Initialize an empty hash map `seen` to store `{value: index}` pairs.
2. Iterate through the `nums` array using index `i` and value `num`:
   - Calculate the required complement: `complement = target - num`.
   - Check if `complement` is already in the `seen` hash map:
     - **If yes:** We found our pair! Return `[seen[complement], i]`.
     - **If no:** Add the current number and its index to the hash map: `seen[num] = i`.
3. Since the problem guarantees exactly one solution, a valid pair will always be found during the traversal.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(n)$ — We iterate through the array of $n$ elements at most once. Hash map insertion and lookup operations take $\mathcal{O}(1)$ average time.
- **Space Complexity:** $\mathcal{O}(n)$ — In the worst-case scenario, we store up to $n$ elements in the hash map.

---

## Python Solution

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in the hash map
            if complement in seen:
                return [seen[complement], i]
            
            # Store the current number and its index
            seen[num] = i
            
        return []

# Test execution
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1
    print("Example 1 Output:", sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    
    # Test Example 2
    print("Example 2 Output:", sol.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
    
    # Test Example 3
    print("Example 3 Output:", sol.twoSum([3, 3], 6))          # Expected: [0, 1]