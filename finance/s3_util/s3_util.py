import os
from pathlib import Path

import boto3

client = boto3.client("s3")
s3 = boto3.resource("s3")
bucket = s3.Bucket("personal-data-dashboard.david-pw.com")


def get_s3_filenames(prefix: str) -> list[str]:
    paginator = client.get_paginator("list_objects_v2")
    paginator_iterator = paginator.paginate(Bucket=bucket.name, Prefix=prefix)

    keys = []
    for result in paginator_iterator:
        if result is None or result.get("Contents") is None or len(result.get("Contents")) == 0:
            return []
        for content in result.get("Contents"):
            new_key = Path(content.get("Key")).relative_to(prefix)
            keys.append(os.path.join(prefix, new_key))
    return keys


def get_object(key: str):

    return client.get_object(Bucket=bucket.name, Key=key)
