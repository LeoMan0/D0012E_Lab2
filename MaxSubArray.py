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
