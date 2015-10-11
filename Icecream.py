__author__ = 'rfischer'


T = input()
for i in range(0, T):
    M = input()
    N = input()
    cost = [int(n) for n in raw_input().split(' ')]

    sc = set(cost)

    ic = 0
    icp = 0

    for c in sc:
        if M-c in sc:
            # Special case where the total is twice the current value
            if c == M-c:
                # Make sure there are at least two of the current values...
                if cost.count(c) > 1:
                    ic = cost.index(c)
                    # Nuke the first occurrence and get the next
                    cost[ic] = -1
                    icp = cost.index(M-c)
                    break
            else:
                ic = cost.index(c)
                icp = cost.index(M-c)
                break


    if ic < icp:
        print str(ic+1) + " " + str(icp+1)
    else:
        print str(icp+1) + " " + str(ic+1)
