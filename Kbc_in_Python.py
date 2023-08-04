print("\nWelcome in kaun Banega crorepati !!! \n")

player_Name = input("Plzz Enter ur name : ")
print()

level = [1000, 3000, 5000, 10000, 30000, 50000, 100000]

Questions = [["Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
              "Virat Kohli", "Sunil Gavaskar", " VVS laxman", " Rahul Dravid", 4],

             ["Ranthambore, Sariska and Keoladeo Ghana are all names of what?",
                 "National Parks", "Goosebumps", "Mountains", "Rivers", 1],

             ["India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?",
                 "Hindi", "Punjabi", "Kannada", "Malayalam", 4],

             ["In terms of production, which of these is the largest train coach manufacturing unit in the world?",
                 "Integral Coach Factory, Bangalore", "Integral Coach Factory, Mumbai", " Integral Coach Factory, Chennai", "Integral Coach Factory, Kolkata", 3],

             ["In 2020, Louise Gluck won the Nobel Prize in which category?",
                 " Music", "Sports", "Literature", "Dance", 3],

             ["Which of the following companies was originally started as a loom manufacturing unit in 1909?",
                 "Suzuki", "CEAT", "Honda", "Mercedes", 1],

             ["Which state is the largest producer of sugarcane in India?",
              " Maharashtra", " Karnataka", "Madhya Pradesh", " Uttar Pradesh", 4]]

for i in range(0, len(Questions)):
    Q = Questions[i]
    print(f"Que. {i+1} for {level[i]} Rs")
    print(f"{Q[0]}")
    print(f"1. {Q[1]}"), print(f"2. {Q[2]}")
    print(f"3. {Q[3]}"), print(f"4. {Q[4]}")

    Ans = int(input("Enter your answer 1 to 4 or 0 for Exit : "))

    if (Ans == Q[5]):
        print(
            f"Correct Answer ! Congratulations {player_Name} You won {level[i]} Rs \n")
    elif (Ans == 0):
        print("You quit the game.")
        print(f"Congratulations {player_Name}. You won {level[i-1]} Rs \n")
        break
    else:
        print("Oops ! Wrong answer")

        if (i == 0):
            print("You will get only 0 Rs.")

        elif (i > 0 and i <= 3):
            print("You will get only 3000 Rs.")

        elif (i < 3 and i <= 6):
            print("You will get only 10000 Rs.")
        break
