def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr

def part_one(input):

    n = len(input)
    diffs = []
    for i in range(1, n):
        diffs.append(int(input[i]) - int(input[i-1]))

    def is_unidirectional(diffs):

        if '0' in diffs:
            return False 
        
        else:

            first_diff = diffs[0]

            if first_diff > 0:
                # increasing series 
                for i in range(1, range(len(diffs))):
                    if diffs[i] <= 0:
                        return False 
            else:
                # decreasing series
                for i in range(1, range(len(diffs))):
                    if diffs[i] >= 0:
                        return False 
                    
        return True  


    def has_correct_gaps(diffs):
        
        result = True

        for diff in diffs:
            if diff < 1 or diff > 3:
                result = False 
        
        return result


def part_two(input):

    pass
    

def main():
    f = "inputs//day2.txt"
    data = parse_input(f)
    data = data[:20]
    print(data)

    sample = [
        '7 6 4 2 1',
        '1 2 7 8 9',
        '9 7 6 2 1',
        '1 3 2 4 5',
        '8 6 4 4 1',
        '1 3 6 7 9'
        ]

    # print(part_one(data))
    # print(part_two(data))



if __name__ == "__main__":
    main()