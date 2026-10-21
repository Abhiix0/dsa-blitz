from collections import Counter
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = Counter()
        players = set()
        answer = [[],[]]
        for m in matches:
            losses[m[1]] += 1
            players.add(m[0])
            players.add(m[1])
        for n in players:
            if n not in losses:
                answer[0].append(n)
            if losses[n] == 1:
                answer[1].append(n)
        answer[0]= sorted(answer[0])
        answer[1]= sorted(answer[1])
        return answer

#this problem can be solved using a Counter data structure. The function findWinners takes a list of matches as input, where each match is represented by a list of two integers (the winner and the loser). It counts the number of losses for each player using the Counter class and keeps track of all players in a set. After processing all matches, it iterates through the set of players to identify those who have not lost any matches (added to answer[0]) and those who have lost exactly one match (added to answer[1]). Finally, it sorts both lists and returns them as the final answer.