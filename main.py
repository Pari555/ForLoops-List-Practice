emojiList = ["😃","❤️","🥭","🌸","🦋","🤘🏻","🥴"]
#Using a for loop , print out each emoji on your list
#Print out the length of your list
#Print out the fourth item in your list
for index in emojiList:
  print(index)

print(len(emojiList))

print(emojiList[3])

#Create a favorite Emoji variable and set that equal to your favorite emoji on the list
favEmoji = emojiList[6]

#Create a for loop,make a pyramid with your favorite emoji
for index in range(1, 11):
  print((favEmoji + " ") * index)

#Upside Down Pyramid (start,stop,step)
#Step number is defalted to +1
for index in range(10, 0, -1):
  print((favEmoji + " ") * index)

#Pyramid that is right aligned
for index in range(11, 0, -1):
  print((" " * index) + favEmoji * (9 - index ))
  