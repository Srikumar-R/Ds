def push(q,w):
    q.append(w)
def pop(q):
    q.pop()
def peek(q):
    return(q[-1])
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
    print("Press \"6\" for \"Peeking value in a list\"")
    b=input()
    if b=='1':
        x=input("Enter the data to be inserted: ")
        push(a,x)
        print_values(a)
    elif b=='2' and a!=[]:
        pop(a)
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
    elif b=='6':
        print(peek(a))
    else:
        if a==[]:
            print("List is empty...")
        elif b not in '123456':
            print("Invalid input")
print("Process Finished... Thank you Visit Again..!!!")

