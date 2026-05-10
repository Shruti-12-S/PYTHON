'''
Concept: Classes & Objects
Create a class Book with the following attributes:
title
author 
list of reviews

And add methods to:
add a new review
count reviews
display all reviews
'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self,review):
        self.reviews.append(review)
        print("Review added successfully")
    
    def count_reviews(self):
        print(f"Total reviews: {len(self.reviews)}")

    def display_reviews(self):
        print("\nBook Reviews:")

        if len(self.reviews) == 0:
            print("No reviews available")
        else:
            for i, review in enumerate(self.reviews, start = 1):
                print(f"{i}. {review}")


book1 = Book("Atomic Habits","James Clear")

book1.add_review("Excellent self-help book")
book1.add_review("Very motivating and practical")
book1.add_review("Easy to understand")

book1.count_reviews()

# Display reviews
book1.display_reviews()

