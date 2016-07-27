visitSet = set()
def visit(pool,dic,count):
    best = count;
    for p in dic[pool]:
        key = pool + (p * factor)
        if not key in visitSet:
            visitSet.add(key)        
            best = max(best,visit(p,dic,count+1))
    return best
    
with open('subtask1.input','r') as f:
    tests = int(f.readline());
    
    for t in range(1,tests+1):
        total = f.readline().strip()
        pools = int(total)
        factor = 10**len(total)
        
        start = int(f.readline());
        dic = {};
        for p in range(1,pools+1):
            dic[p]=[]
            info = f.readline().split();
            for i in range(1,int(info[0])+1):
                dic[p].append(int(info[i]))
        
        visitSet.clear()
        best = visit(start,dic,0)
        print 'Case #{}: {}'.format(str(t),str(best))
    
    
