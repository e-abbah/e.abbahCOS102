
info = ["Name    | ", "Age    | ", "Height    | ", "Score    | "]


name = ["NAME", "Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
age = ["AGE", "17", "16", "17", "18", "16", "18", "17", "20", "19", "17"]
height = ["HEIGHT", "5.5", "6.0", "5.4", "5.9", "5.6", "5.5", "6.1", "6.0", "5.7", "5.5"]
scores = ["SCORE", "80", "85", "70", "60", "76", "66", "87", "95", "50", "49"]

boys_name = ["NAME", "Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_age = ["AGE", "19", "16", "18", "17", "20", "19", "16", "18", "17", "19"]
boys_height = ["HEIGHT", "5.7", "5.9", "5.8", "6.1", "5.9", "5.5", "6.1", "5.4", "5.8", "5.7"]
boys_scores = ["SCORE", "74", "87", "75", "68", "66", "78", "87", "98", "54", "60"]

def teams(name, age, height, scores):
    for i in range(11):
     print(f"\t{name[i]}\t  |{age[i]} \t|{height[i]}\t |{scores[i]}")

print("          INFO ON GIRLS IN THE CLASS")
teams(name, age, height, scores)
print('')
print('')
print("          INFO ON BOYS IN THE CLASS")
teams(boys_name, boys_age, boys_height, boys_scores)