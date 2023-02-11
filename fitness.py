def interpret_dsl(filename):
    Track = {"calorie": [],
               "protein": [],
               "fat": [],
                "sugar": [],
             }

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == '' or line[0] == '~':
                continue
            lines = line.split()

            if lines[0] == 'Total':
                print("Total Number of " + str(sum(Track[lines[3]])) + ' ' + lines[3] + ' consume.')
            else:
                Track[lines[1]].append(int(lines[0]))


interpret_dsl('fitness.dsl')