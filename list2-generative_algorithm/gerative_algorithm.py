import numpy as np
import random

import sys
sys.setrecursionlimit(15000)
def generativ_algorthm(current_step, current_min=None, current_path=None, limit=10000, repet=0):
    if limit == 0 or repet == 500:
        return current_min, current_path
    
    
    keys = list(points.keys())
    values = []
    for row in current_step:
        sec = []
        for index in row:
            p = keys[index - 1]
            sec.append(points[p])
        values.append(sec)
    values = np.array(values)

    distances = []
    for sep_arr in values:
        distance = 0
        for n in range(6):
            p1, p2 = sep_arr[n], sep_arr[n + 1]
            distance += np.linalg.norm(np.array(p2) - np.array(p1))
        distances.append(distance)

    ord_arr = {dist: step for dist, step in zip(distances, current_step)}
    currently_min = min(distances)
    
    if current_min is None or currently_min < current_min:
        current_min, current_path = currently_min, ord_arr[currently_min]
        repet=0
        print("min value found:", current_min )
        print("best path:", current_path)
        
        print(current_step)
            
    if current_min <= 28:
        return current_min, current_path
    
    crossover_values = {}
    range_of_crossover = min(5, len(distances))
    sec_dist = distances.copy()
    
    while len(crossover_values) < range_of_crossover and sec_dist:
        min_value = min(sec_dist)
        index = distances.index(min_value)
        crossover_values[min_value] = index
        sec_dist.remove(min_value)
    
    if len(crossover_values) < 2:
        return current_min, current_path
    
    crossover_point = random.randint(1, 4)
    elements_cross = list(crossover_values.values())
    selected_sequences = [current_step[i] for i in elements_cross]
    
    if len(selected_sequences) % 2 != 0:
        selected_sequences.pop()
        elements_cross = elements_cross[:-1]
    
    
    
    
    new_steps = []
    for i in range(0, len(selected_sequences), 2):
        parent1, parent2 = selected_sequences[i], selected_sequences[i + 1]
        offspring1 = np.concatenate([parent1[:crossover_point], [g for g in parent2 if g not in parent1[:crossover_point]]])
        offspring2 = np.concatenate([parent2[:crossover_point], [g for g in parent1 if g not in parent2[:crossover_point]]])
        
        if len(offspring1) > 1:
            idx1, idx2 = random.sample(range(len(offspring1)), 2)
            offspring1[idx1], offspring1[idx2] = offspring1[idx2], offspring1[idx1]
            offspring2[idx1], offspring2[idx2] = offspring2[idx2], offspring2[idx1]
        
        new_steps.extend([offspring1, offspring2])
    
    num_to_remove = min(len(elements_cross), len(ord_arr))
    for _ in range(num_to_remove):
        if ord_arr:
            max_key = max(ord_arr.keys())
            ord_arr.pop(max_key)
    
    combined_steps = new_steps + list(ord_arr.values())
    steps = np.array(combined_steps, dtype=object)
    
    
    return generativ_algorthm(steps, current_min, current_path, limit-1, repet+1)

points = {
    "p1": [-2.750, -1.700, 0.100],
    "p2": [1.250, 4.899, 1.000],
    "p3": [0.180, 2.774, 2.550],
    "p4": [-2.750, 6.400, 0.100],
    "p5": [5.300, 6.375, 0.100],
    "p6": [0.250, 1.400, 0.100],
    "p7": [4.775, -1.525, 0.100],
}

steps = [random.sample(range(1, 8), 7) for _ in range(10)]
steps = np.array(steps)
best_result, best_path = generativ_algorthm(steps)
    
print("min value found:", best_result)
print("best path:", best_path)

for idx in best_path:
    target_pos = points[f"p{idx}"]
    print("steps:", target_pos)



