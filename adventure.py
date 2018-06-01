print "You are walking down a hallway. You get to the end. There is a door."
print "Do you 1. Open the door or 2. Walk away?"

door = raw_input("> ")

if door == "1":
    print "You open the door. You see a book on the table."
    print "1. You walk into the room and pick up the book."
    print "2. You turn around and walk away."

    book = raw_input("> ")

    if book == "1":
        print "The cover is black leather. It looks old. Voices are whispering."
        print "1. You open the book."
        print "2. You put the book down."

        up = raw_input("> ")

        if up == "1":
            print "The book contains the secret to immortal life."
            print "1. You take the book."
            print "2. You get the hell out and leave the book."

            immortal = raw_input("> ")

            if immortal == "1":
                print "You are on your way out with the book when you trip."
                print "You fall and the book falls out of your hands."
                print "You hear evil laughing and footsteps approaching."
                print "1. You leave the book and run away."
                print "2. You pause to pick up the book before you run."

                life = raw_input("> ")

                if life == "1":
                    print "You get away alive, and go home."
                    print "You remember the secret to immortal life."
                    print "You live longly and happily."
                    print "Longly is not a word but you get the idea."
                elif life == "2":
                    print "You almost get away, but something grabs your foot."
                    print "The monster that guards the book kills you."
                else:
                    print "You failed at following simple instructions."
                    print "Good job."
            elif immortal == "2":
                print "You go home and never accomplish anything."
                print "You die sad and alone and wish you'd taken the book."
            else:
                print "Seriously? 1 or 2 man, it's not difficult."
        elif up == "2":
            print "You wonder whether you should open the book anyway."
            print "1. Open the book."
            print "2. Leave the book."

            leave = raw_input("> ")

            if leave == "1":
                print "The book burns your eyes out."
                print "You stumble around in the maze for eternity, blind."
            elif leave == "2":
                print "You run away down the hallway. You hear a noise."
                print "1. You investigate."
                print "2. You keep running."

                running = raw_input("> ")

                if running == "1":
                    print "The noise is a monster that eats you."
                elif running == "2":
                    print "You make it out safely and go home."
                    print "Your little sister is missing."
                    print "You later find out she went looking for you."
                    print "She died in the tunnels."
                    print "The noise was her."
                else:
                    print "Dude you've gotta only write 1 or 2"
            else:
                print "You are really bad at following simple directions."
        else:
            print "Learn your numbers!"
    if book == "2":
        print "You get home safe. Someone else eventually finds the book."
        print "The book contained the cure for cancer."
        print "The other person is now rich and famous."
    else:
        print "Try again."
if door == "2":
    print "You spend the rest of your life haunted by what was behind that door."
    print "You can never find it again."
