#!/usr/bin/env python3
import json
with open("example_json.txt") as f:
    json_obj = json.load(f)
    for obj in json_obj["data"]:
        print(obj["public_metrics"]["like_count"])
