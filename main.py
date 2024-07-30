import function as f 
books = ['c', 'c++', 'java', 'python']
f=f.Library(books)

msg = """
    1. Itreating operation
    2. Remove book
    3. Add  book
    4. Accessing book
"""
8
while True:
    print(msg)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        f.iterating()
    elif ch == 2:
        book = input("Enter the book name to remove : ")
        f.remove_book(book)
    elif ch == 3:
        book = input("Enter the book name to add: ")
        f.add_book(book)
    elif ch == 4:
        i=int(input("Enter the index number: "))
        book=f.access_element(i)
        if book:
            print("Book at index",i,":",book)
    elif ch == 5:
        print("Thank you. Have a nice day!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
