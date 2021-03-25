def student_grade(name, grade):
    sentence = "{} received {}% on the exam".format(name, grade)
    # sentence = "{} received {score}% on the exam".format(name, score=grade)
	# sentence = "{student_name} received {student_score}% on the exam".format(student_score=grade, student_name=name)
    return sentence
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))