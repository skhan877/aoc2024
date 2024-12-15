def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))
    return arr

def product(a, b):
    return a * b 

def extract_muls(input): 
    lst = input[0].split(")")
    lst = [x+")" for x in lst if "mul" in x]
    lst = [x[x.find("mul("): ] for x in lst]
    ans = 0 

    for instr in lst[90:100]:
        n = len(instr)
        # stack = [] 
        print(instr) 
        i, j = 0, 3
        if instr[i:j+1] != "mul(":
            continue 
        else:
            i, j = 4, 4
            # print(instr, instr[j])
            # while instr[j] != ")":
            while j - i < 7:
                if instr[j] == "(":
                    break 
                elif instr[j] != ")":
                    j += 1
                else:
                    print("else: ", i, j, j-i)
                    i = j
                    j += 1
            nums = instr[i:j].split(",")
            if isinstance(int(nums[0]), int) and isinstance(int(nums[1]), int):
                prod = int(nums[0]) * int(nums[1])
                ans += prod
        print(instr, i, j, j-i, nums, ans)



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