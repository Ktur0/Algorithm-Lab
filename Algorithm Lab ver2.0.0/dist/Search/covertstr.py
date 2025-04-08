def convert_str_to_graph(line):
    graph = {}
    line1 = line.split(',')
    line = []
    for i in line1:
        line2 = i.split(' ')
        for e in line2:
            line.append(e)
    while '' in line:
        line.remove('')
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
    
    for u in line:
        for e in u: 
            if e != ' ' and e != '0' and e != '1' and e != '2' and e != '3' and e != '4' and e != '5' and e != '6' and e != '7' and e != '8' and e != '9':
                return 'Error'

    i = 0
    
    while i < len(line):

        if int(line[i]) not in graph:
            graph[int(line[i])] = [int(line[i+1])]
        else:
            graph[int(line[i])].append(int(line[i+1]))

        if int(line[i+1]) not in graph:
            graph[int(line[i+1])] = []           

        i += 2

    return graph