'''
- if the len(s) < k return 0
- move along the character and count the freq of the next char, and -1 the one before
- if catch a repeat, can move the left pointer to that character, because no point continue sliding
through the substring with repeated characters
- Time O(n) to go through the array 
- Space O(26) to store the freq
'''

def solution(s, k):
    if len(s) < k:
        return 0
    
    res = 0
    freq = {}
    flag = True

    for i in range(k):
        freq[s[i]] = freq.get(s[i], 0) + 1
        
    for i in freq.values():
        if i > 1:
            flag = False
    if flag:
        res += 1
    
    for r in range(k, len(s)):
        flag = True
        freq[s[r]] = freq.get(s[r], 0) + 1
        freq[s[l]] = freq[s[l]] - 1
        for i in freq.values():
            if i > 1:
                flag = False
                break
        if flag:
            res += 1
        l += 1

    return res

print(solution("home", 5))
