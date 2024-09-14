import requests
from .dataset import Dataset

class BlockchainMLAPI:
    def __init__(self, api_key, base_url='https://api.blockchainml.com/v1'):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def get_dataset(self, dataset_id):
        response = self.session.get(f'{self.base_url}/datasets/{dataset_id}')
        response.raise_for_status()
        return Dataset(response.json(), self)

    def list_datasets(self):
        response = self.session.get(f'{self.base_url}/datasets')
        response.raise_for_status()
        return [Dataset(data, self) for data in response.json()]

    def download_dataset(self, dataset_id):
        response = self.session.get(f'{self.base_url}/datasets/{dataset_id}/download')
        response.raise_for_status()
        return response.content