def school_data(n):
    stud_count = 0
    prof_count = 0
    school_details = []
    for i in range(n):
        school_details.append(input("Enter email address here: "))
    print(school_details)
    for el in school_details:
        if '@student.college.edu' in el:
            stud_count += 1
        elif '@prof.college.edu' in el:
            prof_count += 1

    print(f"There is/are a total of {stud_count} email(s) entered")
    print(f"There is/are a total of {prof_count} email(s) entered")


school_data(int(input("Enter the amount of information to be stored: ")))
