def vertexation(rings):

    vertex_list = []
    for edge in rings:
        vertex_list += edge
    return list(set(vertex_list))

def filling(rings):
    vertices = vertexation(rings)
    connections = dict.fromkeys(vertices,[])
    rings = list(rings)

    for edge in range(len(rings)):
        rings[edge] = list(rings[edge])

    for vertex in range(1,len(connections)+1):
         for edge in rings:
             if vertex in edge:
                 connections[vertex] = connections.get(vertex) + edge

    for connection in range(1,len(connections)+1):
        connections[connection] = list(set(connections[connection]))
        if connection in connections[connection]: connections[connection].remove(connection)


    return connections

def break_rings(rings):

    connections = filling(rings)

    initial_number = len(connections)
    max_connection_number = 1
    while max_connection_number>0:

        max_connection_number = 0
        max_connection_ring = 0

        for connection in connections:
            if len(connections[connection])>max_connection_number:
                max_connection_number = len(connections[connection])
                max_connection_ring = connection

        for connection in connections:
            if max_connection_ring in connections[connection]: connections[connection].remove(max_connection_ring)

        if max_connection_ring !=0:
            connections.pop(max_connection_ring)

    diff = initial_number - len(connections)
    print('Broken:', diff)

    return diff


break_rings(({8,7},{1,9},{2,7},{3,6},{1,7},{5,7},{3,4},{9,5},{9,6},{3,5},))
break_rings(({3,4},{1,6},{1,2},{9,5},{2,5},{9,2},{8,3},{2,4},{8,4},{1,3},{8,1},{1,7},{6,7},))
break_rings(({5,7},{9,4},{1,2},{9,5},{1,3},{9,3},{9,6},{1,5},{2,3},{3,7},{9,7},{8,6},{3,4},))
break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7},))
break_rings(({1,3},{3,4},{3,5},{4,6},{6,7},{8,3},{8,1},{2,6},{8,4},{9,5},{4,5},{1,7},))
break_rings(({9,5},{5,6},{2,6},{4,5},{8,2},{1,3},{1,4},{9,4},{1,2},{9,2},{8,7},{8,3},{8,6},{2,3},{8,9},))
break_rings(({9,7},{9,6},{8,5},{8,3},{8,9},{5,7},{4,5},{8,4},{1,7},{9,4},{1,5},{2,5},{4,6},{8,2},{1,2},{2,4},{8,7},{8,1},))
break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},))
break_rings(({2,5},{3,7},{5,6},{6,7},{9,6},{8,9},{9,7},{1,4},{1,9},{9,5},{2,4},{2,6},{2,3},{9,2},{3,6},{4,5},{1,2},))
break_rings(({1,4},{4,7},{9,3},{8,2},{4,6},{3,4},{2,3},{8,9},{5,7},{9,5},))
break_rings(({1,3},{8,4},{4,6},{3,7},{8,2},{1,2},{8,9},{4,5},{8,1},{1,9},{1,7},{1,6},{2,5},{9,6},{2,4},{9,2},))
break_rings(({9,7},{9,4},{9,3},{2,6},{2,5},{3,7},{4,6},{1,3},{1,4},{8,9},{3,5},{5,7},))
break_rings(({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},{10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},))
break_rings(({1,4},{4,7},{9,2},{2,6},{5,6},{8,1},{3,7},{9,3},{3,6},{8,6},{1,7},{2,4},{1,9},{8,3},{9,6},))
break_rings(({1,2},{3,7},{2,3},{3,5},{1,4},{2,5},{9,3},{5,7},{1,9},{8,4},{1,3},{2,6},{9,4},))
break_rings(({4,6},{2,5},{1,6},{6,7},{2,6},{8,7},{2,4},{4,7},{9,3},{3,7},{8,3},{2,7},{9,6},{4,5},))
break_rings(({11,7},{10,5},{4,6},{3,4},{19,14},{1,17},{8,4},{18,3},{17,12},{16,11},{9,11},{2,6},{11,4},{17,3},{13,6},{11,20},{11,15},{8,3},{5,7},))
break_rings(({4,6},{4,12},{2,4},{12,5},{12,14},{12,7},{9,13},{1,10},{9,18},{17,19},{4,13},{2,20},{10,14},{11,12},{11,15},{16,2},{8,5},{3,12},{17,11},{10,19},))
break_rings(({1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{8,7},{8,9},{9,1},))
break_rings(({1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{8,7},{8,9},{9,7},{10,4},{10,11},{11,12},{12,13},{12,14},))
break_rings(({1,2},{1,3},{1,5},{2,3},{2,4},{4,6},{5,6},))
