"""Load local classroom configuration, independently of GitHub authentication."""

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def validate_config():
    """Require a classroom value without displaying it or storing it in source."""
    load_dotenv(PROJECT_ROOT / ".env")
    access_key = os.getenv("BILLING_ACCESS_KEY", "").strip()
    if not access_key or len(access_key) != 19 :
        raise ValueError(
            "Missing BILLING_ACCESS_KEY. Create .env from .env.example "
            "and insert the classroom demo value supplied by your teacher."
        )
    if access_key == "replace-with-classroom-value":
        raise ValueError(
            "The classroom access key is still a placeholder. "
            "Replace it in .env with the demo value supplied by your teacher."
        )
