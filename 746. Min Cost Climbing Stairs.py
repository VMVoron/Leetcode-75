class Solution:
    def minCostClimbingStairs(self, cost):
        f = g = 0
        for i in range(2, len(cost) + 1):
            # Compute the minimum cost to reach the current step by taking
            # a single step from the previous step or a double step from the one before previous.
            # This compares the cost of reaching the previous step and one step before that,
            # added to the cost of the step that would be taken.
            f, g = g, min(f + cost[i - 2], g + cost[i - 1])
            # Update the previous step cost for the next iteration
        return g
