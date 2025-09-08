import data

def add_student(name,age,course):
    if not name or not course:
        return "Please add a name and course. "
    if age <=0:
        return "Please Enter a valid Age"
    
    data.enter_student(name,age,course)
    return "Student has been successfully added"

def view_students():
    students=data.get_students()
    return students if students else  "No student is there"

def remove_student(std_id):
    data.delete_student(std_id)
    return f"Student with the student id {std_id} has been removed successfully."

