#Ballots!
#(c) Erik's Gadgets
try:
    print("Ballots! Event Log")

    import PySimpleGUI as sg

    sg.theme("LightBrown6")

    sg.Popup("Ballots! [DEMO]\n(c) 2023 Erik's Gadgets")

    import random

    candidates = []

    last_names = ["Smith", "Brown", "Jones", "William", "Becker", "Lucason", "Jamison", "Jameson", "Lewie", "Johnson", "Peters", "Barlo"]

    first_names = ["John", "Richard", "Henry", "Ron", "Ray", "Dave", "Luka", "Mary", "Ben", "Sophia", "Josh", "Frank"]

    no_of_candidates = sg.Window(title="Ballots!", layout=[[sg.Text("Number of Candidates")], [sg.Text("at least 1! no more than 12!")], [sg.Input(3), sg.Button("OK")],[sg.Text("Number of Voters!")], [sg.Text("at least (num_of_candidates) * 5! anything less is unstable!")], [sg.Input(300)]])

    while True:
        event, values = no_of_candidates.Read()
        if event == "OK" or event == sg.WIN_CLOSED:
            times = int(values[0])
            voters = int(values[1])
            break
        
    no_of_candidates.close()

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

    print(candidates)
    radios = []

    candidate_votes = {}

    radiopos = -1

    for i in candidates:
        radiopos += 1
        radios.append(sg.Radio(candidates[radiopos], "Candidate"))
        candidate_votes[str(radiopos + 1)] = 0


    ballots = sg.Window(title="Ballots! [DEMO]", layout=[[radios], [sg.Button("Submit")]])

    while True:
        
        event, values = ballots.Read()
        
        print(values)
        print(event)
        if event == "Submit":
            for i in range(0, len(radios)):
                
                if values[i] == True:
                
                    sg.Popup("You voted for: " + str(candidates[i]))
                    pos = -1
                    for i in values:
                        pos += 1
                        if values[pos] == True:
                            candidate = pos
                            candidate_votes[str(candidate + 1)] = 1
                    ballots.close()
                    candidates2 = []
                    pos = -1
                    for i in candidates:
                        pos += 1
                        candidates2.append(candidates[pos])
                    print(candidate_votes)
                    print(candidates)
                    pos = 0
                    for i in candidates2:
                        pos += 1
                        candidate_votes[str(pos)] += random.randint(0, voters)
                        voters -= candidate_votes[str(pos)]
                    print(candidate_votes)
                    print(candidates)
                    voted = []
                    pos = 0
                    for i in candidate_votes:
                        pos += 1
                        voted.append(candidate_votes[str(pos)])
                    print(candidate_votes)
                    print(candidates)
                    print(voted)
                    pos = 0
                    pos2 = -1
                    for i in candidate_votes:
                        pos += 1
                        pos2 += 1
                        if max(voted) == candidate_votes[str(pos)]:
                            winner = pos2
                    pos = -1
                    categorized = {}
                    for i in candidates:
                        pos += 1
                        print(candidates[pos])
                        categorized[candidates[pos]] = voted[pos]
                    sg.Popup("RESULTS:\n" + str(categorized) + "\n" + str(candidates[winner]) + " WON!")
                    sg.Popup("You Voted: " + str(candidates[candidate]))
                    if winner == candidate:
                        sg.Popup("Congratulations! Your Pick Won!\nHope you enjoy living under the new President!")
                    break

        
        if event == sg.WIN_CLOSED:
           
            break

    ballots.close()
except Exception as err:
    import PySimpleGUI as sg
    sg.Popup("FATAL ERROR!!!\n" + str(err))
    exit()

