import unittest
# aby dobrzeoddać abstrakcję, trzeba przemyśleć wybór klas, aby dobrze obrazowały rzeczywisty model, a metody umieścić tak, aby odpowiedzialność poszczególnych podmiotów się zgadzała
class Library(): # aplikacja zarzdza zasobami biblioteki, więc klasy to biblioteka i klient
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): # biblioteka umożliwia wypożyczenie z niej książki
        if requestedBook in self.availableBooks: # o ile taka istnieje i jest dostępna
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): # przejrzenie zasobu
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): # przeywrócenie książki do zasobu
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")
 
class Customer(): # klient ma wiele cech, ale z perspektywy biblioteki interesuje nas tylko czy ma wypożyczoną książę i jeśli tak to jaką
    book = "" # ten typ biblioteki umożliwia wypożyczenie jedne książki jednej osobie
    haveBook = False
    def requestBook(self, book): # klient może zapytać o książę
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): # albo zwrócić jeśli posiada
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
 
 
def setup():
    size(220,100)
 
    if __name__ == '__main__':
        unittest.main()
   
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) # do wypożyczania
    rect(100,40,100,20) # do zwracania
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)
 
def mouseClicked(): # poklikajcie kilkakrotnie w przyciski: wypożyczneie dwa razy tej samej książki, próba zwrócenia bez posiadania żadnej? Kto podejmuje działanie?
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
            library.lendBook(Madziks.requestBook("Sens Sztuki")) # cała interakcja między biblioteką a klientem łączy się dopiero tutaj, obiekty są oddzielne i każdy ma swoją odpowiedzialność: biblioteka za przechowywane książki, klient za wypożyczoną i to tej odpowiedzialności dotyczą metody, nie używają wzajemnie swoich pól, jest porządek
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            library.addBook(Madziks.returnBook())
 
class tescik(unittest.TestCase):
    global library, Madzia
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
    library = Library(books)
    Madzia = Customer()
 
    def testSameBooks(self):
        self.assertFalse(Madzia.haveBook)
        
    def testEmptyLibrary(self):
        self.assertTrue(library.availableBooks != [])
        
class testCustomer(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(testCustomer, self).__init__(*args, **kwargs)
        self.cust = Customer
        self.cust2 = Library
 
    def testSameBooks(self):
        self.assertNotEqual(self.cust.book, self.cust2.book)
 
