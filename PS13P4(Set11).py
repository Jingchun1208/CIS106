f = open("Code/PS13P4(11).txt", "r")
playernames=[]
batting_average =[]
player=f.readline()
while player !="":
  playernames.append(str(player).rstrip("\n"))
  ba=float(f.readline())
  batting_average.append(ba)
  player=f.readline()
f.close()
l=len(playernames)

def display (player, batting_average):
  for z in playernames,batting_average:
    print(z)

def search(playernames,player,batting_average,playersearch):
  for y in range(0,9,1):
    if playernames[y] in playersearch:
      sindex=y
      print(playernames[sindex]," has a batting avg of ",batting_average[sindex])
display(player,batting_average)    

user_choice = input("Do you want to search for a player? (yes/no)")
while user_choice == "yes":
  playersearch=str(input("What player do you seek?"))
  search(playernames,player,batting_average,playersearch)
  
  user_choice = str(input("Do you want to search another player? ('Yes' or 'No')"))
  
