from collections import deque

bomb_types = {
    40 : "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

bomb_produced = {
    "Cherry Bombs":0,
    "Datura Bombs":0,
    "Smoke Decoy Bombs":0
}


bomb_effects = [int(x) for x in input().split(", ")]
bomb_casings = [int(x) for x in input().split(", ")]

while bomb_effects and bomb_casings:
    result = bomb_effects[0] + bomb_casings[-1]
    if result in bomb_types:
        bomb_produced[bomb_types[result]] += 1
        del bomb_effects[0]
        del bomb_casings[-1]

    else:
        bomb_casings[-1] -= 5

    if bomb_produced[min(bomb_produced.keys(), key=(lambda k: bomb_produced[k]))] >=3:
        break

if bomb_produced[min(bomb_produced.keys(), key=(lambda k: bomb_produced[k]))] >=3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    # bomb_effects = bomb_effects[::-1]
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    bomb_casings = bomb_casings[::-1]
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for k in bomb_produced:
    print(f"{k}: {bomb_produced[k]}")

print("--------------------")
print(bomb_produced[min(bomb_produced.keys(), key=(lambda k: bomb_produced[k]))])
print(bomb_produced)
print(bomb_effects)
print(bomb_casings)
