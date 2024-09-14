# bmlhub: BlockchainML Dataset Hub

[![PyPI version](https://badge.fury.io/py/bmlhub.svg)](https://badge.fury.io/py/bmlhub)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/bmlhub.svg)](https://pypi.org/project/bmlhub/)

`bmlhub` is a Python package that provides easy access to datasets from the BlockchainML API. It allows users to seamlessly integrate these datasets into their data science workflows using popular libraries such as pandas, polars, HuggingFace datasets, and mlcroissant.

## Features

- Simple API to access BlockchainML datasets
- Easy conversion to pandas DataFrames, polars DataFrames, HuggingFace datasets, and mlcroissant datasets
- Automatic handling of API authentication
- Efficient data downloading and parsing

## Installation

You can install `bmlhub` using pip:

```bash
pip install bmlhub
```

## Quick Start

Here's a simple example to get you started:

```python
from bmlhub import BlockchainMLAPI
from bmlhub.utils import get_api_key

# Initialize the API client
api = BlockchainMLAPI(get_api_key())

# List available datasets
datasets = api.list_datasets()
for dataset in datasets:
    print(dataset)

# Get a specific dataset
dataset = api.get_dataset('dataset_id')

# Load into pandas
df = dataset.to_pandas()

# Load into polars
pl_df = dataset.to_polars()

# Load into HuggingFace datasets
hf_dataset = dataset.to_huggingface()

# Load into mlcroissant
croissant_dataset = dataset.to_croissant()
```

## Authentication

To use `bmlhub`, you need to set your BlockchainML API key as an environment variable:

```bash
export BLOCKCHAINML_API_KEY='your-api-key-here'
```

You can obtain an API key by signing up at [BlockchainML website](https://www.blockchainml.com).

## API Reference

### BlockchainMLAPI

The main class for interacting with the BlockchainML API.

- `BlockchainMLAPI(api_key, base_url='https://api.blockchainml.com/v1')`
  - `api_key`: Your BlockchainML API key
  - `base_url`: The base URL for the API (optional)

Methods:
- `list_datasets()`: Returns a list of available datasets
- `get_dataset(dataset_id)`: Retrieves a specific dataset by ID

### Dataset

Represents a dataset from the BlockchainML API.

Methods:
- `to_pandas()`: Convert the dataset to a pandas DataFrame
- `to_polars()`: Convert the dataset to a polars DataFrame
- `to_huggingface()`: Convert the dataset to a HuggingFace dataset
- `to_croissant()`: Convert the dataset to a mlcroissant dataset

## Contributing

We welcome contributions to `bmlhub`! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have any questions, please open an issue on our [GitHub repository](https://github.com/yourusername/bmlhub/issues).

## Acknowledgments

- Thanks to the BlockchainML team for providing the API
- This package uses several open-source libraries, including pandas, polars, datasets, and mlcroissant

---

Made with ❤️ by the BlockchainML team