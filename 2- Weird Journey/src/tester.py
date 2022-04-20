from brute import solve as brute
from optimal import solve as optimal
from solution_1 import solve as solution_1


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

    temp = read_file_line(f)
    k = 0
    edges = []
    while k < len(temp):
        edges.append((temp[k], temp[k + 1]))
        k += 2
    f.close()

    # you can test the following codes
    # warning: to test the brute_sol you most generate small cases
    # brute_sol = brute(n, m, edges)
    solution_1_sol = solution_1(n, m, edges)
    optimal_sol = optimal(n, m, edges)

    if not (solution_1_sol == optimal_sol):
        count += 1
        print("ERROR at " + aux)
        print("first SOLUTION = " + str(solution_1_sol))
        print("second SOLUTION = " + str(optimal_sol))

    else:
        print("SUCCES at " + aux)

print("Found " + str(count) + " errors")
