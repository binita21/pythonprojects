no_of_students=int(input("Enter no of students\n"))
subjects=['Maths','Science','Social','English','Computer']
# full_marks, pass_marks = 75,35
Total_marks_sub = 75*len(subjects)

def student_marks_analyzer():
    for i in range(1,no_of_students+1):
        maths,science,social,english,computer = map(float,input(f"Enter marks of student id {i} in each 5 subjects :").split())
        marks =maths,science,social,english,computer
        def sum_marks():
            sum=maths+science+social+english+computer
            return sum
        print(f"Total marks of student_id {i} is {sum_marks()}")
        total_marks_std = sum_marks()
        
        

        def average_marks():
            average_marks = total_marks_std/len(subjects)
            return average_marks
        print(f"Average marks of student_id {i} is {average_marks()}")
        average_marks()
        

        def calc_grade():
            percentage = round(total_marks_std*100/(Total_marks_sub))
            print(f"Percentage = {percentage}")
            
            if percentage >= 90:
                print("Congratulations! You got and A+ grade.")
            elif percentage >= 80:
                print("Congratulations! You got an A grade.")
            elif percentage >= 70:
                print("Congratulations! You got B+ grade.")
            elif percentage >= 60:
                print("Congratulations! You got B grade.")
            elif percentage >= 50:
                print("You got C grade and just passed")
            else:
                print("You failed (NG)!")
        calc_grade()


student_marks_analyzer()
        
    