quicksort = lambda l : l if len(l)<=1 else quicksort([x for x in l[1:] if x < l[0]]) + [l[0]] + quicksort([x for x in l[1:] if x >= l[0]])
