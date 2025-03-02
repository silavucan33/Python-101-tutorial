# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Pyhton's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

#2.Instead of returning a memory address we can customize this behavior
    def __str__(self):
        return f"{self.title} by {self.author}"
    #with '__str__' we can return a string representation of the object when we print it directly to the console


#4.Another dunder method to check to see if two objects are equal
#we'll disregard the number of pages. you can have to diffrent versions of the same book and they might have diffrent font sizes or dimensions of the physical pages might be diffrent
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

#compare the number of pages
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

#to customize the behavior of addition
#let's add the pages together of two books. maybe we need a summer reading list and we would like to see the total number of pages
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

#within an object we can search for a keyword within one of the attributes
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

#now we could search for a key given an object
#we're accessing book attributes by indexing. (with this object return the value at this key, what's that attribute)
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 201)

#1.what would happen if I was to print 'book1' directly to the console?
#print(book1)
#well we're given a memory address

#3.if they were to have the same title, the same author and the same number of pages, then pyhton would say they're not equal still

#book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
#book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
#print(book1 == book2)


print(book1)
print(book2)
print(book3)
print(book3 == book4)
print(book2 < book3)
print(book2 > book3)
print(book2 + book3)
print("Lion" in book1)
print("Rowling" in book2)
print(book1['title'])
print(book4['author'])
print(book2['num_pages'])
print(book3['audio'])

