import csv
import json

def marks_array():
    with open('marks.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

        rows, cols = (line_count, 3)
        marks = [[0 for i in range(cols)] for j in range(rows)]
        n = 0
        csv_file.seek(0)
        next(csv_reader)
        for row in csv_reader:
            marks[n][0] = row[0]
            marks[n][1] = row[1]
            marks[n][2] = row[2]
            n += 1
        del marks[-1]
        return marks 

def tests_array():
    with open('tests.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

        rows, cols = (line_count, 3)
        tests = [[0 for i in range(cols)] for j in range(rows)]
        n = 0
        csv_file.seek(0)
        next(csv_reader)
        for row in csv_reader:
            tests[n][0] = row[0]
            tests[n][1] = row[1]
            tests[n][2] = row[2]
            n += 1
        del tests[-1]
        return tests

def courses_array():
    with open('courses.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

        rows, cols = (line_count, 3)
        courses = [[0 for i in range(cols)] for j in range(rows)]
        n = 0
        csv_file.seek(0)
        next(csv_reader)
        for row in csv_reader:
            courses[n][0] = row[0]
            courses[n][1] = row[1]
            courses[n][2] = row[2]
            n += 1
        del courses[-1]
        return courses

def students_array():
    with open('students.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

        rows, cols = (line_count, 2)
        students = [[0 for i in range(cols)] for j in range(rows)]
        n = 0
        csv_file.seek(0)
        next(csv_reader)
        for row in csv_reader:
            students[n][0] = row[0]
            students[n][1] = row[1]
            n += 1
        del students[-1]
        return students

def unique_students(marks):
    unique_students = [0]
    unique_students[0] = marks[0][1]
    #print(unique_students)
    for entry in marks:
        flag = False
        for n in unique_students:
            #print (entry[1], n)
            if entry[1] == n:
                flag = True
                #print(flag)
        if flag == False:
            unique_students.append(entry[1])
    return unique_students

def report_card(marks, tests, students, courses):

    line_counter = 0
    for line in marks:
        if line_counter == 0:
            #record_entry = [student_id, course_id(decided via test id), weight_sum, marks_sum, count]
            record_entry = []
            record_entry.append(line[1])
            for entry in tests:
                if entry[0] == line[0]:
                    record_entry.append(entry[1])
                    record_entry.append(entry[2])
                    record_entry.append(float(line[2])*(float(entry[2])/100))
                    record_entry.append(1)
            record = []
            record.append(record_entry)
            line_counter += 1

        else:
            record_entry = []
            record_entry.append(line[1])
            for entry in tests:
                if entry[0] == line[0]:
                    record_entry.append(entry[1])
                    record_entry.append(entry[2])
                    record_entry.append(int(line[2])*(int(entry[2])/100))
                    record_entry.append(1)
            entry_count = 0
            flag = False
            for entry in record:
                if (entry[0] == record_entry[0] and entry[1] == record_entry[1]):
                    record[entry_count][2] = int(record[entry_count][2]) + int(record_entry[2])
                    record[entry_count][3] = float(record[entry_count][3]) + float(record_entry[3])
                    record[entry_count][4] += record_entry[4]
                    flag = True
                entry_count += 1
            if flag == False:
                record.append(record_entry)

    updated_record = []
    #updated_record_entry = [student_id, course_id(decided via test id), weight_sum, marks_sum, count, student_name, course_name, course_teacher]
    for entry in record:
        for x in students:
            if entry[0] == x[0]:
                entry.append(x[1])
        for y in courses:
            if entry[1] == y[0]:
                entry.append(y[1])
                entry.append(y[2])
        updated_record.append(entry)
    
    return updated_record

def create_json(report_card, students, courses):
    student_list = []
    for entry in students:
        #print(entry)
        course_list = []
        count = 0
        avg_sum = 0
        for value in report_card:
            if entry[0] == value[0]:
                course_list.append({"id": value[1],
                                    "name": value[6],
                                    "teacher": value[7],
                                    "courseAverage": round(value[3],2)})
                count += 1
                avg_sum += value[3]
        student_list.append({"id": entry[0],
                            "name": entry[1],
                            "totalAverage": round(avg_sum/count,2), 
                            "courses": course_list})
        #print (course_list)
    error = False
    for entry in report_card:
        if entry[2] != 100:
            error = True
    if (error == False):
        print (json.dumps({"students":student_list}))
        return ({"students":student_list})
    else:
        print (json.dumps({"error": "Invalid course weights"}))
        return (json.dumps({"error": "Invalid course weights"}))

marks = marks_array()
tests = tests_array()
courses = courses_array()
students = students_array()
report_card = report_card(marks, tests, students, courses)
output = create_json(report_card, students, courses)
with open("output.txt", "w") as outfile:
    outfile.write(output, outfile)
#print(marks)
#print(tests)
#print(courses)
#print(students)

#time taken to complete this assignment was less than what is shown by the timer as I dozed off in the middle 