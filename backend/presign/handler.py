import json
import os
import uuid

import boto3

s3 = boto3.client("s3")

ALLOWED_TYPES = {
    "image/jpeg": "jpg",
    "image/png": "png",
}

MAX_SIZE = 2 * 1024 * 1024


def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, ensure_ascii=False)
    }


def lambda_handler(event, context):

    # 1. 요청 데이터 확인
    try:
        body = json.loads(event.get("body") or "{}")
    except (ValueError, TypeError):
        return response(400, {"error": "Invalid JSON"})

    content_type = body.get("content_type")

    # 2. 이미지 형식 검증
    if content_type not in ALLOWED_TYPES:
        return response(400, {
            "error": "Only JPEG and PNG are allowed"
        })

    # 3. 인증된 사용자 확인
    claims = (
        event.get("requestContext", {})
        .get("authorizer", {})
        .get("jwt", {})
        .get("claims", {})
    )

    user_id = claims.get("sub")

    if not user_id:
        return response(401, {"error": "Unauthorized"})

    # 4. S3 버킷 설정
    bucket = os.environ.get("UPLOAD_BUCKET")

    if not bucket:
        return response(500, {"error": "Bucket not configured"})

    # 5. 고유한 이미지 경로 생성
    upload_id = uuid.uuid4().hex
    extension = ALLOWED_TYPES[content_type]

    s3_key = f"uploads/{user_id}/{upload_id}.{extension}"

    # 6. S3 업로드용 임시 URL 발급
    try:
        upload = s3.generate_presigned_post(
            Bucket=bucket,
            Key=s3_key,
            Fields={
                "Content-Type": content_type
            },
            Conditions=[
                {"Content-Type": content_type},
                ["content-length-range", 1, MAX_SIZE]
            ],
            ExpiresIn=300
        )
    except Exception:
        return response(500, {
            "error": "Failed to create upload URL"
        })

    # 7. 결과 반환
    return response(200, {
        "upload_url": upload["url"],
        "fields": upload["fields"],
        "s3_key": s3_key,
        "upload_id": upload_id,
        "expires_in": 300
    })