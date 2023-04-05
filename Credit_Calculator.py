grade_list = ['A+','A','B+','B','C+','C','D+','D','F','a+','a','b+','b','c+','c','d+','d','f']
gra_num_list = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0,4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]
total_grade,total_credit_sub,total_credit_view = 0, 0, 0

def change(n):
    cha_num = grade_list.index(n)
    cha_gra = gra_num_list[cha_num]
    return cha_gra

while True:
    pc = input("작업을 선택하세요.\n 1. 입력 \n 2. 계산 \n")

    if pc == '1':
        credit = int(input("학점을 입력하세요:\n"))
        grade = input("평점을 입력하세요: \n")
        print("입력되었습니다.")

        if grade in grade_list:

            if change(grade) == 0.0:
                total_grade += change(grade)*credit
                total_credit_view += credit

            else:
                total_grade += change(grade)*credit
                total_credit_sub += credit
                total_credit_view += credit
            
        else:
            print("Error!")

    elif pc == '2':
        gpa_view = round(total_grade/total_credit_view,2)
        gpa_sub = round(total_grade/total_credit_sub,2)

        print("제출용: ",total_credit_sub,"학점(GPA: ",gpa_sub,")")
        print("열람용: ",total_credit_view,"학점(GPA: ",gpa_view,")\n")
        print("프로그램을 종료합니다.")
        break
 
    else:
        print("Error!")