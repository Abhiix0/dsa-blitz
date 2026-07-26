class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = []

        for i in range(len(names)):
            people.append([names[i], heights[i]])

        people.sort(key=lambda x: x[1], reverse=True)

        result = []

        for person in people:
            result.append(person[0])

        return result

#This problem can be solved in O(n log n) time complexity, where n is the length of the input lists. We first create a list of pairs (name, height) by iterating through the names and heights lists. We then sort this list of pairs based on the height in descending order using a custom sorting key. Finally, we extract the names from the sorted list of pairs and return them as the result.