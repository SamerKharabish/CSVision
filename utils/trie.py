""" Defines a TrieNode class and a Trie class. """

from typing import Union, Iterable

class TrieNode:
    """
    Class representing a node in the Trie. Each node contains a dictionary of children nodes,
    a flag indicating if it is the end of a word, and a list of strings that pass through this node.
    """

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.strings: list[Union[str, Iterable[str]]] = []


class Trie:
    """
    Trie (prefix tree) for efficient prefix-based searches.
    Supports insertion of strings and searching for strings by prefix.
    """

    def __init__(self):
        self.__root: TrieNode = TrieNode()

    def insert(self, word: str, original_string: Union[str, Iterable[str]]) -> None:
        """
        Inserts a word into the Trie. Each node along the path of the word
        stores the original string associated with the word.

        Args:
            word (str): The word that will be inserted into the trie.
            original_string (Union[str, Iterable[str]]): The group name and the substring.
        """
        node: TrieNode = self.__root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.strings.append(original_string)
        node.is_end_of_word = True

    def search_prefix(self, prefix: str) -> list[tuple[str, str]]:
        """
        Searches for all strings in the Trie that match the given prefix.

        Args:
            prefix (str): The search term.

        Returns:
            list[tuple[str, str]]: List of original strings associated with the matched prefix
        """
        node: TrieNode = self.__root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.strings

    def reset(self) -> None:
        """
        Reset the trie.
        """
        self.__root = TrieNode()
