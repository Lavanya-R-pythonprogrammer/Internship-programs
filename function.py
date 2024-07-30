class Library:
    def __init__(self, books):
        self.books = books

    def iterating(self):
        print("Available books:")
        for book in self.books:
            print(book)

    def remove_book(self, remove_book):
        if remove_book in self.books:
            print("You have remove:", remove_book)
            self.books.remove(remove_book)
        else:
            print("Book not available")

    def add_book(self, add_book):
        print("book is added ")
        self.books.append(add_book)
        
    def access_element(self,index):
        if 0<=index<len(self.books):
            return self.books[index]
