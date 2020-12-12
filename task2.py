import pandas as pd


INPUT_FILE = "scores.csv"
GRADE_A = ("A", 4.0)
GRADE_B = ("B", 3.0)
GRADE_C = ("C", 2.0)
GRADE_D = ("D", 1.0)
GRADE_F = ("F", 0.0)


def grade_calculator(score):
    if not score or score > 100:
        raise Exception(f"Score must be between 0 & 100, incorrect score passed {score}")
    elif score >= 90:
        return GRADE_A
    elif 90 > score >= 80:
        return GRADE_B
    elif 80 > score >= 70:
        return GRADE_C
    elif 70 > score >= 60:
        return GRADE_D
    else:
        return GRADE_F


if __name__ == "__main__":
    try:
        csv_data = pd.read_csv(INPUT_FILE)
    except Exception as e:
        print(f"Exception raised when reading from {INPUT_FILE} with error {e}")
        raise 
    class_data_dict = csv_data.to_dict()
    subjects = list(class_data_dict["Unnamed: 0"].values())
    # Remove the subjects from the class_data_dict dictionary.
    class_data_dict.pop("Unnamed: 0")

    total_gpa = 0
    subject_count = len(subjects)
    student_names= class_data_dict.keys()
    for student in student_names:
        student_gpa = 0
        scores = class_data_dict[student]
        for index in range(subject_count):
            subject_gpa = grade_calculator(scores[index])
            #print(f"Grade for {student} in {subjects[index]} is {subject_gpa[0]}")
            student_gpa+= subject_gpa[1]
        print (f"{student} {student_gpa/subject_count:.2f}")
        total_gpa+=student_gpa/subject_count
    print()
    print (f"The class GPA is {total_gpa/len(student_names):.2f}")
