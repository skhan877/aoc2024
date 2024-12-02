def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    arr = [row.split(" ") for row in arr] 

    return arr



def part_one(input):

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

    for report in input:
        n = len(report)
        diffs = []
        for i in range(1, n):
            diffs.append(int(report[i]) - int(report[i-1]))
        print(diffs)

    return 


def part_two(input):

    pass
    

def main():
    f = "inputs//day2.txt"
    data = parse_input(f)
    # data = data[:20]
    # print(data)

    sample = [
        '7 6 4 2 1',
        '1 2 7 8 9',
        '9 7 6 2 1',
        '1 3 2 4 5',
        '8 6 4 4 1',
        '1 3 6 7 9'
        ]

    sample = [row.split(" ") for row in sample] 
    # print(sample)

    
    print(part_one(sample))
    # print(part_two(data))



if __name__ == "__main__":
    main()