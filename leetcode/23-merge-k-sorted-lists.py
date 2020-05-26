from utils import ListNode, prettyPrintLinkedList, stringToListNode
from typing import List
import heapq


class Solution:
    # Divide and conquer O(N log K)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            dummy = ListNode(-1)
            curr = dummy
            left, right = lists[0], lists[1]
            while True:
                if left is None:
                    curr.next = right
                    break
                elif right is None:
                    curr.next = left
                    break
                elif left.val < right.val:
                    curr.next = left
                    curr = curr.next
                    left = left.next
                else:
                    curr.next = right
                    curr = curr.next
                    right = right.next
            return dummy.next
        else:
            mid = len(lists) // 2
            left = lists[:mid]
            right = lists[mid:]
            left = self.mergeKLists(left)
            right = self.mergeKLists(right)
            return self.mergeKLists([left, right])

    # Use heap O(A log(A))
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     heads = lists.copy()
    #     q = []
    #     for i, node in enumerate(lists):
    #         heapq.heappush(q, (node.val, i))
    #     dummy = ListNode(-1)
    #     curr = dummy
    #     while q:
    #         v, i = heapq.heappop(q)
    #         curr.next = heads[i]
    #         curr = curr.next
    #         heads[i] = heads[i].next
    #         if heads[i] is not None:
    #             heapq.heappush(q, (heads[i].val, i))
    #     return dummy.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     def nodeGen(node):
    #         while node is not None:
    #             yield node.val
    #             node = node.next

    #     def merged():
    #         gens = list(map(nodeGen, lists))
    #         q = []
    #         for i, gen in enumerate(gens):
    #             v = next(gen, None)
    #             if v is not None:
    #                 heapq.heappush(q, (v, i))
    #         while q:
    #             v, i = heapq.heappop(q)
    #             yield v
    #             newV = next(gens[i], None)
    #             if newV is not None:
    #                 heapq.heappush(q, (newV, i))

    #     dummy = ListNode(-1)
    #     curr = dummy
    #     for v in merged():
    #         curr.next = ListNode(v)
    #         curr = curr.next
    #     return dummy.next


    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     heads = [n for n in lists]
    #     out = ListNode(-1)
    #     curr = out
    #     while True:
    #         lenHeads = len(heads)
    #         if lenHeads == 0:
    #             break
    #         if lenHeads == 1:
    #             curr.next = heads[0]
    #             break
    #         minVal, minI = float('inf'), -1
    #         i = 0
    #         for _ in range(lenHeads):
    #             if heads[i].val < minVal:
    #                 minVal = heads[i].val
    #                 minI = i
    #             i += 1
    #         if minI > -1:
    #             curr.next = heads[minI]
    #             curr = curr.next
    #             heads[minI] = heads[minI].next
    #             if heads[minI] is None:
    #                 heads.pop(minI)
    #     return out.next


if __name__ == "__main__":
    lst1 = stringToListNode("[1, 4, 5]")
    lst2 = stringToListNode("[1, 3, 4]")
    lst3 = stringToListNode("[2, 6]")
    prettyPrintLinkedList(Solution().mergeKLists([lst1, lst2, lst3]))
