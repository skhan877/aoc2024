def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    # arr = [row.split(" ") for row in arr] 

    return arr

def part_one(input):
    pass 

def part_two(input):
    pass

def main():
    f = "inputs//day3.txt"
    data = parse_input(f)
    # data = data[20:50]
    # print(data)

    sample = [
        ]

    # sample = [row.split(" ") for row in sample] 
    # print(sample)

    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()