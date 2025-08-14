class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val result = IntArray(nums.size)

        var p = 1
        for (i in nums.indices) {
            result[i] = p
            p *= nums[i]
        }

        p = 1
        for (i in nums.indices.reversed()) {
            result[i] *= p
            p *= nums[i]
        }

        return result
    }
}