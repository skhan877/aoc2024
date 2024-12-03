def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    arr = [row.split(" ") for row in arr] 

    return arr



def part_one(input):

    def has_correct_gaps(diffs):
        
        result = True
        first_diff = diffs[0]
        n = len(diffs)

        if first_diff > 0:
            for i in range(n):
                if diffs[i] < 1 or diffs[i] > 3: 
                    result = False 
        
        elif first_diff < 0:
            for i in range(n):
                if diffs[i] > -1 or diffs[i] < -3: 
                    result = False 

        else:
            result = False
        
        return result

    safe = 0

    for report in input:
        n = len(report)
        diffs = []
        for i in range(1, n):
            diffs.append(int(report[i]) - int(report[i-1]))
        # print(report, diffs, has_correct_gaps(diffs))
        if has_correct_gaps(diffs):
            safe += 1

    return safe 


def part_two(input):

    pass
    

def main():
    f = "inputs//day2.txt"
    data = parse_input(f)
    # data = data[49:100]
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

    
    print(part_one(data))
    # print(part_two(data))



if __name__ == "__main__":
    main()