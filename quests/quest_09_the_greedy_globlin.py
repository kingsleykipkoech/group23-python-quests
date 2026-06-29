gold = 27  # total  gold
friends = 4  # how many friends to share with

each_friend_gets = gold // friends   # divide equally
goblin_keeps = gold % friends     # what is left 

print("Each friend gets:", each_friend_gets)
print("The goblin keeps:", goblin_keeps)

