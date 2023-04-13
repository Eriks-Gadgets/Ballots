#Ballots!
#(c) Erik's Gadgets

print("Ballots! Event Log")

import PySimpleGUI as sg

sg.theme("LightBrown6")

sg.Popup("Ballots! [DEMO]\n(c) 2023 Erik's Gadgets")

import random

candidates = []

last_names = ["Smith", "Brown", "Jones", "William", "Becker", "Lucason", "Jamison", "Jameson", "Lewie"]

first_names = ["John", "Richard", "Henry", "Ron", "Ray", "Dave", "Luka", "Mary", "Ben"]


times = 3
time = 0

while time != times:
    rand_first_name = random.randint(0, len(first_names) - 1)
    rand_last_name = random.randint(0, len(last_names) - 1)
    curcandidate = ""
    curcandidate += first_names[rand_first_name]
    curcandidate += " "
    curcandidate += last_names[rand_last_name]
    del first_names[rand_first_name]
    del last_names[rand_last_name]
    print(last_names)
    print(first_names)
    print(rand_first_name)
    print(rand_last_name)
    candidates.append(curcandidate)
    time += 1

candidates.append(curcandidate)

radios = []

radiopos = -1

for i in candidates:
    radiopos += 1
    radios.append(sg.Radio(candidates[radiopos], "Candidate"))

del radios[-1]

ballots = sg.Window(title="Ballots! [DEMO]", layout=[[radios], [sg.Button("Submit")]])

while True:
    
    event, values = ballots.Read()
    
    print(values)
    print(event)
    if event == "Submit":
        for i in range(0, len(radios)):
            
            if values[i] == True:
            
                sg.Popup("You voted for: " + str(candidates[i]))
                if values[0] == True:
                    candidate = 0
                    candidate1_votes = 1
                    candidate2_votes = 0
                    candidate3_votes = 0
                if values[1] == True:
                    candidate = 1
                    candidate1_votes = 0
                    candidate2_votes = 1
                    candidate3_votes = 0
                if values[2] == True:
                    candidate1_votes = 0
                    candidate2_votes = 0
                    candidate3_votes = 1
                    candidate = 2
                ballots.close()
                candidate1 = candidates[0]
                candidate2 = candidates[1]
                candidate3 = candidates[2]
                voters = 455
                candidate1_votes += random.randint(0, voters)
                voters -= candidate1_votes
                candidate2_votes += random.randint(0, voters)
                voters -= candidate2_votes
                candidate3_votes += voters
                voted = [candidate1_votes, candidate2_votes, candidate3_votes]
                if max(voted) == candidate1_votes:
                    winner = 0
                elif max(voted) == candidate2_votes:
                    winner = 1
                else:
                    winner = 2
                categorized = {candidate1:candidate1_votes, candidate2:candidate2_votes, candidate3:candidate3_votes}
                sg.Popup("RESULTS:\n" + str(categorized) + "\n" + str(candidates[winner]) + " WON!")
                sg.Popup("You Voted: " + str(candidates[candidate]))
                if winner == candidate:
                    sg.Popup("Congratulations! Your Pick Won!\nHope you enjoy living under the new President!")
                break

    
    if event == sg.WIN_CLOSED:
       
        break

ballots.close()
