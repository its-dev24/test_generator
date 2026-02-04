import json
import re
from typing import Any


def extract_json(text: str) -> Any:
    if not text or not text.strip():
        raise ValueError("LLM returned empty response")

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError(f"No JSON found in LLM response:\n{text}")

    return json.loads(match.group())
