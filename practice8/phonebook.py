import csv
from connect import get
def cr_t():
    conn=get()
    cur=conn.cursor()
    cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook(
                id SERIAL PRIMARY KEY,
                name TEXT,
                phone TEXT)
""")
    conn.commit()
    cur.close()
    conn.close()

def add():
    name=input("Name: ")
    phone=input("Phone: ")

    conn=get()
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO phonebook(name,phone) VALUES(%s,%s)",
        (name,phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    

def impo():
    conn=get()
    cur=conn.cursor()

    with open('contacts.csv',mode='r',encoding='utf-8') as file:
        read=csv.reader(file)
        for i in read:
            if len(i)<2:
                continue
            name,phone=i[0],i[1]
            cur.execute("INSERT INTO phonebook (name,phone) VALUES (%s,%s)",(name,phone))
            conn.commit()
        
def show():
    conn=get()
    cur=conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    for r in cur.fetchall():
        print(r)

def delete():
    name=input("Enter name to delete: ")
    conn=get()
    cur=conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s",(name,))

    conn.commit()
    cur.close()
    conn.close()

def update():
    name=input("Enter name of contact to update: ")
    newp=input("Input new phone: ")
    conn=get()
    cur=conn.cursor()
    cur.execute("UPDATE phonebook SET phone=%s WHERE name = %s",(newp,name))
    conn.commit()
    cur.close()
    conn.close()

def search():
    name=input("Enter name to search:")
    conn=get()
    cur=conn.cursor()
    cur.execute("SELECT*FROM phonebook WHERE name LIKE %s",(f'%{name}%',))
    results=cur.fetchall()
    for j in results:
        print(j)
    cur.close()
    conn.close()

def menu():
    cr_t()
    while True:
        print("\n1-Add")
        print("2-Show")
        print("3-Delete")
        print("4-contacts")
        print("5-update")
        print("6-search")
        print("0-Exit")

        choice=input("Choose: ")
        if choice=="1":
            add()
        elif choice=="2":
            show()
        elif choice=="3":
            delete()
        elif choice=="4":
            impo()
        elif choice=="5":
            update()
        elif choice=="6":
            search()
        elif choice=="0":
            break
        else:
            print("Error")
menu()
cr_t()