class Solution {
    var left = 0
    var maxLen = 0

    fun extendPalindrome(s: String, j: Int, k: Int) {
        var l = j
        var r = k

        while(l >= 0 && r < s.length && s[l] == s[r]) {
            l--
            r++
        }

        if (maxLen < r - l - 1) {
            left = l + 1
            maxLen = r - l - 1
        }
    }

    fun longestPalindrome(s: String): String {
        val len = s.length

        if (len < 2) return s

        for (i in 0..<len) {
            extendPalindrome(s, i, i + 1)
            extendPalindrome(s, i, i + 2)
        }
        return s.substring(left, left + maxLen)
    }
}
