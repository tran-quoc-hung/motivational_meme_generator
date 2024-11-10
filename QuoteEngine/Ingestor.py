from typing import List

from .Quote import Quote
from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor

class Ingestor(IngestorInterface):
    """ """
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """ implement parse method """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)