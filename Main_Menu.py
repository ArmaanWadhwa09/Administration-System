import Admission as ADM
import Student_Data as STU
import Fee_details as FEE
import Library_details as LIB
def menu():
    print('\t\t-------------------------------------------')
    print('\t\t\t**SCHOOL MANAGEMENT SYSTEM**')
    print('\t\t-------------------------------------------')
    print('\t\t    **KUNSKAPSSKOLAN SCHOOL-MAIN MENU**')
    print('\t\t1-ABOUT SCHOOL')
    print('\t\t2-ADMISSION')
    print('\t\t3-STUDENT DATA')
    print('\t\t4-FEE DETAILS')
    print('\t\t5-LIBRARY DETAILS')
    print('\t\t6-EXIT')
    print('\t\t-------------------------------------------')
    choice=int(input('Enter your choice : '))
    if choice==1:
        f=open('kunskapsskolan.txt','r')
        print('\n',f.read())
        menu()
    elif choice==2:
        ADM.menu()
    elif choice==3:
        STU.menu()
    elif choice==4:
        FEE.menu()
    elif choice==5:
        LIB.menu()
    elif choice==6:
        print('\n\nThanks for using "School Management System"\nDeveloped By: Armaan Wadhwa\tClass: 12th')
        print('Subject: CS with python\t\tSchool: Kunskapsskolan')
    else:
        print('Invalid Choice')






