from typing import List
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letterMap = {}
        indegree = {}

        def compare(str1, str2):
            added = False
            for i in range(min(len(str1), len(str2))):
                letterMap.setdefault(str1[i], [])
                letterMap.setdefault(str2[i], [])
                indegree.setdefault(str1[i], 0)
                indegree.setdefault(str2[i], 0)
                if str1[i] != str2[i] and not added:
                    letterMap[str1[i]].append(str2[i])
                    indegree[str2[i]] += 1
                    added = True
            biggerStr = str1 if len(str1) > len(str2) else str2
            for j in range(min(len(str1), len(str2)), max(len(str1), len(str2))):
                letterMap.setdefault(biggerStr[j], [])
                indegree.setdefault(biggerStr[j], 0)

        for word in words:
            for ch in word:
                letterMap.setdefault(ch, [])
                indegree.setdefault(ch, 0)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            compare(word1, word2)
            # Check for invalid prefix order
            if len(word1) > len(word2) and word1.startswith(word2):
                return ''

        queue = deque([letter for letter in indegree if indegree[letter] == 0])
        seen = []

        while queue:
            curr = queue.popleft()
            seen.append(curr)
            for letter in letterMap[curr]:
                indegree[letter] -= 1
                if indegree[letter] == 0:
                    queue.append(letter)

        if len(seen) != len(letterMap):
            return ''
        
        return "".join(seen)
