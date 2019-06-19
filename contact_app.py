print("Welcome to contacts!!!...")
z=True
contacts=dict()
in_contact=dict()
while z==True:
    print("Press \"1\" for \"Adding a contact\" \nPress \"2\" for \"Deleting a contact\"")
    print("Press \"3\" for \"Updating a contact\"\nPress \"4\" for \"Searching a contact\"\nPress \"5\" to \"Exit the contacts\"")
    print("Press \"6\" for \"Viewing all the contacts\"")
    a=int(input())
    if a==1:
        print("Press 1-Add contact in SIM or Press 2-Add contact in PHONE")
        y=int(input())
        if y==1:
            newname=input("Enter the contact name: ")
            num=input("Enter the new number: ")
            if len(num)==10:
                contacts[newname]=num
                print("Added Successfully!!!")
            else:
                print("Please enter the correct number. Total digits should be 10")
        elif y==2:
            newname=input("Enter the contact name: ")
            num=input("Enter the new number: ")
            if len(num)==10:
                contacts[newname]=num
                print("Added Successfully!!!")
    elif a==2 and contacts!={}:
        name_to_delete=input("Enter the contact to be deleted: ")
        if name_to_delete in contacts:
            contacts.pop(name_to_delete)
            print("Deleted Successfully!!!")
        else:
            print("Name not in the contacts.")
    elif a==3 and contacts!={}:
        print("Press n for updating name or m for number updating")
        x=input()
        searchname=input("Enter the name to be updated: ")
        if x=="n":
            if searchname in contacts:
                y=contacts[searchname]
                new=input("Enter the new name: ")
                contacts[new]=y
                contacts.pop(searchname)
                print("Updated Successfully!!!")
            else:
                print("Name not in the contacts. Try adding the contact")
        if x=="m":
            if searchname in contacts:
                new_num=input("Enter the new number: ")
                contacts[searchname]=new_num
                print("Updated Successfully!!!")
            else:
                print("Name not in the contacts. Try adding the contact")
    elif a==4 and contacts!={}:
        search=input("Enter the name to be shown: ")
        if search in contacts:
            print("The number for the contact "+search+" is "+contacts[search])
        else:
            print("Sorry...The entered contact is not found. Try entering correct name or add the contact")
    elif a==5:
        z=False
    elif a==6:
        Total=len(contacts)
        print("The number of contacts in your list is",Total,".They are: ")
        for i,j in contacts.items():
            print(i,"->",j)
    else:
        if contacts=={}:
            print("Nothing in Contacts. Please try to add some contacts.")
        z=True
    
