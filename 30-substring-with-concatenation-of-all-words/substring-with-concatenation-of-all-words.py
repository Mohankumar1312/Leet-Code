from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        ans = []
        
        # Iterate over each possible starting offset within the word length
        for i in range(word_len):
            left = i
            current_count = Counter()
            matched = 0
            
            # Slide window across the string in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    current_count[word] += 1
                    matched += 1
                    
                    # If we have too many instances of this word, shrink from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        matched -= 1
                        left += word_len
                        
                    # If all words matched, record the starting index
                    if matched == num_words:
                        ans.append(left)
                else:
                    # Reset the window if we encounter an invalid word
                    current_count.clear()
                    matched = 0
                    left = right + word_len
                    
        return ans