import practice_erp as f

def add_items():
    print("press 1 for library management add")
    print("print 2 for event management add")
    print("press 3 for student management add")
    choice=int(input("what is your choice"))
    if choice==1:
        f.library_management_add()
    elif choice==2:
        f.event_management_add()
    elif choice==3:
        f.student_management_add()
    else:
        print("wrong choice")
def show_items():
    print("press 1 for library management show")
    print("press 2 for event management show")
    print("press 3 for student management show")
    choice=int(input("what is your choice"))
    if choice==1:
        f.library_management_show()
    elif choice==2:
        f.event_management_show()
    elif choice==3:
        f.student_management_show()

def search_items():
    print("press 1 for library management search")
    print("press 2 for event management search")
    print("press 3 for student management search")
    choice=int(input("what is your choice"))
    if choice==1:
        f.library_management_search()
    elif choice==2:
        f.event_management_search()
    elif choice==3:
        f.student_management_search()
    else:
        print("wrong id")

def update_items():
    print("press 1 for lib management update")
    print("press 2 for event management update")
    print("press 3 for student management update")
    choice=int(input("choose your choice"))
    if choice==1:
        f.library_management_update()
    elif choice==2:
        f.event_management_update()
    elif choice==3:
        f.student_management_update()
    else:
        print("wrong choice")

def delete_items():
    print("press 1 for library management delete")
    print("press 2 for event management delete")
    print("press 3 for student management delete")
    choice=int(input("choose your choice"))
    if choice==1:
        f.library_management_delete()
    elif choice==2:
        f.event_management_delete()
    elif choice==3:
        f.student_management_delete()
    else:
        print("wrong choice")

while(True):
    print("press 1 for add items")
    print("press 2 for show items")
    print("press 3 for search items")
    print("press 4 for update items")
    print("press 5 for delete items")
    print("press 6 to stop system")
    choice=int(input("choose choice"))
    if choice==1:
        add_items()
    elif choice==2:
        show_items()
    elif choice==3:
        search_items()
    elif choice==4:
        update_items()
    elif choice==5:
        delete_items()
    elif choice==6:
        break

    else:
        print("no choice")

