def compure_scores(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score

last_name = input("Enter last name:")
score1 = float(input("Enter score 1:"))
score2 = float(input("Enter score 2:"))
score3 = float(input("Enter score 3:"))
total_points,average_score = compure_scores(score1, score2, score3)

print("Last name: ", last_name)
print("Total points: ", total_points)
print("Average exam score: ", average_score)
