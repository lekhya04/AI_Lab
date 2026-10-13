rooms = ["A", "B", "C"]
weights = {"A": 1, "B": 2, "C": 3}
total = sum(weights.values())
target = {r: weights[r] / total for r in rooms}
current = "A"      
samples = []       
trials = [("C", .80), ("A", .50), ("B", .60),
          ("A", .20), ("C", .70), ("B", .90),
          ("A", .40), ("C", .10), ("B", .50),
          ("A", .90), ("B", .30), ("C", .20)]
for step, (proposed, u) in enumerate(trials, 1):
    old_weight = weights[current]
    new_weight = weights[proposed]
    ratio = new_weight / old_weight
    alpha = min(1.0, ratio)
    if u < alpha:
        current = proposed            
    samples.append(current)
    print(step, "u=", u, "alpha=", round(alpha, 3),
          "room=", current)
counts = {r: samples.count(r) for r in rooms}
print("Counts:", counts)
print("Target probabilities:", target)