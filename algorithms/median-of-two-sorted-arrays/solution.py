class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i=0
        j=0
        num=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                num.append(nums1[i])
                i+=1
            else:
                num.append(nums2[j])
                j+=1
        while i<len(nums1):
            num.append(nums1[i])
            i+=1
        while j<len(nums2):
            num.append(nums2[j])
            j+=1
        n=len(num)
        if n%2==0:
            median=(num[n//2]+num[n//2-1])/2
        else:
            median=num[n//2]
        return median