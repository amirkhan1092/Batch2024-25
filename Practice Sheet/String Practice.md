### **Easy Questions**

#### 1. **Reverse a String**
**Problem:**
Write a function to reverse a given string.

**Scenario:**
You are writing a program to reverse the input string for display purposes.

**Example:**
```python
Input: "hello"
Output: "olleh"
```

#### 2. **Check if a String is Palindrome**
**Problem:**
Write a function to check if a given string is a palindrome.

**Scenario:**
You need to verify if a user-entered string reads the same forward and backward.

**Example:**
```python
Input: "madam"
Output: True

Input: "hello"
Output: False
```

#### 3. **Count Vowels in a String**
**Problem:**
Write a function to count the number of vowels in a string.

**Scenario:**
You are tasked with calculating how many vowels appear in a given sentence.

**Example:**
```python
Input: "apple"
Output: 2

Input: "python"
Output: 1
```

#### 4. **Remove Spaces from a String**
**Problem:**
Write a function to remove all spaces from a given string.

**Scenario:**
You are processing user input and need to remove any spaces for validation purposes.

**Example:**
```python
Input: "hello world"
Output: "helloworld"
```

#### 5. **Check if Two Strings are Anagrams**
**Problem:**
Write a function to check if two strings are anagrams (i.e., they contain the same characters in different order).

**Scenario:**
You are working on a text processing tool and need to check if two words are anagrams.

**Example:**
```python
Input: "listen", "silent"
Output: True

Input: "apple", "pale"
Output: False
```

---

### **Medium Questions**

#### 6. **Find the Longest Word in a String**
**Problem:**
Write a function to find the longest word in a given sentence.

**Scenario:**
You need to highlight the longest word from a text document.

**Example:**
```python
Input: "The quick brown fox"
Output: "quick"
```

#### 7. **Replace Spaces with %20 (URL Encoding)**
**Problem:**
Write a function that replaces all spaces in a string with `%20`.

**Scenario:**
You are working on URL encoding where spaces must be replaced with `%20`.

**Example:**
```python
Input: "hello world"
Output: "hello%20world"
```

#### 8. **Count Frequency of Each Character**
**Problem:**
Write a function to count the frequency of each character in a string.

**Scenario:**
You are analyzing text data and need to find the frequency of individual characters.

**Example:**
```python
Input: "apple"
Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```

#### 9. **Find the First Non-Repeating Character**
**Problem:**
Write a function to find the first non-repeating character in a string.

**Scenario:**
You need to identify the first character in a string that does not repeat.

**Example:**
```python
Input: "swiss"
Output: "w"
```

#### 10. **Check if Two Strings are Rotations of Each Other**
**Problem:**
Write a function to check if one string is a rotation of another string.

**Scenario:**
You are developing a circular queue system and need to check if one sequence is a rotated version of another.

**Example:**
```python
Input: "abcde", "deabc"
Output: True

Input: "abcde", "abced"
Output: False
```

#### 11. **Find All Permutations of a String**
**Problem:**
Write a function to generate all possible permutations of a given string.

**Scenario:**
You are working on a password generator, and need to generate all possible combinations.

**Example:**
```python
Input: "abc"
Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

#### 12. **Compress a String Using the Counts of Repeated Characters**
**Problem:**
Write a function to compress a string by replacing consecutive repeated characters with the character followed by the count.

**Scenario:**
You are implementing a data compression algorithm.

**Example:**
```python
Input: "aaabbcccc"
Output: "a3b2c4"
```

#### 13. **Find the Most Frequent Word in a String**
**Problem:**
Write a function to find the most frequent word in a sentence.

**Scenario:**
You are analyzing customer reviews and need to find the most frequently mentioned word.

**Example:**
```python
Input: "apple banana apple orange banana apple"
Output: "apple"
```

#### 14. **Check if a String Contains Only Digits**
**Problem:**
Write a function to check if a string contains only digits.

**Scenario:**
You are validating a phone number input to ensure that it only contains numbers.

**Example:**
```python
Input: "12345"
Output: True

Input: "123a5"
Output: False
```

#### 15. **Find the Longest Palindromic Substring**
**Problem:**
Write a function to find the longest palindromic substring in a given string.

**Scenario:**
You are working on a DNA sequence analyzer and need to find the longest palindromic sequence in a strand.

**Example:**
```python
Input: "babad"
Output: "bab"
```

---

### **Hard Questions**

#### 16. **Find the Longest Substring Without Repeating Characters**
**Problem:**
Write a function to find the longest substring without repeating characters.

**Scenario:**
You are analyzing user passwords to ensure there are no consecutive repeating characters.

**Example:**
```python
Input: "abcabcbb"
Output: 3 ("abc")
```

#### 17. **Group Anagrams from a List of Strings**
**Problem:**
Write a function to group anagrams from a list of strings.

**Scenario:**
You are organizing a list of words for a word puzzle and want to group words that are anagrams.

**Example:**
```python
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

#### 18. **Wildcard Pattern Matching**
**Problem:**
Write a function to check if a string matches a given pattern with `?` for any single character and `*` for any sequence of characters.

**Scenario:**
You are building a file search tool where users can use wildcards in file names.

**Example:**
```python
Input: "abc", "a*c"
Output: True
```

#### 19. **Find All Subsequences of a String**
**Problem:**
Write a function to find all subsequences of a string.

**Scenario:**
You are working on a code autocompletion system and need to generate possible subsequences for matching.

**Example:**
```python
Input: "abc"
Output: ["", "a", "b", "c", "ab", "ac", "bc", "abc"]
```

#### 20. **Minimum Window Substring**
**Problem:**
Write a function to find the minimum window substring in a string that contains all the characters of another string.

**Scenario:**
You are processing a large text document and need to find the smallest segment that contains all the keywords.

**Example:**
```python
Input: "ADOBECODEBANC", "ABC"
Output: "BANC"
```