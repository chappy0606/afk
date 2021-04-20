import os
from typing import Awaitable
import uuid

def rename_to_uuid(filename=''):
    prefix = 'comp/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[0] + '.png'
    return prefix + name + extension

print(rename_to_uuid())