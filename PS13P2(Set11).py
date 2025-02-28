last_name = ["Albert", "White", "Knight", "Dean", "Brown","George", "Jackson", "Smith", "Taylor", "Jacky"]

exam_scores = [100.0, 97.0, 95.0, 93.0, 91.0, 89.0, 87.0, 85.0, 83.0, 81.0]

def display_exam_scores(last_name, scores):  
    for x in range(0,10,1):  
        print(last_name[x], "scores", scores[x])

display_exam_scores(last_name, exam_scores)
