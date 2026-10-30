import json

import pytest

@pytest.mark.dh
def test_jsonhandling():
    with open("testData/creds.json",) as data:
        formattedData  = json.load(data)
        print(formattedData)
        