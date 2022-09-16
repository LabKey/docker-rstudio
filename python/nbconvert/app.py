import uuid
from urllib.parse import unquote_plus

import boto3
from invoke import run

print('Loading function')

s3_client = boto3.client('s3')

def nbconvert(source_path):
  # TODO: allow for, detect, and process incoming tar.gz
  print(f'now in nbconvert, and...')
  result = run(f"HOME=/tmp python3 -m nbconvert -y --execute --allow-errors --to html {source_path}")
  print(f'got result: {result}')


def handler(event, context): 
  print(f'got context {context} from event {event}')
  if 'test' in event:
    run('cp /var/task/Intro.ipynb /tmp/')
    download_path="/tmp/Intro.ipynb"
    nbconvert(download_path)
    return(f"completed processing of context {context} from event {event}")
  for record in event['Records']:
      bucket = record['s3']['bucket']['name']
      key = unquote_plus(record['s3']['object']['key'])
      tmpkey = key.replace('/', '')
      upload_key = tmpkey.replace('.ipynb','.html')

      print(f'got bucket {bucket} key {key} tmpkey {tmpkey}')

      download_path = f'/tmp/{uuid.uuid4()}{tmpkey}'
      upload_path = download_path.replace('.ipynb','.html')

      print(f'got download_path {download_path} upload_path {upload_path}')

      print(f'trying to download file')
      s3_client.download_file(bucket, key, download_path)

      print(f'trying to convert')
      nbconvert(download_path)

      print(f'trying to upload')
      s3_client.upload_file(upload_path, bucket, upload_key)


  return(f"completed processing of context {context} from event {event}")
