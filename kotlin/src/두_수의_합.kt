class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val numsMap = mutableMapOf<Int, Int>()

        for ((i, n) in nums.withIndex()) {
            if (numsMap.containsKey(target - n)) {
                return intArrayOf(numsMap[target - n] ?: 0, i)
            }

            numsMap[n] = i
        }

        return intArrayOf(0, 0)
    }
}