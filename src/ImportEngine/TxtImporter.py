from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot process this type of files')

        quotemodels = []
        with open(path, 'r') as file:
            data = file.readlines()

        for line in data:
            if line != "":
                text = line.split('-')
                new_quotemodel = QuoteModel(text[0], text[1].strip())
                quotemodels.append(new_quotemodel)

        return quotemodels