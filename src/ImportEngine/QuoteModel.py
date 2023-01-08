class QuoteModel:
    """Quote Model
    quote: is the quote
    name: is the name of the creator of the quote
    """
    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __str__(self):
        return f"quote is {self.body} , name is {self.author}"
