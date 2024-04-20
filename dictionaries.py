# library_inventory = {"1984" : 4 , "To kill a mockingbird" : 3 , "The great gatsby" : 5}

# print(f"Copies of a 1984 {library_inventory["1984"]}")

# # borrowing a copy

# library_inventory["1984"] -= 1

# print(f"Copies of a 1984 {library_inventory["1984"]}")



book_club = {
    "1984" : {
        "author" : "George Orwell",
        "year" : "1949",
        "reviews" : {"Alice" : 9 , "Bob" : 8}
    },
    "Brave New World" : {
        "author" : "Aldous Huxley",
        "year" : "1932",
        "reviews" : {"Charlie" : 7 , "Diana" : 8}
    }
}

# adding a review
book_club["1984"]["reviews"]["Charlie"] = 10

# print(book_club["1984"]["reviews"])

# accessing a data

for book , details in book_club.items() :
    avg_review = sum(details["reviews"].values()) / len(details["reviews"])
    print(f"{book} ({details["year"]}) , Average review : {avg_review : 1f}")


