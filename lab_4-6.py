
beast = input("Enter an animal: ").lower()
dish = input("Enter a dish: ").lower()


beast = beast.replace("-", "").replace(" ", "")
dish = dish.replace("-", "").replace(" ", "")


is_allowed = dish[0] == dish[-1] == beast[0]

if is_allowed:
    print("True - The beast is allowed to bring the dish to the feast.")
else:
    print("False - The beast is not allowed to bring the dish to the feast.")
