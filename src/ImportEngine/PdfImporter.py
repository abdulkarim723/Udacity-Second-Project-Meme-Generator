from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise FileExtensionNotSupported('Cannot Ingest Exception')
        tmp = f'./{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
        file_ref = open(tmp, "r")
        quotemodels = []
        for line in file_ref.readlines():
            line = line.strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quotemodel = QuoteModel(parsed[0], parsed[1])
                quotemodels.append(new_quotemodel)

        file_ref.close()
        os.remove(tmp)
        return quotemodels
