class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * (n + 1)

        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        current = 0
        a = []

        for i in range(len(diff) - 1):
            current += diff[i]
            a.append(current)

        return a

#this problem can be solved in O(n + m) time complexity, where n is the number of flights and m is the number of bookings. We use a difference array to efficiently apply the seat bookings to the flights. By iterating through the bookings and updating the difference array, we can then compute the final number of seats for each flight by taking the prefix sum of the difference array.