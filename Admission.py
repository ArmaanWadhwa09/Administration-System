#ADMISSION MODULE
import Main_Menu as m

def details():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    a=int(input('Enter Admission Number : '))
    b=input('Enter Name: ')
    c=(input('Enter fathers Name : '))
    d=int(input('Enter Class : '))
    query=('Insert into Admission values(%s,%s,%s,%s)')
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
    query=('Select*from Admission')
    mycursor.execute(query)
    for (a,b,c,d) in mycursor:
        print('Admission number: ',a)
        print('Name: ',b)
        print('Fathers Name: ',c)
        print('Class: ',d)
    mycursor.close()
    mydb.close()
    menu()
    
def search():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    mycursor.execute('select admission_number from admission')
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for i in l:
        for t in i:
            p.append(t)
    e=int(input('Enter a Admission Number To Be Searched : '))
    if e in p:
        query=('select*from Admission where Admission_Number=%s'%e)
        mycursor.execute(query)
        for (a,b,c,d) in mycursor:
            print('Admission number: ',a)
            print('Name: ',b)
            print('Fathers Name: ',c)
            print('Class: ',d)
        mycursor.close()
        mydb.close()
        menu()
    else:
        print('Enter a valid Admission Number To Be Searched')
        search()
    
def delete():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    mycursor.execute('select admission_number from admission')
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for i in l:
        for t in i:
            p.append(t)
    e=int(input('Enter Admission Number To Be Deleted: '))
    if e in p:
        query=('delete from Admission where Admission_Number=%s'%e)
        mycursor.execute(query)
        mycursor.close()
        mydb.close()
        print('Record Deleted!')
        menu()
    else:
        print('Enter a valid Admission Number To Be Deleated')
        delete()
def update():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    mycursor.execute('select admission_number from admission')
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for i in l:
        for t in i:
            p.append(t)
    e=int(input('Enter Admission Number To Select Record Needed To Be Updated/Editted: '))
    if e in p:
        print('Input New Data')
        s=input('Enter Student Name: ')
        q=(input('Enter Fathers Name: '))
        m=int(input('Enter Class: '))
        query=('update Admission set Name="%s", Fathers_Name="%s",Class=%s where Admission_Number=%s'%(s,q,m,e))
        mycursor.execute(query)
        mycursor.close()
        mydb.close()
        print('Record Has Been Updated/Editted')
        menu()
    else:
        print('Enter a valid admission number to be updated')
        update()

def menu():
    print('\t\t-------------------------------------------')
    print('\t\t\t**ADMISSION MENU**')
    print('\t\t-------------------------------------------')
    print('\t\t1-ADD ADMISSION DETAILS')
    print('\t\t2-SHOW ADMISSION DETAILS')
    print('\t\t3-SEARCH ADMISSION RECORD')
    print('\t\t4-DELETE ADMISSION RECORD')
    print('\t\t5-UPDATE ADMISSION RECORD')
    print('\t\t6-RETURN TO MAIN MENU')
    print('\t\t-------------------------------------------')
    choice=int(input('Enter your choice : '))
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