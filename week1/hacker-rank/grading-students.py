def gradingStudents(grades):
    # Write your code here
    for i in range (len(grades)):
        if grades[i] < 38:
            continue
        if (5 - (grades[i] % 5)) < 3:
            if grades[i] % 5 == 0:
                continue
            else:
                grades[i] += ( 5 - grades[i] % 5 ) 
            
            
    return grades