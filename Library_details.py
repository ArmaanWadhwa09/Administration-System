#LIBRARY DETAILS
import Main_Menu as m

def ISS():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    a=int(input('Enter Roll Number: '))
    b=input('Enter Student Name: ')
    c=input('Enter Book Name : ')
    d=input('Enter Return Date : ')
    e=input('Is Book Returned? (Yes/No): ')
    query=('Insert into Library values(%s,%s,%s,%s,%s)')
    record=(a,b,c,d,e)
    mycursor.execute(query,record)
    mycursor.close()
    mydb.close()
    print('New Record Added!')
    menu()

def RET():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    e=int(input('Enter Roll Number to update value: '))
    mycursor.execute('select roll_number from library')
    l=[]
    p=[]
    for k in mycursor:
        l.append(k)
    for i in l:
        for t in i:
            p.append(t)
    if e in p:
        f=input('Is Book Returned? (Yes/No): ')
        query=('UPDATE Library Set Book_Returned=%s where Roll_Number=%s')
        record=(f,e)
        mycursor.execute(query,record)
        mycursor.close()
        mydb.close()
        print('Value Updated!')
        menu()
    else:
        print('Enter a valid roll Number')
        RET()

def menu():
    print('\t\t-------------------------------------------')
    print('\t\t\t   **LIBRARY DETAILS MENU**')
    print('\t\t-------------------------------------------')
    print('\t\t1-BOOK ISSUE')
    print('\t\t2-UPDATE BOOK RETURN')
    print('\t\t3-RETURN TO MAIN MENU')
    print('\t\t-------------------------------------------')
    choice=int(input('Enter Your Choice : '))
    if choice==1:
        ISS()
    elif choice==2:
        RET()
    elif choice==3:
        m.menu()
    else:
        print('Invalid choice....please try again')
        menu()