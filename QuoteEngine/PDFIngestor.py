"""Module read data from pdf file."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .Quote import Quote

class PDFIngestor(IngestorInterface):
    """Read data from pdf file."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Read data from pdf file return as list quotes."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')
        
        tmp = f'./{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        new_file_ref = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                new_file_ref = line.split(' "')

        for line in new_file_ref:
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = Quote(parsed[0].strip().strip('"'), parsed[1])
                quotes.append(new_quote)
        
        file_ref.close()
        os.remove(tmp)
        return quotes