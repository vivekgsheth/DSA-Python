#User function Template for python3
class Solution:
    def subset(self, idx, s, n, arr, result):
        
        # base case
        if idx == n:
            result.append(s)
            return
    
        s += arr[idx]
        self.subset(idx+1, s, n, arr, result)
        s -= arr[idx]
        
        self.subset(idx+1, s, n, arr, result)
    
    
    def subsetSums(self, arr, N):
        
        result = []
        self.subset(0, 0, len(arr), arr, result)
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
