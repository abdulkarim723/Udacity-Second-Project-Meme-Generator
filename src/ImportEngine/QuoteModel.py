class QuoteModel:
    """Quote Model
    quote: is the quote
    name: is the name of the creator of the quote
    """
    def __init__(self, quote: str, name: str):
        self.quote = quote
        self.name = name

    def __str__(self):
        return f"quote is {self.quote} , name is {self.name}"
