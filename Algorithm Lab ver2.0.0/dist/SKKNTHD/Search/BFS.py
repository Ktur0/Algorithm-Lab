import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def hierarchy_pos(G, root=None, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    Xây dựng vị trí các nút để hiển thị dưới dạng cây.
    """
    pos = {}

    def _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter, pos, parent=None, parsed=[]):
        if root not in parsed:
            parsed.append(root)
            pos[root] = (xcenter, vert_loc)
            neighbors = list(G.neighbors(root))
            if parent is not None and parent in neighbors:
                neighbors.remove(parent)
            if len(neighbors) != 0:
                dx = width / len(neighbors)
                nextx = xcenter - width / 2 - dx / 2
                for neighbor in neighbors:
                    nextx += dx
                    pos = _hierarchy_pos(
                        G, neighbor, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, 
                        xcenter=nextx, pos=pos, parent=root, parsed=parsed
                    )
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter, pos)

def bfs_with_animation_tree(graph, start, speed=1.0):
    """
    Thực hiện BFS và vẽ từng bước minh họa dưới dạng cây.
    """
    # Khởi tạo đồ thị NetworkX
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Vị trí các đỉnh theo dạng cây
    pos = hierarchy_pos(G, root=start)

    # BFS
    visited = set()
    queue = deque([start])
    edges_visited = []

    plt.figure(figsize=(10, 8))
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    edges_visited.append((node, neighbor))
                    queue.append(neighbor)

            # Vẽ đồ thị tại bước hiện tại
            plt.clf()
            nx.draw(
                G, pos, with_labels=True, node_color="lightgray",
                node_size=3000, font_size=12, edge_color="gray"
            )
            
            # Tô màu các cạnh đã thăm
            nx.draw_networkx_edges(
                G, pos, edgelist=edges_visited, edge_color="blue", width=2.5
            )
            
            # Tô màu các nút đã thăm
            nx.draw_networkx_nodes(
                G, pos, nodelist=list(visited), node_color="skyblue", node_size=3000
            )
            
            plt.title("BFS Visualization (Tree Layout)", fontsize=16)
            plt.pause(speed)  # Tạm dừng để hiển thị chuyển động
    
    plt.show()


