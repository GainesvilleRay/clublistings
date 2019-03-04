from __future__ import print_function
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
#import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "client_secret.json"
SPREADSHEET = "Go live music listings (Responses)"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_id'],
                                            json_key['client_secret'], SCOPE)
