# scripts/download_data.py

import requests
from scripts.config_loader import load_config
from . import paths

def download_raw_data(url: str, filename: str, save_location: str):
    """
    Downloads data from the specified URL.

    Args:
        url (str): The URL from which to download the data.
        filename (str): The name of the file to save the data to.
        save_location (str): The location to save the downloaded data. Valid options are 'raw' or 'extra'.

    Raises:
        requests.HTTPError: If there is an error while making the HTTP request.
        ValueError: If the save_location is not 'raw' or 'extra'.

    Returns:
        None
    """
    print(f'Downloading data from {url}...')
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text

        # Save data to the specified location
        if save_location == 'raw':
            save_dir = paths.data_raw_dir
        elif save_location == 'external':
            save_dir = paths.data_external_dir
        else:
            raise ValueError(f'Invalid save location: {save_location}')

        save_file = save_dir / filename
        with open(save_file, 'w') as f:
            f.write(data)
        print(f'Data downloaded to {save_file}')
    except requests.HTTPError as e:
        print(f'Error while making the HTTP request: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
        
def download_data_from_config(config_file: str):
    """
    Downloads data from the URLs provided in the config file.

    Returns:
        None
    """
    config = load_config(config_file)
    for save_location in ['raw', 'external']:
        for data_job in config['data'][save_location]:
            url = data_job['url']
            filename = data_job['name']
            download_raw_data(url, filename, save_location)