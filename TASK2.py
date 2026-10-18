# Hill Climbing for Exam Seating

def conflict(arr):
    score = 0
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) == 1:
            score += 1
    return score

seating = list(map(int, input("Enter seating arrangement: ").split()))

current = conflict(seating)

while True:
    improved = False
    for i in range(len(seating)):
        for j in range(i + 1, len(seating)):
            new = seating[:]
            new[i], new[j] = new[j], new[i]

            if conflict(new) < current:
                seating = new
                current = conflict(new)
                improved = True
                break
        if improved:
            break
    if not improved:
        break

print("Optimized Seating:", seating)
print("Conflict Score:", current)
