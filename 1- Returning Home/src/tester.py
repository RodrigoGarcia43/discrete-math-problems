from brute import analyze as brute
from optimal import analyze as optimal


def read_file_line(f):
    a = f.readline()
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("(", "")
    a = a.replace(")", "")
    a = a.replace(" ", "")
    a = a.split(",")
    a[len(a) - 1] = a[len(a) - 1].replace("\n", "")
    b = []
    for item in a:
        b.append(int(item))
    return b


test = "test"
count = 0
for i in range(0, 10000):
    aux = test + str(i)
    f = open("tests/" + aux, "r")
    n = read_file_line(f)[0]
    m = read_file_line(f)[0]
    start = read_file_line(f)
    start_x, start_y = start[0] - 1, start[1] - 1
    end = read_file_line(f)
    end_x, end_y = end[0] - 1, end[1] - 1
    temp = read_file_line(f)
    k = 0
    instant_positions = []
    while k < len(temp):
        instant_positions.append((temp[k] - 1, temp[k + 1] - 1))
        k += 2
    f.close()

    # you can test the following codes
    brute_sol = brute(n, start_x, start_y, (end_x, end_y), instant_positions)
    optimal_sol = optimal(n, m, start_x, start_y, (end_x, end_y), instant_positions)

    if not (brute_sol == optimal_sol):
        count += 1
        print("ERROR at " + aux)
        print("first SOLUTION = " + str(brute_sol))
        print("second SOLUTION = " + str(optimal_sol))

    else:
        print("SUCCES at " + aux)

print("Found " + str(count) + " errors")
