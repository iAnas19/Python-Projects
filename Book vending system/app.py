class Book:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qtyInStock = qty
        self.Authors = []

    def GetName(self):
        return self.name

    def GetAuthors(self):
        return self.Authors

    def GetPrice(self):
        return self.price

    def SetPrice(self, new):
        self.price = new

    def GetQtyInStock(self):
        return self.qtyInStock

    def SetGetQtyInStock(self, new):
        self.qtyInStock = new

    def GetNumOfAuthor(self):
        return len(self.Authors)

    def PrintAuthors(self):
        for i in self.Authors:
            print(i.name)

    def AddAuthor(self, author):
        self.Authors.append(author)

    def RemoveAuthor(self, name):
        for i in self.Authors:
            if i.name == name:
                self.Authors.remove(i)


class Author:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender


auth1 = Author("Rhonda Bryne", "email@email.com", "F")
auth2 = Author("Paulo Coelho", "email2@email.com", "T")
b = Book("Alchemist", 12, 3)
print(b.GetNumOfAuthor())
b.AddAuthor(auth1)
b.AddAuthor(auth2)
print(b.GetNumOfAuthor())
b.RemoveAuthor("Paulo Coelho")
b.PrintAuthors()
print(b.GetNumOfAuthor())
