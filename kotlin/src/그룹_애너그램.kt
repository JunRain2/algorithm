class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val words = mutableMapOf<List<Char>, MutableList<String>>()

        for (s in strs) {
            val key = s.toList().sorted()

            words.getOrPut(key) { mutableListOf() }.add(s)
        }

        return words.values.toList()
    }

    fun groupAnagrams2(strs: Array<String>): List<List<String>> {
        return strs.groupBy { it.toList().sorted() }.values.toList()
    }
}