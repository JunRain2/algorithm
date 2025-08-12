class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val counts = mutableMapOf<String, Int>()

        val words = paragraph.replace("\\W+".toRegex(), " ").lowercase().trim().split(" ")

        for (w in words) {
            if(w !in banned) {
                counts[w] = counts.getOrDefault(w, 0) + 1
            }
        }

        return counts.maxBy { it.value }.key
    }
}