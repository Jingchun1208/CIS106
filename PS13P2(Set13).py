class student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()  
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250.00  
        else:
            rate = 500.00 
        self.tuition = self.enrolled_credits * rate
        return self.tuition

    def display_student_info(self):
        print(f"Student Name: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Enrolled Credits: {self.enrolled_credits}")
        print(f"Tuition Owed: ${self.compute_tuition()}\n") 

student_1=student('Emma','Smith','I',15)
student_2=student('Olivia','Brown','O',20)
student_3=student('James','Miller','I',10)

print(f"{student_1.first_name} {student_1.last_name}, {student_1.district_code}, {student_1.enrolled_credits} credits, Tuition: ${student_1.compute_tuition()}")
print(f"{student_2.first_name} {student_2.last_name}, {student_2.district_code}, {student_2.enrolled_credits} credits, Tuition: ${student_2.compute_tuition()}")
print(f"{student_3.first_name} {student_3.last_name}, {student_3.district_code}, {student_3.enrolled_credits} credits, Tuition: ${student_3.compute_tuition()}")
