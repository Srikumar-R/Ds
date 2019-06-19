def insert_to_beg(q,w):
    q.insert(0,w)
def insert_in_any(q,w,e):
    q.insert(w,e)
def insert_at_end(q,w):
    q.append(w)
def delete_data(q,w,v):
    q.pop(v)
def search(q,w):
    if w in q:
        return("YES")
    else:
        return("NO")
def print_values(q):
    for i in q:
        print(i)

a=[]
print("Welcome!!!")
z=True
while(z==True):
    print("Press \"1\" for \"Insert in a list\" \nPress \"2\" for \"Delete in list\"")
    print("Press \"3\" for \"Search in a list\"\nPress \"4\" for \"Display values in a list\"\nPress \"5\" to \"Exit the list process\"")
    b=input()
    if b=='1':
        x=input("Enter the data to be inserted: ")
        print("Where to insert?... \nPress 1 to insert in beginning\nPress 2 to insert in any other place \nPress 0 to insert in the end")
        c=input()
        if c=='1':
            insert_to_beg(a,x)
            print_values(a)
        elif c=='2':
            y=int(input("Enter the place where to be inserted: "))
            insert_in_any(a,y-1,x)
            print_values(a)
        elif c=='0':
            insert_at_end(a,x)
            print_values(a)
    elif b=='2' and a!=[]:
        x=input("Enter the data to be deleted: ")
        if x in a:
            delete_data(a,x,a.index(x))
            print_values(a)
        else:
            print("Data not in the list")
    elif b=='3' and a!=[]:
        x=input("Enter the data to be searched: ")
        y=search(a,x)
        if y=='YES':
            print("Data is in given list")
        elif y=="NO":
            print("Data not in the list")
    elif b=='4' and a!=[]:
        print_values(a)
    elif b=='5':
        z=False
    else:
        if a==[]:
            print("List is empty...")
        elif b not in '12345':
            print("Invalid input")
print("Process Finished... Thank you Visit Again..!!!")

