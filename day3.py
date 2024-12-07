def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    # arr = [row.split(" ") for row in arr] 

    return arr

def product(a, b):
    return a * b 

def extract_muls(input): 
    lst = input[0].split(")")
    lst = [x+")" for x in lst if "mul" in x]
    lst = [x[x.find("mul("): ] for x in lst]
    for instr in lst:
        n = len(instr) 


    #     print(instr, idx)
    return lst 

def part_one(input):
    lst = extract_muls(input)
    return lst 

def part_two(input):
    pass

def main():
    f = "inputs//day3.txt"
    data = parse_input(f)
    # data = data[20:50]
    # print(data)
    # print(" ")

    sample = [
        ]

    # sample = [row.split(" ") for row in sample] 
    # print(sample)

    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()