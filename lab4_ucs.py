graph = {
    "S": [("A",1), ("B",4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
frontier = [("S", 0, ["S"])]
expanded = []
while len(frontier) > 0:
    best = 0
    for i in range(1, len(frontier)):
        if frontier[i][1] < frontier[best][1]:
            best = i
    node, cost, path = frontier.pop(best)
    if node == "G":
                print("path:", path)
                print("cost:", cost)
                print("processed nodes:", expanded + ["G"])
                print("Expansion count:", len(expanded))
                break
    expanded.append(node)
    for next_node, edge_cost in graph[node]:
                new_cost = cost + edge_cost
                new_path = path + [next_node]
                frontier.append((next_node, new_cost, new_path))
              

   
