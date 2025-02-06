def convert_str_to_graph(line):
    graph = {}
    i = 0
    line = line.split()
    bug = False

    for e in range(0, len(line), 2):
        for u in range(1,len(line), 2):
            if line[e] == '0':
                break

            if line[e] == line[u]:
                bug = False
                break
            else:
                bug = True
    
        if bug == True:
            return 'Error'

    if len(line) % 2 != 0:
        return 'Error'
    elif len(line) == 0:
        return 'Error'
    
    for e in line:
        if e != ' ' and e != '0' and e != '1' and e != '2' and e != '3' and e != '4' and e != '5' and e != '6' and e != '7' and e != '8' and e != '9':
            return 'Error'

    while i < len(line):

        if int(line[i]) not in graph:
            graph[int(line[i])] = [int(line[i+1])]
        else:
            graph[int(line[i])].append(int(line[i+1]))

        if int(line[i+1]) not in graph:
            graph[int(line[i+1])] = []           

        i += 2

    return graph