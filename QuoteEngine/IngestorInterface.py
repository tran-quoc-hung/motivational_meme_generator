"""Interface read data from txt,csv,docx,pdf file."""
from abc import ABC, abstractmethod
from typing import List
from .Quote import Quote

class IngestorInterface(ABC):
    """Interface ingestor."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check ingestor."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Implement parse method."""
        pass