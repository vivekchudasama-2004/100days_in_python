################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
#only accessable inside the function
def drink():
  drink_portion = 3
  print(f"drink portion: {drink_portion}")
drink()

#globel scope
# accessable inside and outside the function
player_health = 100
def drink_portion():
  player=5
  print(f"player_health: {player_health}")

drink_portion()
player_health=50
print(f"player_health: {player_health}")