import sys
import selectors
import json
import io
import struct

request_triva = {
    "animal": "You've selected animal Trivia"
}

animal_trivia = {
     "Where are pandas from?": "China" 
}