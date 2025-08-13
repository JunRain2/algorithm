class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        val sortedNum = nums.sorted()
        val result = mutableSetOf<List<Int>>()

        for (right in 2..<sortedNum.size) {
            var left = 0
            var mid = right - 1

            while (left < mid) {
                val sum = sortedNum[left] + sortedNum[mid] + sortedNum[right]

                if (sum == 0) {
                    result.add(listOf(sortedNum[left], sortedNum[mid], sortedNum[right]))
                    left += 1
                    mid -= 1
                } else if (sum > 0) {
                    mid -= 1
                } else {
                    left += 1
                }
            }
        }
        return result.toList()
    }
}
