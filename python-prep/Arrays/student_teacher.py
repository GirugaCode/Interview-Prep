def assignStudentsToTeacher(s, t):
    s = sorted(s)
    t = sorted(t)

    t_dict = {}

    for teacher in t:
        t_dict[teacher] = []
    
    print(t_dict)

print(assignStudentsToTeacher([1,8,5,14], [1,87,5]))