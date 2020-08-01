class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_list = sentence.split()
        for i in range(len(word_list)):
            if word_list[i].startswith(searchWord):
                return i + 1
        return -1


sentence = "i love eating burger"
searchWord = "burg"
s = Solution()
print(s.isPrefixOfWord(sentence, searchWord))
