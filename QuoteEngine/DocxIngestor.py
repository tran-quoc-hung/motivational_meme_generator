from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .Quote import Quote

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')
        
        quotes = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = Quote(parse[0].strip().strip('"'), parse[1])
                quotes.append(new_quote)
        return quotes


