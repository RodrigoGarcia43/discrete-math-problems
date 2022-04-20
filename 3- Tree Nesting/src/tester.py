from brute import solve as brute

# from brute_optimized import solve as brute_optimized
from optimal import solve as optimal


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

    s_edges = []
    temp = read_file_line(f)
    k = 0

    while k < len(temp):
        s_edges.append((temp[k] - 1, temp[k + 1] - 1))
        k += 2

    m = read_file_line(f)[0]
    t_edges = []
    temp = read_file_line(f)
    k = 0

    while k < len(temp):
        t_edges.append((temp[k] - 1, temp[k + 1] - 1))
        k += 2

    f.close()

    # you can test the following codes
    brute_sol = brute(n, s_edges, m, t_edges)
    optimal_sol = optimal(n, s_edges, m, t_edges)

    if not (brute_sol == optimal_sol):
        count += 1
        print("ERROR at " + aux)
        print("first SOLUTION = " + str(brute_sol))
        print("second SOLUTION = " + str(optimal_sol))

    else:
        print("SUCCES at " + aux)

print("Found " + str(count) + " errors")
