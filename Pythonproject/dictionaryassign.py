# ans1:
# #Creating dictionary of books and it's authors
books = {"Gone with the wind": "Margaret Mitchelll",
         "The Grapes of the Wrath": "John Steinbeck",
         "Great Work of Time": "John Crowley",
         "The Green Bay Tree": "Louis Bromfield"
         }
print(books)

# ans2:
# adding new book
books["Antic hat"] = "Aldous Huxley"
print(books)
# update the authors of existing book
books["Great Work of Time"] = "Rabindranath Tagore"
print(books)

# ans3:
# looping through the dictionary
print("The title of the books along with the authors are:")
for key, value in books.items():
    print(key, ":", value)
