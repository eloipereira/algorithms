import karger as k

def get_adj_list_from_file():
    g = open("kargerMinCut.txt", "r")
    adj_list = {}
    for line in g:
        x, *y = line.split()
        adj_list[x] = y
    g.close()
    return adj_list

def main():
    adj_list = get_adj_list_from_file()
    m = 500000
    minCut = len(adj_list)
    for i in range(0,m):
        c = k.min_cut(adj_list)
        if c < minCut:
            minCut = c
    print(c)
if __name__ == '__main__':
  main()
