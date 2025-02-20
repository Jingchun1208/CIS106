def compute_average_scores (game_score1, game_score2, game_score3, handicap):
    total_score = game_score1 + game_score2 + game_score3
    average_scores = total_score / 3
    average_scores_with_handicap = average_scores + handicap
    return average_scores, average_scores_with_handicap

last_name = input("Enter last name:")
game_score1 = float(input("Enter game score 1:"))
game_score2 = float(input("Enter game score 2:"))
game_score3 = float(input("Enter game score 3:"))
handicap = float(input("Enter handicap:"))
average_scores, average_scores_with_handicap = compute_average_scores (game_score1, game_score2, game_score3, handicap)

print("Last name: ", last_name)
print("Average scores: ", average_scores)
print("Average scores with handicap: ", average_scores_with_handicap)
