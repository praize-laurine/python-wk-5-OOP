# Assignment 1: Design Your Own Class! 

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages
    
    def book_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

# Inheritance

class DigitalBook(Book):
    def __init__(self, title, author, pages, filesize):
        super().__init__(title, author, pages)
        self.filesize = filesize

    def FileSize(self, mbs):
        """Increase file size, but not beyond 12MB"""
        self.filesize = min(12, self.filesize + mbs)
        print(f"DigitalBook '{self.title}' filesize is now {self.filesize} MB")
    
    def read(self, pages):
        """Override read to mention filesize too"""
        if self.filesize <= 0:
            print(f"Book content is empty! Cannot read {self.title}")
        else:
            super().read(pages)  # reuse Book's read() method
            print(f"'{self.title}' has a filesize of {self.filesize} MB, suitable for reading.")

# Creating objects
book1 = Book("Sarah Jakes", "Woman Evolve", 500)
Digitalbook1 = DigitalBook("Apst. Charles", "Purpose of Woman in a Man", 700, 5)


# Using methods
print(book1.book_info())

print("\n--- Digital Book Snippet ---")
print(Digitalbook1.book_info())

