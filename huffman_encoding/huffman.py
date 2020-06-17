"""
https://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/#:~:text=Huffman%20Coding%20%2D%20Python%20Implementation,given%20the%20smallest%20length%20code.

Huffman Compression:
Step1: Building frequency dictionary
Step2: Build heap
Step3: Merge heap nodes and Build tree
Step4: Traverse tree and Make codesMap
Step5: Encode text
"""

from collections import Counter
from trie import Node, Trie
import heapq

class HeapNode(Node):
    def __init__(self, char, isKey, children, freq, key):
        super(HeapNode, self).__init__(char, isKey, children)
        self.freq = freq
        self.key = key

    def __gt__(self, other):
        return self.freq > other.freq


class Huffman:
    def make_frequency_dict(self, text):
        c = Counter(text)
        total = sum(c.values())
        freq = {k: v/total for k, v in c.items()}
        return freq

    def make_heap(self, freq):
        heap = []
        for k, v in freq.items():
            node = HeapNode('', True, dict(), v, k)
            heapq.heappush(heap, node)
        return heap

    def merge_heap(self, heap):
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node1.char = '0'
            node2 = heapq.heappop(heap)
            node2.char = '1'
            merged = HeapNode('', False, dict(), node1.freq + node2.freq, None)
            merged.children['0'] = node1
            merged.children['1'] = node2
            heapq.heappush(heap, merged)
        return heap

    def make_codemap(self, node):
        codemap = {}
        def helper(node, prefix=''):
            if node.isKey:
                codemap[node.key] = prefix
            for k, v in node.children.items():
                helper(v, prefix+k)
        helper(node)
        return codemap

    def compress(self, text):
        freq = self.make_frequency_dict(text)
        heap = self.make_heap(freq)
        heap = self.merge_heap(heap)
        root = heap[0]
        codemap = self.make_codemap(root)
        trie = Trie()
        trie.root = root

        encoded = []
        for c in text:
            encoded.append(codemap[c])

        print("Compressed.")
        return trie, codemap, ''.join(encoded)

    def decompress(self, trie, compressed):
        compressed = list(compressed)
        res = []
        def findLeaf(node, compressed):
            while compressed:
                if compressed[0] in node.children:
                    head = compressed.pop(0)
                    node = node.children[head]
                if node.isKey:
                    return node.key
        while compressed:
            res.append(findLeaf(trie.root, compressed))
        return ''.join(res)

    def write(self, compressed, fname):
        extra_padding = 8 - len(compressed) % 8
        compressed = compressed + '0'*extra_padding
        padding_info = "{0:08b}".format(extra_padding)
        compressed = padding_info + compressed

        ba = bytearray()
        for i in range(0, len(compressed), 8):
            byte = compressed[i:i+8]
            ba.append(int(byte, 2))

        with open(fname, 'wb') as f:
            f.write(bytes(ba))

        print("Saved")

    def read(self, fname):
        bc = open(fname, 'rb').read()
        padding_info = bc[0]
        bit_string = ""
        for i in range(1, len(bc)):
            bit_string += "{0:08b}".format(bc[i])
        bit_string = bit_string[:-padding_info]
        return bit_string


if __name__ == "__main__":
    hf = Huffman()
    text = open("./argument.txt").read()
    trie, codemap, compressed = hf.compress(text)
    decompressed = hf.decompress(trie, compressed)
    print(text == decompressed)
    hf.write(compressed, "argument.bin")
    bit_string = hf.read("./argument.bin")
    decompressed = hf.decompress(trie, bit_string)
    print(text == decompressed)
