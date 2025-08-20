class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        if (head == null) {
            return null
        }
        val root = ListNode(0)
        root.next= head

        var start = root
        for (i in 0..<left) {
            start = start.next
        }
        val end = start.next
        for (i in 0..<(right - left)) {
            val tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        }

        return root.next
    }
}