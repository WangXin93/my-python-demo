""" Trie
"""
import heapq


class Node(object):
    def __init__(self, char, isKey, children):
        self.char = char
        self.isKey = isKey
        self.children = children


class Trie(object):
    def __init__(self):
        self.root = Node(char="", isKey=False, children=dict())

    def add(self, s):
        node = self.root
        if s == "":
            node.isKey = True
        for i in range(len(s)):
            c = s[i]
            if c not in node.children:
                node.children[c] = Node(char=c, isKey=False, children=dict())
            node = node.children[c]
            if i == len(s) - 1:
                node.isKey = True

    def contains(self, s):
        node = self.root
        if s == "":
            return node.isKey
        for i in range(len(s)):
            c = s[i]
            if c not in node.children:
                return False
            node = node.children[c]
        if not node.isKey:
            return False
        return True

    def keysWithPrefix(self, s):
        prefix = list(s)
        strStack = []
        lst = []
        self._keyWithPrefixHelper(prefix, self.root, strStack, lst)
        return [heapq.heappop(lst)[1] for _ in range(len(lst))]

    def _keyWithPrefixHelper(self, prefix, currNode, strStack, lst):
        if prefix and prefix[0] not in currNode.children:
            return
        if prefix:
            head = prefix.pop(0)
            strStack.append(head)
            self._keyWithPrefixHelper(prefix, currNode.children[head],
                                      strStack, lst)
        else:
            if currNode.isKey:
                heapq.heappush(lst, (len(strStack), ''.join(strStack)))
            if currNode.children:
                for child in currNode.children.values():
                    strStack.append(child.char)
                    self._keyWithPrefixHelper(prefix, child, strStack, lst)
                    strStack.pop(-1)

    def longestPrefixOf(self, s):
        node = self.root
        strStack = []
        for i in range(len(s)):
            c = s[i]
            if c in node.children:
                node = node.children[c]
                strStack.append(node.char)
        return ''.join(strStack)


if __name__ == "__main__":
    t = Trie()
    t.add("hello")
    t.add("hi")
    t.add("help")
    t.add("heip")
    t.add("zebra")
    print(t.contains("hello"))
    print(t.contains("hi"))
    print(t.contains("help"))
    print(t.contains("zebra"))
    print(t.contains("hell"))
    print(t.contains("zebrahah"))
    print(t.keysWithPrefix("h"))  # ['hello', 'hi', 'help']
    print(t.longestPrefixOf("helloo"))  # Hello
