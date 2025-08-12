class Solution {
    fun isPalindrome(s: String): Boolean {
        var start = 0
        var end = s.length - 1

        while (start < end) {
            when {
                !Character.isLetterOrDigit(s[start]) -> start++
                !Character.isLetterOrDigit(s[end]) -> end--
                Character.toLowerCase(s[start]) != Character.toLowerCase(s[end]) -> return false
                else -> {
                    start++
                    end--
                }
            }
        }
        return true
    }
}