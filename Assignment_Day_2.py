lottery = "hello coders"

print("Congratulation you have successfully entered the lottery and got a chance to win the lottery!! ")
print("Choose correct character of the word '",lottery,"' to win the lottery")
inputs = input(" ").lower()

if inputs == lottery[0] or inputs == lottery[1] or inputs == lottery[4] or inputs == lottery[6] or inputs == lottery[8] :
    print("congratulation, you win the lottery")
else:
    print("sorry, You didn't win the lottery")