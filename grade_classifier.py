student_info = []

def add_info():
    name = input("Enter your first name and last name: ")
    subject1_marks = input("Enter subject 1 marks: ")
    subject2_marks = input("Enter subject 2 marks: ")
    subject3_marks = input("Enter subject 3 marks: ")
    new_dict = {'name': f'{name}', 'subject1_marks': f'{subject1_marks}', 'subject2_marks': f'{subject2_marks}', 'subject3_marks': f'{subject3_marks}'}
    student_info.append(new_dict)

def calculate_average():
    marks = round(float(student_info[0]['subject1_marks']), 2) + round(float(student_info[0]['subject2_marks']), 2) + round(float(student_info[0]['subject3_marks']), 2)
    print(f'Average: {round((marks / 3), 2)}')
    
def display_results():
    name = str(student_info[0]['name'])
    print("=======================================")
    print(f"      RESULTS FOR {str(name).upper()}")
    print("=======================================")
    name = str(student_info[0]['name'])
    print(f'Name    : {name.upper()}')
    marks = round(float(student_info[0]['subject1_marks']), 2) + round(float(student_info[0]['subject2_marks']), 2) + round(float(student_info[0]['subject3_marks']), 2)
    average = f'{round((marks /3), 2)}'
    print(f'Average : {(average)} %')
    if average >= "80":
        name = str(student_info[0]['name'])
        print("Status  : PASS")
        print("Grade   : A")
        print(f'Comment(s): Excellent results {name.title()} 🎉')
        print("=====================================")
    elif average >= "70":
        name = str(student_info[0]['name'])
        print("Status  : PASS")
        print("Grade   : B")
        print(f'Comment(s): Nice work there {name.title()}!')
        print("=====================================")
    elif average >= "60":
        name = str(student_info[0]['name'])
        print("Status  : PASS")
        print("Grade   : C")
        print(f'Comment(s): Well done {name.title()}, there is still room for improveent')
        print("=====================================")
    elif average >= "50":
        name = str(student_info[0]['name'])
        print("Status  : PASS")
        print("Grade   : D")
        print(f'Comment(s): Well done {name.title()}, there is still room for improveent')
        print("=====================================")
    elif average >= "40":
        name = str(student_info[0]['name'])
        print("Status  : FAIL")
        print("Grade   : F")
        print(f'Comment(s): {name.title()} you need to pull up your socks!')
        print("=====================================")
    else:
        name = str(student_info[0]['name'])
        print("Status  : FAIL")
        print("Grade   : F")
        print(f'Comment(s): {name.title()} needs intervention.')
        print("=====================================")

add_info()
calculate_average()
display_results()