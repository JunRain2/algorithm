class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
//    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
//        var a = list1
//        var b = list2
//
//        var result = ListNode(0)
//        var node: ListNode? = result
//
//        while (a != null && b != null) {
//            if (a.`val` < b.`val`) {
//                node?.next = ListNode(a.`val`)
//                a = a.next
//            } else {
//                node?.next = ListNode(b.`val`)
//                b = b.next
//            }
//            node = node?.next
//        }
//
//        if (a == null) {
//            node?.next = b
//        } else {
//            node?.next = a
//        }
//
//        return result.next
//    }

    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        if(list1 == null) return list2
        if(list2 == null) return list1

        return if (list1.`val` < list2.`val`) {
            list1.next = mergeTwoLists(list1.next, list2)
            list1
        } else {
            list2.next = mergeTwoLists(list2.next, list1)
            list2
        }
    }
}