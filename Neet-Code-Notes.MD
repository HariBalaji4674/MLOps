# Neet-Code Problems and Notes with Solutions

## Contains Duplicates[HashSet]
```
hashSet = set()
for i in nums:
    if i in hashSet:
        return true
    hashSet.add(i)
return False

```

## Two Sum [hashMap]
```
hashMap = {}
for i,num in enumerate(nums):
    diff = target - num
    if diff in hashMap:
        return [hashMap[diff],i]
    hashMap[n] = i
return 
```

## Group Anagrams [HashMap ][defaultdict(list)]
```
res = defaultdict(list)
for word in words:
    count = [0] * 26
    for c in word:
        count[ord(c)-ord(a)] += 1 
    key = tuple(count)
    res[key].append(s)
return res.values()

```

## Given an array which consists of only 0, 1 and 2 [Dutch,National,Flag,Algorithim]

```
low = 0
mid = 0
high = len(n)-1
while mid <= high:
    if mid == 0:
        low,mid = mid,low
        low = low+1
        mid = mid+1
    elif mid == 1:
        mid = mid + 1
    else:
        mid,high = high,mid
        high = high - 1
retrun arr

```
## Move all the negative elements to one side of the array
1. Normal array.sort() or Sorted Metod --> Give O(nlog(n))
```
numbers = []
numbers.sort()
sorted(numbers)

```
2. Quick Sort Algorithim
```
for i in range(len(nums)):
    if arr[i] < 0:
        arr[i],a[j] = a[j],a[i]
        j = j + 1
print(arr)

```
3. Two Pointer Method
4. Two Pass Method 

## Prefix sum

## Kadane’s algo

## Two pointers

## Product of subarray except itself

## Top K Frequent Elements

## Product of Array Except Self

## Valid Sudoku

## Encode and Decode Strings

## Longest Consecutive Sequence

## Valid Palindrome

## Two Sum II Input Array Is Sorted

## 3Sum

## Container With Most Water

## Trapping Rain Water

## Best Time to Buy And Sell Stock

## Longest Substring w/out Repeating Characters

## Longest Repeating Character Replacement

## Permutation In String

## Minimum Window Substring

## Sliding Window Maximum

## Valid Parentheses

## Min Stack

## Evaluate Reverse Polish Notation

## Generate Parentheses
## 
## Daily Temperatures
## 
## Car Fleet
## 
## Largest Rectangle In Histogram
## 
## Binary Search
## 
## Search a 2D Matrix
## 
## Koko Eating Bananas
## 
## Find Minimum In Rotated Sorted Array
## 
## Search In Rotated Sorted Array
## 
## Time Based Key Value Store
## 
## Median of Two Sorted Arrays
## 
## Reverse Linked List
## 
## Merge Two Sorted Lists
## 
## Reorder List
## 
## Remove Nth Node From End of List
## 
## Copy List With Random Pointer
## 
## Add Two Numbers
## 
## Linked List Cycle
## 
## Find The Duplicate Number
## 
## LRU Cache
## 
## Merge K Sorted Lists
## 
## Reverse Nodes In K Group
## 
## Invert Binary Tree
## 
## Maximum Depth of Binary Tree
## 
## Diameter of Binary Tree
## 
## Balanced Binary Tree
## 
## Same Tree
## 
## Subtree of Another Tree
## 
## Lowest Common Ancestor of a Binary Search Tree
## 
## Binary Tree Level Order Traversal
## 
## Binary Tree Right Side View
## 
## Count Good Nodes In Binary Tree
## 
## Validate Binary Search Tree
## 
## Kth Smallest Element In a BST
## 
## Construct Binary Tree
## 
## Binary Tree Maximum Path Sum
## 
## Serialize And Deserialize Binary Tree
## 
## Implement Trie Prefix Tree
## 
## Design Add And Search Words
## 
## Word Search II
## 
## Kth Largest Element In a Stream
## 
## Last Stone Weight
## 
## K Closest Points to Origin
## 
## Kth Largest Element In Array
## 
## Task Scheduler
## 
## Design Twitter
## 
## Find Median From Data Stream
## 
## Subsets
## 
## Combination Sum
## 
## Permutations
## 
## Subsets II
## 
## Combination Sum II
## 
## Word Search
## 
## Palindrome Partitioning
## 
## Letter Combinations of a Phone
## 
## N Queens
## 
## Number of Islands
## 
## Clone Graph
## 
## Max Area of Island
## 
## Pacific Atlantic Water Flow
## 
## Surrounded Regions
## 
## Rotting Oranges
## 
## Walls And Gates
## 
## Course Schedule
## 
## Course Schedule II
## 
## Redundant Connection
## 
## Number of Connected Components
## 
## Graph Valid Tree
## 
## Word Ladder
## 
## Reconstruct Itinerary
## 
## Min Cost to Connect All Points
## 
## Network Delay Time
## 
## Swim in Rising Water
## 
## Alien Dictionary
## 
## Cheapest Flights Within K Stops
## 
## Climbing Stairs
## 
## Min Cost Climbing Stairs
## 
## House Robber
## 
## House Robber II
## 
## Longest Palindromic Substring
## 
## Palindromic Substrings
## 
## Decode Ways
## 
## Coin Change
## 
## Maximum Product Subarray
## 
## Word Break
## 
## Longest Increasing Subsequence
## 
## Partition Equal Subset Sum
## 
## Unique Paths
## 
## Longest Common Subsequence
## 
## Best Time to Buy And Sell Stock II
## 
## Coin Change II
## 
## Target Sum
## 
## Interleaving String
## 
## Longest Increasing Path In a Matrix
## 
## Distinct Subsequences
## 
## Edit Distance
## 
## Burst Balloons
## 
## Regular Expression Matching
## 
## Maximum Subarray
## 
## Jump Game
## 
## Jump Game II
## 
## Gas Station
## 
## Hand of Straights
## 
## Merge Triplets to Form Target Triplet
## 
## Partition Labels
## 
## Valid Parenthesis String
## 
## Insert Interval
## 
## Merge Intervals
## 
## Non Overlapping Intervals
## 
## Meeting Rooms
## 
## Meeting Rooms II
## 
## Minimum Interval to Include Each Query
## 
## Rotate Image
## 
## Spiral Matrix
## 
## Set Matrix Zeroes
## 
## Happy Number
## 
## Plus One
## 
## Pow(x, n)
## 
## Multiply Strings
## 
## Detect Squares
## 
## Single Number
## 
## Number of 1 Bits
## 
## Counting Bits
## 
## Reverse Bits
## 
## Missing Number
## 
## Sum of Two Integers
## 
## Reverse Integer