class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun isPalindrome(head: ListNode?): Boolean {
        var fast = head
        var slow = head

        while ((fast != null) && (fast.next != null)) {
            fast = fast.next?.next
            slow = slow?.next
        }

        if (fast != null) {
            slow = slow?.next
        }

        var rev: ListNode? = null
        while (slow != null) {
            val next = slow.next
            slow.next = rev
            rev = slow
            slow = next
        }

        var left = head
        while (rev != null && left != null) {
            if (rev.`val` != left.`val`) {
                return false
            }

            rev = rev.next
            left = left.next
        }

        return true
    }
}