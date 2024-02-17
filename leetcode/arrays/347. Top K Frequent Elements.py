'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

from collections import defaultdict

def topKFrequent(nums, k):
    '''
    Given: [1, 1, 1, 2, 2, 3], k = 2 -> Return: 1, 2
    [1], k = 1 -> Return: 1

    TODO:
    - Need a dictionary to store the frequencies and the number corresponding to that freq
    - Eg: 0: {}, 1: {3}, 2:, {2}, 3: {1}
    - Max length of dictionary = array len + 1
    - Time: O(n)
    - Storage: O(n)
    '''
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if res.length() == k:
                return res
    