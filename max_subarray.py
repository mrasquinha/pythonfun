num_tests = int(input())

for test in range(num_tests):
    num_elements = int(input())
    elements = list(map(int, input().split()))

    max_so_far = elements[0]
    max_ending_here = 0

    for i in range(num_elements):
        if (max_ending_here < 0 and elements[i]>0):
            max_ending_here = 0
        max_ending_here += elements[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    #non-contiguous
    mask = (1<<num_elements) - 1
    max_subsum = elements[0]
    while (mask !=0):
        sub_seq_mask = mask
        itr = 0
        sum_this_mask = 0
        while(itr < num_elements):
            if(sub_seq_mask>>itr&1):
                sum_this_mask += elements[itr]
            itr += 1
        mask -= 1
        if(max_subsum < sum_this_mask):
            max_subsum = sum_this_mask

    print (max_so_far, max_subsum)

