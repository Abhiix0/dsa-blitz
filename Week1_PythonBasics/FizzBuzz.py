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
    