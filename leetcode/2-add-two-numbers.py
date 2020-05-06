from utils import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        out = None
        currNode = None
        while not (l1 is None and l2 is None and carry == 0):
            currVal = 0
            if l1 is not None:
                currVal += l1.val
            if l2 is not None:
                currVal += l2.val
            if carry == 1:
                currVal += 1
                carry = 0
            if currVal >= 10:
                carry = 1
                currVal -= 10
            if out is None:
                currNode = ListNode(currVal)
                out = currNode
            else:
                currNode.next = ListNode(currVal)
                currNode = currNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return out

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = None
    for num in [5, 6, 4]:
        if l2 is None:
            l2 = ListNode(num)
            cur = l2
        else:
            cur.next = ListNode(num)
            cur = cur.next
    l_12 = Solution().addTwoNumbers(l1, l2)

    print(ListNode.ConvertToList(l_12))
