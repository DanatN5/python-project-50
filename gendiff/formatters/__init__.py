from .plain import plain_format
from .stylish import stylish_format
from .json import json_format

FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format
}