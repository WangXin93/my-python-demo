"""
Consider three situations:
* delete at the beginning
* delete at the middle
* delete at the end
"""
from utils import ListNode, stringToListNode, prettyPrintLinkedList


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Two pass
        # lenList = 0
        # h = head
        # while h is not None:
        #     lenList += 1
        #     h = h.next
        # cnt = 0
        # curr = head
        # prev = None
        # while True:
        #     if cnt == lenList - n:
        #         if prev is None:
        #             return curr.next
        #         else:
        #             prev.next = curr.next
        #             return head
        #     prev = curr
        #     curr = curr.next
        #     cnt += 1

        # One pass
        # prev, fast, slow = None, head, head
        # for i in range(n):
        #     fast = fast.next
        # while fast:
        #     prev = slow
        #     slow = slow.next
        #     fast = fast.next
        # if prev is None:
        #     return slow.next
        # else:
        #     prev.next = slow.next
        #     return head

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        if len(nodes) > n:
            node = nodes[len(nodes) - n - 1]
            if node.next is not None:
                node.next = node.next.next
        else:
            head = head.next
        return head


if __name__ == "__main__":
    lst = stringToListNode("[1, 2, 3, 4, 5]")
    lst = Solution().removeNthFromEnd(lst, 2)
    prettyPrintLinkedList(lst)

    lst = stringToListNode("[1, 2, 3, 4, 5]")
    lst = Solution().removeNthFromEnd(lst, 1)
    prettyPrintLinkedList(lst)

    lst = stringToListNode("[1, 2, 3, 4, 5]")
    lst = Solution().removeNthFromEnd(lst, 5)
    prettyPrintLinkedList(lst)
