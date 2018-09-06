import json
import os
import io
import requests

from typing import Any, Dict, List, Union, Optional

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Secrets, Configuration
from logzero import logger

__all__ = ["attack"]

Selector = Dict[str, Dict[str, Any]]
Task = Dict[str, Any]

def attack(task: Task, selector: Selector, configuration: Configuration):
    """
    Send a POST to the Turbulence API with the attack information. See the
    Turbulence API docs for more information 
    (https://github.com/cppforlife/turbulence-release/blob/master/docs/api.md).
    """

    url = configuration["turb_api_url"]
    verify_ssl = configuration.get("turb_verify_ssl", True)

    data = {"Tasks": [task], "Selector": selector}
    url = '{}/api/v1/incidents'.format(url)

    logger.debug('Posting `{}` to `{}`'.format(data, url))
    r = requests.post(url, json=data, verify=verify_ssl)
    if r.status_code != 200:
        raise FailedActivity('Turbulence atttack failed: {}'.format(r.text))

    logger.debug('attack submitted sucessfully: {}'.format(r.text))
    return r.text
