import ast
from ProfChoices import choose_prof
from Fight import choose_enemy, begin_fight

def greeting():
    player_name = input("Greetings, traveller. What is your name?\n")
    savedata["Name"] = player_name
    choose_prof(savedata)


f = open('savefile', 'r')
read_file = f.read()
f.close()
savedata = ast.literal_eval(read_file)
print(savedata)
greeting()
print(savedata)
sds = str(savedata)
nf = open('savefile', 'w')
nf.write(sds)
nf.close()
enemy = choose_enemy()
begin_fight(savedata, enemy)

