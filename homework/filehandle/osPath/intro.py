import os 

print("hozrgi: ", os.getcwd())

#os.chdir("../")

#print("keyingi: ", os.getcwd())


from pathlib import Path

base = Path()          # hozirgi papka
logs = base / "logs"   # ichidagi logs papka

logs.mkdir(exist_ok=True)

file = logs / "a.log"
file.write_text("hello")

print(file.exists())  # True