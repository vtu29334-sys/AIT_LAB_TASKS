import random

# Jobs defined as (Job ID, Processing Time, Due Date)
jobs = [(1, 4, 6), (2, 7, 10), (3, 2, 5), (4, 5, 12), (5, 3, 8)]

def evaluate(seq):
    time, tardiness = 0, 0
    for job_id, p_time, due in seq:
        time += p_time
        tardiness += max(0, time - due)
    return time, tardiness

def fitness(seq):
    makespan, tardiness = evaluate(seq)
    return 1 / (1 + makespan + tardiness)

# Initialize population
pop = [random.sample(jobs, len(jobs)) for _ in range(10)]

# Genetic Algorithm Loop
for _ in range(50):
    pop.sort(key=fitness, reverse=True)
    parents = pop[:5]  # Select top 5
    next_gen = parents.copy()
    
    # Generate offspring via swap mutation
    for child in parents:
        c = child.copy()
        i, j = random.sample(range(len(c)), 2)
        c[i], c[j] = c[j], c[i]
        next_gen.append(c)
        
    pop = next_gen

best_seq = pop[0]
makespan, tardiness = evaluate(best_seq)

print("Optimal Job Order:", [job[0] for job in best_seq])
print("Makespan (Total Time):", makespan)
print("Total Tardiness:", tardiness)
