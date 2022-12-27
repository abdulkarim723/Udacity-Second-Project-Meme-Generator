from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CsvImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot process this type of files')

        quotemodels = []
        csv = pd.read_csv(path)

        for index, line in csv.iterrows():
            if line.body != "":
                new_quotemodel = QuoteModel(line.body, line.author)
                quotemodels.append(new_quotemodel)

        return quotemodels
