class Solution:
    def valid(self, nums, k, numOperations):
        m=max(nums)
        s=m+k+2
        f=[0]*s
        r=0
        for num in nums:
            f[num]+=1
        p=[0]*s
        p[0]=f[0]
        for i in range(1,s):p[i]=p[i-1]+f[i]
        for x in range(s):
            if f[x]==0 and numOperations==0:continue
            i=max(0,x-k)
            j=min(s-1,x+k)
            t1=p[j]-(p[i-1] if i>0 else 0)
            t2=f[x]+min(numOperations,t1-f[x])
            r=max(r,int(t2))

        return r