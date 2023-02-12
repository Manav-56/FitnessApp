def interpret_dsl(filename):
    track = {
        "calorie": [],
        "protein": [],
        "fat": [],
        "sugar": [],
    }

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "" or line[0] == "~":
                continue
            lines = line.split()

            if lines[0] == "Total":
                print(
                    "Total Number of "
                    + str(sum(track[lines[3]]))
                    + " "
                    + lines[3]
                    + " consume."
                )
            else:
                track[lines[1]].append(int(lines[0]))


interpret_dsl("fitness.dsl")
