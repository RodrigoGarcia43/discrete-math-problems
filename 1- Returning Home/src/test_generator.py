import random


def generator():
    for i in range(0, 10000):
        aux = "test" + str(i)
        f = open("tests/" + aux, "w")

        n = 4
        m = random.randint(1, 10)

        start_x, start_y = random.randint(1, 4), random.randint(1, 4)
        end_x, end_y = random.randint(1, 4), random.randint(1, 4)
        instant_positions = []

        for _ in range(0, m):
            new_pos = (random.randint(1, 4), random.randint(1, 4))
            if not new_pos in instant_positions:
                instant_positions.append(new_pos)

        m = len(instant_positions)

        print(n, file=f)
        print(m, file=f)
        print((start_x, start_y), file=f)
        print((end_x, end_y), file=f)
        print(instant_positions, file=f)

        f.close()


generator()
