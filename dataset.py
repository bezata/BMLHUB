import pandas as pd
import polars as pl
from datasets import Dataset as HFDataset
from mlcroissant import Dataset as CroissantDataset
import io

class Dataset:
    def __init__(self, metadata, api):
        self.metadata = metadata
        self.api = api

    def to_pandas(self):
        data = self.api.download_dataset(self.metadata['id'])
        return pd.read_csv(io.BytesIO(data))

    def to_polars(self):
        data = self.api.download_dataset(self.metadata['id'])
        return pl.read_csv(io.BytesIO(data))

    def to_huggingface(self):
        data = self.api.download_dataset(self.metadata['id'])
        df = pd.read_csv(io.BytesIO(data))
        return HFDataset.from_pandas(df)

    def to_croissant(self):
        data = self.api.download_dataset(self.metadata['id'])
        return CroissantDataset.from_csv(io.BytesIO(data))

    def __repr__(self):
        return f"Dataset(id='{self.metadata['id']}', name='{self.metadata.get('name', 'Unnamed')}')"