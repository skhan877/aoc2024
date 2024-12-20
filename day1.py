def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    # return arr
    arr_A = [a.split("   ")[0] for a in arr]
    arr_B = [a.split("   ")[1] for a in arr]

    return arr_A, arr_B


def part_one(input):

    arr_A, arr_B = input

    arr_A = sorted(arr_A)
    arr_B = sorted(arr_B)
    n = len(arr_A)

    diffs = [abs(int(arr_A[i]) - int(arr_B[i])) for i in range(n)]

    return sum(diffs)


def part_two(input):

    arr_A, arr_B = input 

    arr_A = sorted(arr_A)
    arr_B = sorted(arr_B)
    n = len(arr_A)

    B_counts = {} 
    for x in arr_B:
        if x not in B_counts:
            B_counts[x] = 1
        else:
            B_counts[x] += 1
    
    score = 0 

    for y in arr_A:
        if y in B_counts:
            score += (int(y) * B_counts[y])

    return score 
    

def main():
    f = "inputs//day1.txt"
    data = parse_input(f)
    # data = data[:20]
    # print(data)

    sample = []

    # print(part_one(data))
    print(part_two(data))



if __name__ == "__main__":
    main()