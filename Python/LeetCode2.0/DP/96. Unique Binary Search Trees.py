
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3



input: n: int; n is number of nodes; the value range of n: [0, inf]
output: int, the number of BSF
corner case: n == 0, return 0

Method - DP
DP[i]: the number of BST when the number of nodes is i 

each node can become a root, i
root.left: 1 ~ i - 1
root.right: i + 1 ~ n

dp[j-1]为左子树的排列方式种树
dp[i-j]为左子树的排列方式种树
for j in range(1,i+1):
dp[i]+=dp[j-1]*dp[i-j]
'''


class Tree:
	def buildTree(self, n):
		if n == 0:
			return 0
		
		dp = [0] * (n + 1)
		for i in range(1, n + 1):
			for j in range(1, i + 1):
				if i == 1:
					dp[i] = 1
				else:
					dp[i] += dp[j - 1] * dp[i - j]
return dp[n] 
