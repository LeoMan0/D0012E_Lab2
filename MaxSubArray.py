class MaxSubArray:
    def __init__(self):
        self.test = 0


    def findMaxSubArray(self, arr):
        #Inner function so that maxSubArray methond only has to be called with 1 arugument
        def solve(arr, head, tail):

            if head == tail:
                return {
                'max': arr[head],
                'prefix': arr[head],
                'suffix': arr[head],
                'total': arr[head]
                }

            middle = (head + tail) // 2

            left = solve(arr, head, middle)
            right = solve(arr, middle + 1, tail)
            
            across = left['suffix'] + right['prefix']
            maxValue = max(left['max'], right['max'], across)

            prefix = max(left['prefix'], left['total'] + right['prefix'])
            suffix = max(right['suffix'], right['total'] + left['suffix'])

            total = left['total'] + right['total']

            return {
            'max': maxValue,
            'prefix': prefix,
            'suffix': suffix,
            'total': total
            }
        values = solve(arr, 0, len(arr) - 1)
        return values['max']


  
    def maxSubArray(self, arr, head, tail):

        def acrossMiddle(arr, head, middle, tail):
            leftSum = -1000000
            sum = 0
            for i in range(middle, head -1, -1):
                sum += arr[i]
                if sum > leftSum:
                    leftSum = sum

            rightSum = -1000000
            sum = 0
            for i in range(middle + 1, tail +1):
                sum += arr[i]
                if sum > rightSum:
                    rightSum = sum
            return leftSum + rightSum



        if head == tail:
            return arr[tail]
        middle = (head + tail) // 2

        left = self.maxSubArray(arr, head, middle)
        right = self.maxSubArray(arr, middle + 1, tail)
        across = acrossMiddle(arr, head, middle, tail)

        return max(left, right, across)


    def maxiSubArray(self, nums):
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)


