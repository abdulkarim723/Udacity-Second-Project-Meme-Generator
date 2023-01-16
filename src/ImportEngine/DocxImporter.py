from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise FileExtensionNotSupported('cannot process this type of files')

        quotemodels = []
        file_ref = open(path, 'rb')
        doc = docx.Document(file_ref)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quotemodel = QuoteModel(parse[0], parse[1])
                quotemodels.append(new_quotemodel)

        return quotemodels
