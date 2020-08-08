

def play():

    wood = 30
    day_no = 1
    cart = 0
    gold = 0
    workers = 0
    worker_hire_cost = 20




    print(' ')
    print("Start of gathering game")
    print(' ')


    def get_player_command():
        return input('Action: ')

    def gather_multiplayer():
        global w_gather
        w_gather = 5

        if cart - 1 == 0:
            w_gather = w_gather + 5

        if cart - 1 < 0:
            w_gather = w_gather + 0

        if cart - 1 > 0:
            if cart - 1 > workers:
                w_gather = w_gather + (workers + 1) * 5
            elif cart - 1 < workers:
                w_gather = cart * 5
            elif cart - 1 == workers:
                w_gather = (cart + 1) * 5

        return w_gather

    while True:
        print(5 * '****' + " " + " day " + str(day_no) + "  " + 5 * '****' )
        print("|| Wood count " + str(wood) + " || "
              + "Gold stash " + str(gold) + " ||"
              + "carts " + str(cart) + " || "
              + "workers " + str(workers) + " || ")
        print(12 * '****')
        print(12 * '----')
        print("To gather wood, write 'g'")
        print(12 * '----')
        print("to make a cart, write 'cart'")
        print(12 * '----')
        print("to sell wood, write 'sell'")
        print(12 * '----')
        print("to hire workers, write 'hire'")
        print(12 * '----')
        print("to quit, write 'q'")
        print(' ')
        action_input = get_player_command()



        if action_input == 'gather wood' or action_input == 'g':

            gather_multiplayer()
            print("you gather wood")

            print("Wood + " + str(w_gather))
            wood = wood + w_gather
            day_no = day_no + 1
        elif action_input == 'cart':
            print("if you have more than 1 cart, you need extra workers for each one. ")
            print("Otherwise they are no use")
            print(" ")
            if wood>= 50:
                print("Would you like maximum numbers of carts? y/n")
                action_input = get_player_command()

                if action_input == 'y':
                    max_carts = wood / 50

                    print("you made " + str(int(max_carts)) + " carts.")
                    wood = wood - int(max_carts) * 50
                    cart = cart + int(max_carts)

                elif action_input == 'n':
                    print("You made a one cart.")
                    wood = wood - 50
                    cart = cart + 1

            else:
                print("Not enough wood, you need 50.")

        if action_input == 'sell':
            print("do you want to sell all your wood? (y/n)")
            action_input = get_player_command()

            if action_input == 'y':
                print("You sold all your wood, but gained " + str(wood) + " gold.")
                gold = gold + wood
                wood = wood - wood

            elif action_input == 'n':
                print("enter the amount (full number)")
                action_input = get_player_command()
                amount_sold = int(action_input)
                gold = gold + amount_sold
                wood = wood - amount_sold
                print("you sold " + str(amount_sold) + " wood.")

        if action_input == 'hire':
            print("Would you like maximum numbers of workers? y/n")
            action_input = get_player_command()

            if action_input == 'y':
                max_workers = gold / worker_hire_cost

                print("you hired " + str(int(max_workers)) + " new workers.")
                gold = gold - int(max_workers) * worker_hire_cost
                workers = workers + int(max_workers)

            elif action_input == 'n':
                print("how many do you want to hire? (1 worker costs " + str(worker_hire_cost) + " gold) ")
                action_input = get_player_command()
                amount_hired = int(action_input)

                if gold / amount_hired >= 1.0:

                        print("you gained " + str(amount_hired) + " workers")
                        print("you paid "+ str(amount_hired * worker_hire_cost))
                        workers = workers + amount_hired
                        gold = gold - amount_hired * worker_hire_cost
                else:
                        print("can not do")
        if action_input == 'q':
            break

        if gold > 500:
            print("You are freaking reach!")
            print("You are freaking reach!")
            print("You are freaking reach!")

        else:
            pass

        if gold > 5000:
            print("holllllllyyyyyyyyy sh***********ttttt")
            print("holllllllyyyyyyyyy sh***********ttttt")
            print(5 * '****' + " " + "you won" + "  " + 5 * '****')
            print(5 * '****' + " " + " day " + str(day_no) + "  " + 5 * '****')
            print(5 * '****' + " " + "you won" + "  " + 5 * '****')
            print("holllllllyyyyyyyyy sh***********ttttt")
            print("holllllllyyyyyyyyy sh***********ttttt")
            print("play again? (y/n)")
            action_input = get_player_command()

            if action_input == 'y':

                wood = 30
                day_no = 1
                cart = 0
                gold = 0
                workers = 0
                worker_hire_cost = 20

            if action_input == 'n':
                break
play()
