def enqueue(q,w):
    q.append(w)
def dequeue(q):
    q.pop(0)
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
        enqueue(a,x)
        print_values(a)
    elif b=='2' and a!=[]:
        dequeue(a)
        print_values(a)
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

