
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"Title : {self.title}, Author: {self.author}, Pages: {self.pages}")


if __name__ == '__main__':
    book1 = Book("Atomic Habits",
                 "James Clear",
                 320)

    book2 = Book("Deep Work",
                 "Cal Newport",
                 304)

    book1.description()
    book2.description()
