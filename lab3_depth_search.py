graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None
    cutoff_found = False
    for neighbor in graph[node]:
        if neighbor not in path:
            status, result = dls(
                neighbor, goal, limit - 1, path + [neighbor]
            )
            if status == "FOUND":
                return status, result
            if status == "CUTOFF":
                cutoff_found = True
    if cutoff_found:
        return "CUTOFF", None
    return "FAILURE", None
for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("Depth Limit:", limit)
    print("Status:", status)
    print("Path:", path if path else "None")

