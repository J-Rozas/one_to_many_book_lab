class Book:

    def __init__(self, input_title, input_cover, input_price, input_author, id = None):
        self.title = input_title
        self.cover = input_cover
        self.price = input_price
        self.author = input_author
        self.id = id