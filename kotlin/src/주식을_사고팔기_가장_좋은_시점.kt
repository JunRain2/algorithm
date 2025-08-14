class Solution {
    fun maxProfit(prices: IntArray): Int {
        var min = prices[0]
        var result = 0

        for (i in 1..<prices.size) {
            min = min.coerceAtMost(prices[i]) // 상한선 걸어두기
            result = result.coerceAtLeast(prices[i] - min) // 하한선 걸어두기
        }

        return result
    }
}