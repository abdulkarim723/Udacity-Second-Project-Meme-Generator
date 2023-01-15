from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .DocxImporter import DocxImporter
from .CsvImporter import CsvImporter
from .PdfImporter import PDFImporter
from .TxtImporter import TxtImporter


class FileExtensionNotSupported(Exception):
    """custom class for non supported file extensions"""


class Ingestor(IngestorInterface):
    allowed_extensions = ['docx', 'csv', 'pdf', 'txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise FileExtensionNotSupported('cannot process this type of files')

        ext = path.split('.')[-1]

        if ext == 'docx':
            return DocxImporter.parse(path)

        elif ext == 'csv':
            return CsvImporter.parse(path)

        elif ext == 'pdf':
            return PDFImporter.parse(path)

        elif ext == 'txt':
            return TxtImporter.parse(path)
