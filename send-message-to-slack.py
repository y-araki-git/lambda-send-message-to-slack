import boto3
from urlparse import urljoin
from urllib import urlencode
import urllib2 as urlrequest
import json
import random
 
SLACK_POST_URL = 'WEB HOOK URLÇãLç⁄'
SLACK_MESSAGE_TITLE = 'Something happened'
def lambda_handler(event, context):
  post_image_to_slack()
 
def post_image_to_slack():
  post_msg = build_message()
  return post(post_msg)
 
def build_message(**kwargs):
  post_message = {}
  post_message["pretext"] = SLACK_MESSAGE_TITLE
  post_message["text"] = message()
  post_message.update(kwargs)
  return post_message
 
def post(payload):
  payload_json = json.dumps(payload)
  data = urlencode({"payload": payload_json})
  req = urlrequest.Request(SLACK_POST_URL)
  response = urlrequest.build_opener(urlrequest.HTTPHandler()).open(req, data.encode('utf-8')).read()
  return response.decode('utf-8')
 
def message():
  result = "Something occurred. Please escalate to the information system team."
  return str(result)