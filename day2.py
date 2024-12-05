def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    arr = [row.split(" ") for row in arr] 

    return arr

def get_diffs(input): 
    n = len(input)
    diffs = []
    for i in range(1, n):
        diffs.append(int(input[i]) - int(input[i-1]))
    return diffs

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

def part_one(input):
    safe = 0
    for report in input:
        diffs = get_diffs(report)
        # print(report, diffs, has_correct_gaps(diffs))
        if has_correct_gaps(diffs):
            safe += 1
    return safe 

def part_two(input):
    safe = 0
    for report in input:
        diffs = get_diffs(report)
        if has_correct_gaps(diffs): 
            safe += 1
            # print('original', report, has_correct_gaps(diffs))
        else:
            # print('original', report, has_correct_gaps(diffs))
            # adjust report to remove each element and then retest
            for _ in report:
                report_copy = report.copy()
                report_copy = [x for x in report_copy if x != _]
                new_diffs = get_diffs(report_copy)
                if has_correct_gaps(new_diffs):
                    # print('adjusted', report_copy, has_correct_gaps(diffs)) 
                    safe += 1
                    break 
    return safe 
    

def main():
    f = "inputs//day2.txt"
    data = parse_input(f)
    # data = data[20:50]
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

    
    # print(part_one(data))
    # print(part_two(data))

    lst = [1,1,4,6,7]
    n = len(lst)
    for i in range(n):
        lst_copy = lst.copy() 
        lst_copy = [x for x in lst_copy[:i]] + [y for y in lst_copy[i+1:]]
        print(lst_copy)


if __name__ == "__main__":
    main()