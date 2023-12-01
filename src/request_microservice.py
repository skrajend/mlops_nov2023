import requests
import os
from get_data import read_params
import argparse 

def request_response(config_path):
    config = read_params(config_path)
    url = config["url"]
    json_params = config["json_obj"]
    responses = requests.post(url, json = json_params)
    print(responses.text)