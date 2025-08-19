class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        return reverse(head, null)
    }

    fun reverse(current: ListNode?, prev: ListNode?): ListNode?{
        if (current == null) {
            return prev
        }

        val next = current.next
        current.next = prev
        return reverse(next, current)
    }
}