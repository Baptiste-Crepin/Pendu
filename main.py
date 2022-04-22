import random

all_words = open("HangedMan/mots.txt", "r").read().splitlines()
random_index = random.randint(0, len(all_words))
random_word = all_words[random_index]


class hanged_man():
    def __init__(self, result):
        self.result = result
        self.already_guessed = []
        self.mistakes = 0
        self.found = False


    def is_visible(self, char):
        for i in self.already_guessed:
            if i == char:
                return True
        return False


    def is_word(self, enter):
        if len(enter) == 1: return False
        return True

    
    def guess(self, enter):
        if self.is_word(enter):
            if enter == self.result:
                self.found = True
                return
            self.mistakes += 2
            return
        if enter not in self.already_guessed: 
            self.already_guessed.append(enter)
            if enter not in self.result:
                self.mistakes += 1
    

    def show_word(self):
        final_show = []
        for char in self.result:
            if len(self.already_guessed) == 0: 
                return print(["_" for i in range(len(self.result))])
            if self.is_visible(char):
                final_show.append(char)
            else:
                final_show.append("_")    
        if len(final_show) > 0 and "_" not in final_show:
            self.found = True
        print(final_show)


    def show_mistakes(self):
        if self.mistakes == 0:
            [print("\n") for i in range(7)]
            return
        if self.mistakes == 1:
            [print("\n") for i in range(6)]
            print("_____________\n")
            return
        if self.mistakes == 2:
            print ("\n")
            [print(" |\n") for i in range(5)]
            print("_|____________\n")
            return
        if self.mistakes == 3:
            print ("_____________\n")
            [print(" |\n") for i in range(5)]
            print("_|____________\n")
            return
        if self.mistakes == 4:
            print("_____________\n")
            print(" | /\n")
            print(" |/\n")
            [print(" |\n") for i in range(3)]
            print("_|____________\n")
            return
        if self.mistakes == 5:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/\n")
            [print(" |\n") for i in range(3)]
            print("_|____________\n")
            return
        if self.mistakes == 6:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/        O\n")
            [print(" |\n") for i in range(3)]
            print("_|____________\n")
            return
        if self.mistakes == 7:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/        O\n")
            print(" |         |\n")
            [print(" |\n") for i in range(2)]
            print("_|____________\n")
            return
        if self.mistakes == 8:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/        O\n")
            print(" |        -|-\n")
            [print(" |\n") for i in range(2)]
            print("_|____________\n")
            return
        if self.mistakes == 9:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/        O\n")
            print(" |        -|-\n")
            print(" |         /\\\n")
            print(" |\n")
            print("_|____________\n")
            return
        if self.mistakes == 10:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/        O\n")
            print(" |        -|-\n")
            print(" |         /\\\n")
            print(" |\n")
            print("_|____________\n")
            print(f"Vous etes mort, le mot etait '{self.result}' !\n")
            return





def main():
    word = hanged_man(random_word.upper())
    word.show_word()
    while not word.found and word.mistakes <10:
        word.guess(input("saisissez une lettre ou un mot:  ").upper())
        print("-"*50)
        word.show_mistakes()
        word.show_word()
        print(f"Vous avez déja essayé ces lettres :{word.already_guessed}")
        if word.found: print(f"Bravo, le resultat etait bien {word.result}")
        print("-"*50)



if __name__ == "__main__":
    main()