from functools import reduce


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        products = []
        for k in range(2, n + 1):
            sum_list = k * [n // k]
            for i in range(n - (n // k) * k):
                sum_list[i] += 1
            products.append(reduce(lambda x, y: x * y, sum_list))
            if len(products) > 1 and products[-1] <= products[-2]:
                break
        return products[-2]
