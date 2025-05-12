from grid import Grid

def main():
    my_grid= Grid()
    my_grid.populate_grid()
    my_grid.print_grid()

    nb_cycle = 0


    while True:

        key_input = input('Press "n" to play th next cycle. \nPress "c" to stop \n')
        if key_input.lower() == "c":
            break
        if key_input.lower() == "n":
            cpt = 0
            nb_cycle += 1
            print(f"Cycle count: {nb_cycle}")
            return_value = True
            while cpt <= 100000 :
                my_grid.cycle()
                return_value = my_grid.print_population()
                print(f"Cycle: {cpt}")
                if return_value:
                    break
                cpt += 1
        
main()

