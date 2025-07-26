import os
import json
import base64
from googleapiclient.discovery import build
from google.oauth2 import service_account

def handler(event, context):
    headers = event.get("headers", {})
    auth = headers.get("authorization", "")

    # Use environment variable for token
    expected_token = os.environ.get("ACCESS_TOKEN", "")
    if auth != f"Bearer {expected_token}":
        return {"statusCode": 403, "body": "Forbidden"}

    creds_json = json.loads(base64.b64decode(os.environ["GDRIVE_CREDENTIALS"]))
    creds = service_account.Credentials.from_service_account_info(
        creds_json,
        scopes=["https://www.googleapis.com/auth/drive.readonly"]
    )
    drive_service = build("drive", "v3", credentials=creds)

    file_id = event["queryStringParameters"]["file_id"]

    request = drive_service.files().get_media(fileId=file_id)
    file_data = request.execute()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/pdf"},
        "body": base64.b64encode(file_data).decode("utf-8"),
        "isBase64Encoded": True
    }
