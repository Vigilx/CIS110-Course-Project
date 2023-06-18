print(f"Hello there, I want to tell you about a story about a dog. I can't say any more. ")
print(f"Before I tell you the story, I have to ask you some questions. ")
print(f"Please make sure to anwser the questions and to hit enter. ")
input(f"\nPress The ENTER key to continue...")

keepGoing = "y"
while keepGoing.lower() == "y":

#First Question
    home = input("\Should Osiris go home or go look? ")
    while len(home) == 0:
        home = input(f"Please enter a choice: ")
    #Second Question
    age = input("\nHow old are you?:  ")
    while len(age) == 0:
        age = input(f"please enter age: ")
    #Third Question
    city = input(f"What city were you born in?:  ")
    while len(city) == 0:
        city = input(f"Please enter city: ")
    #Fourth Question
    speed = input(f"Should Osiris run or walk?:  ")
    while len(speed) == 0:
        speed = input(f"Please enter choice: ")
    #Fifth Question
    route = input(f"Should osiris take the short or long way home?:  ")
    while len(route) == 0:
        route = input(f"Please enter choice: ")
    #Sixth Question:
    snack = input(f"nWhat is your favorite snack?:  ")
    while len(snack) == 0:
        snack = input(f"Please enter favorite snack: ")

 
    print(f"\nAlright lets get this story started.")
    print(f"\nThere was once a black lab named Osiris that live in the city of {city} along with his owner.")
    print(f"\nOsiris loves going outside and just exploring the city of {city}. ")
    print(f"\nOne day during {city} summer days, Osiris parent's decide that they wanted to go out to explore the town. So they left poor little Osiris at home. ")
    print(f"\nOsiris is a well behaved dog for the most part so the parent didn't feel the need to put osiris in his crate today. ")
    print(f"\nOsiris was bored being left at home alone with nothing to do, no toys to chew or treats to find. He began to pace back and forth until he noticed the back door was left open, without any thinking he ran out that door so fast. ")
    print(f"\nOnce outside Osiris began to rethink his choice, but he knew this would never happen again so he continued forward .")
    print(f"\nOnce outside, Osiris began to {speed} towards his favorite spot... the Park. ")
    print(f"\nAfter {age} mintues, Osiris decided it was time to head home. ")

    #Decision1 
    route = input(f"\n Should Osiris take the long route or short route back home? Type short or long: ")
    if route == "short":
        print(f"\nOsiris decides he wants to take the short route home, he doesn't want to arrive all tired back home. ")
        print(f"\nOn his way home Osiris finds {age} pieces of {snack} just sitting on the street floor. Just sitting there calling for his name ")
        print(f"\nJust his luck, Osiris thought to himself if he went the long way would of he found these {age} {snack} ! ")

    else:
        print(f"\nOsiris decides to take the long way home, as he doesn't want to go home just yet. ")
        print(f"\nOn his way home, he enjoys the views of the city and tired from a long day")

    #Decision2
    home == input(f"\nOsiris arrives back home, but on he's block he spots a group of dogs standing in a group togeher. Should Osiris go over and check it out or just go back inside? type go look or go home:  ")
    while home.lower() !="go look" and home.lower() != "go home":
        home = input(f"Please type go look or go home: ")

    #Alternate Endings

    if home == "go look":
        print(f"\nOSiris curiosity won the best of him so he decides to go check out the group of dogs to see what is happening. ")
        print(f"As osiris gets closer he notices that he can see a pile of {snack} and everyone was sharing")
        print(f"He filled up his belly and went home before his owners ever noticed he was gone")
    else:
        print(f"Osiris decides to go home and enjoy the rest of his evening resting in his bed.")


    print(f"\nThe END ")

keepGoing = input("Do you want hear the story again? yes or no:  ")
while keepGoing.lower() not in ["yes", "no"]:
    keepGoing = input("Invaild Value: please enter yes or no:  ")
