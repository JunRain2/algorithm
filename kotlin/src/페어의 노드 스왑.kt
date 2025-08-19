class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun swapPairs(head: ListNode?): ListNode? {
        if (head?.next == null) {
            return head
        }
        // 다음 페어 임시 저장
        val nextPair = head.next?.next

        // 1. 페어의 2번째 노드 첫 번째 노드로 연결
        val next = head.next
        next?.next = head
        head.next = swapPairs(nextPair)

        return next
    }
}