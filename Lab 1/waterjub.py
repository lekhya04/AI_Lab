def successors(state):
    x,y=state
    pour_x_to_y = min(x,3-y)
    pour_y_to_x = min(4-x,y)
    return [(4,y),(x,3),(0,y),(x,0),
            (x-pour_x_to_y,y+pour_x_to_y),
            (x+pour_y_to_x,y-pour_y_to_x)]
start = (0,0)
seen = {start}
frontier = [start]
level = 0
while frontier and level < 8:
    new = []
    for s in frontier:
        for ns in successors(s):
            if ns not in seen:
                seen.add(ns)
                new.append(ns)
                if ns[0] == 2:
                    print("GOAL: 2L in X at level", level+1)
    level += 1 
    print("Level", level, "->", len(new), "new states:", sorted(new))
    frontier = new         
print("Total states found:", len(seen))
