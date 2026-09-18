def rock_paper_scissors():
    print("Rules:\n\n1. Rock defeats Scissors.\n2. Scissors defeats Paper.\n3. Paper defeats Rock.\n4. If both players choose the same option, the round ends in a draw.\n5. Choose finish when you want to stop playing.\n\nGood luck!!\n")

    p_score = 0
    ai_score = 0

    choice = {
        1: "Rock",
        2: "Scissors",
        3: "Paper",
        4: "Finish",
    }

    def win():
        if (p_choice == 1 and ai_choice == 2) or (p_choice == 2 and ai_choice == 3) or (p_choice == 3 and ai_choice == 1):
            print("You win!")
            return True
        else:
            return False

    def lose():
        if (ai_choice == 1 and p_choice == 2) or (ai_choice == 2 and p_choice == 3) or (ai_choice == 3 and p_choice == 1):
            print("You lose!")
            return True
        else:
            return False

    def draw():
        if p_choice == ai_choice:
            print("Draw!")
            return True
        else:
            return False


    while True:
        for k, v in choice.items():
            print(k, " - ", v)

        p_choice = int(input("\nChoose your option: "))

        if p_choice not in choice:

            print("Please choose a valid option.")
            continue

        else:

            print("You chose: ", choice[p_choice])
            if p_choice == 4:
                print(f"\nThank you for playing!\nHere is the end score: {p_score:.1f} : {ai_score:.1f}\n")
                if p_score == ai_score:
                    print("You finished in a draw!")
                elif p_score > ai_score:
                    print("You finished in a win!")
                elif p_score < ai_score:
                    print("You finished in a lose!")
                break
            ai_choice = random.choice(range(1, 4))
            print("\nAI chose: ", choice[ai_choice], "\n")

            if win():
                p_score += 1
            elif lose():
                ai_score += 1
            elif draw():
                p_score += 0.5
                ai_score += 0.5
            print(f"\nScore: {p_score:.1f} : {ai_score:.1f}\n")