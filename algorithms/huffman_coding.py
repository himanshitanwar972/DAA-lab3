import heapq
from collections import Counter
from itertools import count


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


def build_huffman_tree(text):
    if not text:
        raise ValueError("Input text cannot be empty.")

    frequencies = Counter(text)
    unique_id = count()

    heap = [
        (freq, next(unique_id), Node(char, freq))
        for char, freq in frequencies.items()
    ]

    heapq.heapify(heap)

    while len(heap) > 1:
        left_freq, _, left = heapq.heappop(heap)
        right_freq, _, right = heapq.heappop(heap)

        merged = Node(
            None,
            left_freq + right_freq,
            left,
            right
        )

        heapq.heappush(
            heap,
            (merged.freq, next(unique_id), merged)
        )

    return heap[0][2]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node.char is not None:
        codebook[node.char] = prefix or "0"
        return codebook

    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encode(text):
    if not text:
        raise ValueError("Input text cannot be empty.")

    root = build_huffman_tree(text)
    codebook = generate_codes(root)

    encoded = "".join(codebook[char] for char in text)

    original_bits = len(text) * 8
    encoded_bits = len(encoded)

    compression_ratio = (
        encoded_bits / original_bits
        if original_bits > 0
        else 0
    )

    space_saved = (
        (1 - compression_ratio) * 100
        if original_bits > 0
        else 0
    )

    return {
        "root": root,
        "frequencies": dict(Counter(text)),
        "codes": codebook,
        "encoded": encoded,
        "original_bits": original_bits,
        "encoded_bits": encoded_bits,
        "compression_ratio": compression_ratio,
        "space_saved_percent": space_saved
    }