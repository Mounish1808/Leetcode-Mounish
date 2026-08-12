# Last updated: 12/08/2026, 12:06:38
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        return sum(p*(100-d)/100 for p,d in zip(prices,discounts))+sum(prices[len(discounts):])
        