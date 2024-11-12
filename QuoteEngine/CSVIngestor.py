"""Module read data from csv file."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class CSVIngestor(IngestorInterface):
    """Read data from csv file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Read data from csv file return as list quotes."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = Quote(row['body'].strip().strip('"'), row['author'])
            quotes.append(new_quote)

        return quotes
