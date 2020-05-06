class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def ConvertToList(n):
        out = []
        while n is not None:
            out.append(n.val)
            n = n.next
        return out
