import numpy as np

def min_cut(adj):
    #print(str(adj))
    l0 = len(adj)
    s = np.random.randint(0,10000)
    np.random.seed(s)
    if l0 <= 2:
        ks = list(adj.keys())
        k = ks[0]
        mc = len(adj[k])
        return mc
    else:
        i_k = np.random.randint(0,l0)
        ks = list(adj.keys())
        k0 = ks[i_k]
        l1 = len(adj[k0])
        j_v = np.random.randint(0,l1)
        vs = adj[k0] 
        k1 = vs[j_v]
        #print('Contracting edge (' + k0 + ',' + k1 + ')') #contract randomly
        new_name = k0+k1
        new_value0 = adj.pop(k0)
        rename = lambda x: new_name if x == k1 or x == k0 else x
        new_value0 = [x for x in new_value0 if x != k0 and x != k1] #remove loops
        new_value1 = adj.pop(k1)
        new_value1 =  [x for x in new_value1 if x != k0 and x != k1]
        adj[new_name] = new_value0 + new_value1
        for (k,v) in adj.items(): #rename contracted edge
            adj[k] = list(map(rename,v))    
        return min_cut(adj) 


