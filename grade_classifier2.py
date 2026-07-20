student_info = []

def add_info():
    name = input("Enter your first name and last name: ").strip().title()
    while True:
        if len(name) == 0:
            print("===========Please enter your names!===============")
            name = input("Enter your first name and last name: ").strip().title()
        elif len(name) > 0:
            student_info.append({'name': f'{name}'})
            print(student_info)
            break


    subject1_marks = input("Enter subject 1 marks: ").strip()
    
    while True:
        if len(subject1_marks) == 0:
            try:
                print("Must be a number!")
                subject1_marks = input("Enter subject 1 marks: ")
                print(type(subject1_marks))
            except ValueError:
                print("Must be a number!")
                break
        elif len(subject1_marks) > 0:
            try:
                updated_marks = int(subject1_marks)
                if updated_marks is str(updated_marks):
                    print('')
               
                elif updated_marks is int(updated_marks):
                        student_info.append({'subject1_marks': f' {int(updated_marks)}'})
                        print("")
                break
            except ValueError:
                print("Must be a number")
                subject1_marks = input("Enter subject 1 marks: ")
                
        else:
            print
    
    subject2_marks = input("Enter subject 2 marks: ").strip()
    
    while True:
        if len(subject2_marks) == 0:
            try:
                print("Must be a number!")
                subject2_marks = input("Enter subject 2 marks: ")
                print(type(subject2_marks))
            except ValueError:
                print("Must be a number!")
                break
        elif len(subject2_marks) > 0:
            try:
                updated_marks = int(subject2_marks)
                if updated_marks is str(updated_marks):
                    print('')
               
                elif updated_marks is int(updated_marks):
                        student_info.append({'subject2_marks': f' {int(updated_marks)}'})
                        print("")
                break
            except ValueError:
                print("Must be a number")
                subject2_marks = input("Enter subject 2 marks: ")
                
        else:
            print
    
    subject3_marks = input("Enter subject 3 marks: ").strip()
    
    while True:
        if len(subject3_marks) == 0:
            try:
                print("Must be a number!")
                subject3_marks = input("Enter subject 3 marks: ")
                print(type(subject3_marks))
            except ValueError:
                print("Must be a number!")
                break
        elif len(subject3_marks) > 0:
            try:
                updated_marks = int(subject3_marks)
                if updated_marks is str(updated_marks):
                    print('')
               
                elif updated_marks is int(updated_marks):
                        student_info.append({'subject3_marks': f' {int(updated_marks)}'})
                        print("")
                break
            except ValueError:
                print("Must be a number")
                subject3_marks = input("Enter subject 2 marks: ")
                
        else:
            print
    

def calculate_average():
    subject1 = student_info[1]['subject1_marks']
    subject2 = student_info[2]['subject2_marks']
    subject3 = student_info[3]['subject3_marks']
    average = round(int(subject1), 2) + round(int(subject2), 2) + round(int(subject3), 2)
    print(f'Average: {average / 3}')
   

def display_results():
    name = str(student_info[0]['name'])
    print("=======================================")
    print(f"      RESULTS FOR {str(name).upper()}")
    print("=======================================")
    name = str(student_info[0]['name'])
    print(f'Name    : {name.upper()}')
    marks = round(float(student_info[1]['subject1_marks']), 2) + round(float(student_info[2]['subject2_marks']), 2) + round(float(student_info[3]['subject3_marks']), 2)
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
