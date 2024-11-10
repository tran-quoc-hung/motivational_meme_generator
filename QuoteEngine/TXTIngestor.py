from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import Quote

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')
        
        file_ref = open(path, "r")
        quotes = []
        
        for line in file_ref.readlines():
            line = line.strip("<ï»¿").strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = Quote(parse[0].strip().strip('"'), parse[1])
                quotes.append(new_quote)
        file_ref.close()
        return quotes


