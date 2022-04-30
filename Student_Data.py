#STUDENT DATA
import Main_Menu as m

def details():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    a=int(input('Enter Roll Number: '))
    b=input('Enter Student Name: ')
    c=input('Enter Stream : ')
    d=int(input('Enter Class : '))
    query=('Insert into Student(Roll_Number,Name,Stream,Class) values(%s,%s,%s,%s)')
    record=(a,b,c,d)
    mycursor.execute(query,record)
    mycursor.close()
    mydb.close()
    print('New Record Added!')
    menu()

def show():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    query=('Select*from Student')
    mycursor.execute(query)
    for (a,b,c,d,e) in mycursor:
        print('Roll number: ',a)
        print('Name: ',b)
        print('Stream: ',c)
        print('Class: ',d)
    mycursor.close()
    mydb.close()
    menu()

    
def search():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    e=int(input('Enter Roll Number To Be Searched : '))
    mycursor.execute('select Roll_Number from student;')
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for k in l:
        for t in k:
            p.append(t) 
    if e in p:
        query=('select*from Student where Roll_Number=%s'%e)
        mycursor.execute(query)
        for (a,b,c,d,e) in mycursor:
            print('Roll number: ',a)
            print('Name: ',b)
            print('Stream: ',c)
            print('Class: ',d)
            print('Fees: ',e)
        mycursor.close()
        mydb.close()
        menu()
    else:
        print('Enter a valid roll number to be searched')
        search()

def delete():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    e=int(input('Enter Roll Number To Be Deleted: '))
    mycursor.execute('select Roll_Number from student;')
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for i in l:
        for t in i:
            p.append(t)
    if e in p:
        query=('delete from Student where Roll_Number=%s'%e)
        mycursor.execute(query)
        mycursor.close()
        mydb.close()
        print('Record Deleted!')
        menu()
    else:
        print('Enter a valid roll number to be deleated')
        delete()

def update():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    mycursor.execute('select Roll_Number from student;')
    e=int(input('Enter Roll Number To Select Record Needed To Be Updated/Editted: '))
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for i in l:
        for t in i:
            p.append(t)
    if e in p:
        print('Input New Data')
        s=input('Enter Student Name: ')
        q=input('Enter Stream: ')
        x=int(input('Enter Class: '))
        query=('update Student set Name="%s",Stream="%s",Class=%s where Roll_Number=%s'%(s,q,x,e))
        mycursor.execute(query)
        mycursor.close()
        mydb.close()
        print('Record Has Been Updated/Editted')
        menu()
    else:
        print('Enter a valid roll number to be updated')
        update()

def menu():
    print('\t\t-------------------------------------------')
    print('\t\t       **STUDENT DATA MENU**')
    print('\t\t-------------------------------------------')
    print('\t\t1-ADD STUDENT RECORD')
    print('\t\t2-SHOW STUDENT DETAILS')
    print('\t\t3-SEARCH STUDENT RECORD')
    print('\t\t4-DELETE STUDENT RECORD')
    print('\t\t5-EDIT STUDENT RECORD')
    print('\t\t6-RETURN TO MAIN MENU')
    print('\t\t-------------------------------------------')
    choice=int(input('Enter Your Choice : '))
    if choice==1:
        details()
    elif choice==2:
        show()
    elif choice==3:
        search()
    elif choice==4:
        delete()
    elif choice==5:
        update()
    elif choice==6:
        m.menu()
    else:
        print('Invalid Choice....please try again')
        menu()