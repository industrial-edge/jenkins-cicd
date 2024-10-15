import sys
import json

try:
    rawData = json.load(sys.stdin)
    print(rawData[len(rawData)-1]['versionNumber'])
except:
    print("0.0.0")
