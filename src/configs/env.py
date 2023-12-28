import json
import os

from dotenv import load_dotenv

# Env variables
load_dotenv()

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT")
IS_DEV_ENVIRONMENT = ENVIRONMENT == "development"

# Firebase
CERTIFICATE_CONTENT = json.loads(os.getenv("FIREBASE_CERTIFICATE_CONTENT"))
BUCKET_NAME = os.getenv("BUCKET_NAME")
UPDATE_PROJECT_URL = os.getenv("UPDATE_PROJECT_URL")
UPDATE_USER_TOKENS_URL = os.getenv("UPDATE_USER_TOKENS_URL")

# Sentry
SENTRY_DSN = os.getenv("SENTRY_DSN")
