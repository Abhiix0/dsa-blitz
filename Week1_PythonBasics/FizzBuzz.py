class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
      output = []
      for i in range(1, n+1):
        if i % 3 == 0:
            ans = "Fizz"
            if i % 5 == 0:
                ans = "FizzBuzz"
        elif i % 5 == 0:
            ans = "Buzz"
        else:
            ans = str(i)
        output.append(ans)
      print(output)
      return output

#this problem can be solved in O(n) time complexity by iterating through the numbers from 1 to n and checking the divisibility of each number by 3 and 5. If a number is divisible by both 3 and 5, we append "FizzBuzz" to the output list. If it is only divisible by 3, we append "Fizz", and if it is only divisible by 5, we append "Buzz". If it is not divisible by either, we append the number itself as a string. Finally, we return the output list containing the FizzBuzz results.