def assignStudentsToTeacher(s, t):
    s = sorted(s)
    t = sorted(t)

    t_dict = {}
    

    for teacher in t:
        t_dict[teacher] = []
    
    
    
    for teacher in t_dict:
        for student in s:
            is_found = False
            if teacher >= student:
                for teach in t_dict:
                    if student in t_dict[teach]:
                        is_found = True
                if is_found == False:
                    t_dict[teacher].append(student)
    print(t_dict)
    
    # for teacher in t_dict:
    #     for student in s:
    #         if teacher >= student:
    #             if student not in t_dict[teacher]:
    #                 t_dict[teacher].add(student)
    # print(t_dict)



def assignStudentsToTeacherTwo(s, t):
    s = sorted(s)
    t = sorted(t)

    s_dict = {}
    

    # for student in s:
    #     s_dict[student] = []
    
    # {}

    for student in s:

        if student not in s_dict:
            prev = max(t) - student
            for teacher in t:
                if teacher >= student:
                    difference = teacher - student
                    if difference <= prev:
                        s_dict[student] = teacher
                        prev = difference
    return s_dict

print(assignStudentsToTeacherTwo([1,8,5,14], [1,87,5]))
print(assignStudentsToTeacherTwo([0,190,34,25], [2,4,100]))

    # for student in s:
    #     if student not in s_dict:
            
    #         for teacher in t:
    #             is_found = False
    #             difference = teacher - student
    #             if difference < 
    #             if teacher >= student:
    #                 for teach in s_dict:
    #                     if student in s_dict[teach]:
    #                         is_found = True
    #                 if is_found == False:
    #                     s_dict[teacher].append(student)
