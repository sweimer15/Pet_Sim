# Pet directory to hold our pet's parameters
pet = {"Name": "", "Type": "", "Age": 0, "Hunger": 0, "Playfulness": 0, "Toys": []}

# Handle quiting the game
def quitSimulator():
    print("That's the end of thegame! Thank you for playing the pet simulator")

# Feed your pet using current supplies 
def feedPet():
    # Set the pet's hunger level to the decreased hunger
    newHunger = pet["Hunger"] - 10
    if newHunger < 0:
        newHunger = 0
    pet["Hunger"] = newHunger
    print("Fed your Pet! Hunger decreased by 10")

# Create a dictionary of pets and their associated toys that they can use
petToys = {"Cat": ["Scratching Post", "Toy Mouse", "Ball of Yarn"], "Dog": ["Chew Toy", "Stick", "Frisbee"], "Fish": ["Undersea Castle", "Fake Coral", "Buried Tresure"]
           , "Dragon": ["Play Castle", "Toy Princess", "Gold Coins"]}

# Get your pet a new toy 
def getToy():
    toyChoices = petToys[pet["Type"]]
    toyNum = -1
    while toyNum < 0 or toyNum >= len(petToys):
        print("Here are your toy choices: ")
        for i in range(len(toyChoices)):
            print(str(i) + ": " + toyChoices[i])

        toyNum = int(input("Please input your choice of pet toy: "))

# Get the chosen toy as a string 
    chosenToy = toyChoices[toyNum]

# Add it to teh list of toys
    pet["Toys"].append(chosenToy)
    print("Nice! you chose: " + chosenToy + " for " + pet["Name"] + ". Great Pick!")

# Play with the toys 
def playToys():
    print("Yay! Let's Play with our toys.")
    pet["Playfulness"] += 10

# Funciton to print the menu
def printMenu(menuOptions):
    print()
    print("Here is the current menu of options you have:")
    print("----------")

    # iterate through the menu options, printing out the key ment to be pressed, along with its corresponding text
    for key in menuOptions:
        print(key + "\t" + menuOptions[key]["text"])

    #print an additional newline character
    print()

#Print states about the pet
def printStats():
    print()
    print("Your " + pet["Type"] + " named " + pet["Name"] + " had a great time playing with you!")
    print(pet["Name"] + " is " + str(pet["Age"]) + " days old")
    print(pet["Name"] + " is currentlty at a hunger level of " + str(pet["Hunger"]) + " out of 100!")
    print("You have " + str(len(pet["Toys"])) + " toys! They are: ")
    for toy in pet["Toys"]:
        print(toy)
    print()

# Handle initializing our pet, with its food, thirst, fun level
def initPet(petToys):

    # Extract the possible pets into a list for easier references
    petOptions = list(petToys.keys())

    #initialize selectedPet in order to continue prompting forpets if choice given was't in the dictionary
    selectedPet = ""

    # Loop through pets
    while selectedPet not in petOptions:
        print("Your options of pets are: ")
        for option in petOptions:
            print(option)

        selectedPet = input("Please select one of these pets. Which one would you like? ")

        if selectedPet not in petOptions:
            print("Sorry! That wasn't ome of our options.")

    # Store pet type in dictionary
    pet["Type"] = selectedPet

    # Prompt and store pet name
    petName = input("Great! you've selected a pet, now please name your pet! ")
    pet["Name"] = petName

#Main loop that controls out program logic
def main():
    # Initialize our pet
    initPet(petToys)

    # Options in the menu and their corresponding function to invoke
    menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, "F": { "function": feedPet, "text": "Feed " + pet["Name"] + "!"}, "G": { "function": getToy, "text": "Get a toy for " + pet["Name"] + "!"}, "P": { "function": playToys, "text": "Play with " + pet["Name"]+ " and your toys!"} }

    # Enter main loop of the simulator 
    keepPlaying = True
    while keepPlaying:
        menuSelection = ""
        menuOptionsKeys = list(menuOptions.keys())

        while menuSelection not in menuOptionsKeys:
            # Print out the possible options
            printMenu(menuOptions)

            # Get the response, lowercase
            menuSelection = input("Which option will you select? ").upper()
            print()

        # Handle quitting from the simulator
        if menuSelection == "Q":
            keepPlaying = False

        # Invoke the function associated with the menu selection
        menuOptions[menuSelection]["function"]()

        # Increment pet variables 
        pet["Hunger"] += 3
        pet["Age"] += 1

        # Print stats after 
        printStats()

main()