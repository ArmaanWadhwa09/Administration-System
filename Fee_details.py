#FEE DETAILS
import Main_Menu as m

def DEP():
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
        f=int(input('Enter Fees To Be Deposited: '))
        query=('UPDATE Student Set Fee=%s where Roll_Number=%s')
        record=(f,e)
        mycursor.execute(query,record)
        mycursor.close()
        mydb.close()
        print('Fees Deposited!')
        menu()
    else:
        print('Enter a valid Roll Number To Select Record Needed To Be Updated/Editted')
        DEP()

def DET():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='project',autocommit='True')
    mycursor=mydb.cursor()
    mycursor.execute('select Roll_Number from student;')
    e=int(input('Enter Roll Number To Select Record Needed To Be Searched: '))
    l=[]
    p=[]
    for i in mycursor:
        l.append(i)
    for i in l:
        for t in i:
            p.append(t)
    if e in p:
        query=('select*from Student where Roll_Number=%s'%e)
        mycursor.execute(query)
        for (a,b,c,d,e) in mycursor:
            print('Roll number: ',a)
            print('Name: ',b)
            print('Stream: ',c)
            print('Class: ',d)
            print('Fee: ',e)
        mycursor.close()
        mydb.close()
        menu()
    else:
        print('Enter a valid Roll Number To Select Record Needed To Be Searched')
        DET()

def menu():
    print('\t\t-------------------------------------------')
    print('\t\t\t   **FEE DETAILS MENU**')
    print('\t\t-------------------------------------------')
    print('\t\t1-FEE DEPOSIT')
    print('\t\t2-FEE DETAILS')
    print('\t\t3-RETURN TO MAIN MENU')
    print('\t\t-------------------------------------------')
    choice=int(input('Enter Your Choice : '))
    if choice==1:
        DEP()
    elif choice==2:
        DET()
    elif choice==3:
        m.menu()
    else:
        print('Invalid Choice....please try again')
        menu()