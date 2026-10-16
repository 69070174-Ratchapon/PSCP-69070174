"""padthai"""
required_ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}
required_tastes = {"Sweet", "Sour", "Salty"}

ingredients = set()
while True:
    item = input()
    if item == "Cook":
        break
    ingredients.add(item)

tastes = set()
while True:
    taste = input()
    if taste == "End":
        break
    tastes.add(taste)

if ingredients - required_ingredients:
    print("This is not Pad Thai!!!")
elif ingredients != required_ingredients:
    print("This is bad!")
elif tastes != required_tastes:
    print("Not Bad...")
else:
    print("Delicious!")
