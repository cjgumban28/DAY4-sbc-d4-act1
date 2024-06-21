from random import randint


choices = ["Fold", "Unfold"]
com1 = choices[randint(0, 1)]
com2 = choices[randint(0, 1)]


user = input("Choose Fold or Unfold >").capitalize()
p1 = "Fold" if user == "Fold" else "Unfold"


print(f"Player 1 = {p1}")
print(f"Computer 1 = {com1}")
print(f"Computer 2 = {com2}")


if (p1 == "Fold" and com1 == "Unfold" and com2 == "Unfold") or (p1 == "Unfold" and com1 == "Fold" and com2 == "Fold"):
    print("Player 1 Win!!!!")
elif (p1 == "Unfold" and com1 == "Fold" and com2 == "Unfold") or (p1 == "Fold" and com1 == "Unfold" and com2 == "Fold"):
    print("Computer 1 Win!!!!")
elif (p1 == "Unfold" and com1 == "Unfold" and com2 == "Fold") or (p1 == "Fold" and com1 == "Fold" and com2 == "Unfold"):
    print("Computer 2 Win!!!!")
else:
    print("No one wins.")
