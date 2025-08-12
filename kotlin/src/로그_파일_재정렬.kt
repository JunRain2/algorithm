class Solution {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        val letterList = mutableListOf<String>()
        val digitList = mutableListOf<String>()

        for (log in logs) {
            if (Character.isDigit(log.split(" ")[1][0])) {
                digitList.add(log)
            } else {
                letterList.add(log)
            }
        }

        letterList.sortWith(Comparator { s1, s2 ->
            val s1x = s1.split(" ", limit = 2) // limit라는 표현은 2덩이로 자른다는 의미
            val s2x = s2.split(" ", limit = 2)

            val compared = s1x[1].compareTo(s2x[1])
            if (compared == 0) {
                s1x[0].compareTo(s2x[0])
            } else {
                compared
            }
        })

        return (letterList + digitList).toTypedArray()
    }
}