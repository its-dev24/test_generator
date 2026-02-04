import json
from src.services import call_llm
from src.utils import commonUtils


async def branch_analyzer(code: str):
    prompt = """
You are a senior QA engineer and test automation expert.

Your task is to analyze the given Python code and return ALL independent execution paths.

STRICT RULES (MANDATORY):
- Return ONLY valid JSON
- Do NOT include any text outside JSON
- Use only JSON primitives (true, false, null, numbers, strings)
- Do NOT use Python literals (True, False, None)
- Do NOT nest branches
- Each branch must represent exactly ONE final execution path
- Paths must be mutually exclusive
- Paths must fully cover the logic
- Do NOT use vague paths like "default" or "else"

JSON SCHEMA (MUST MATCH EXACTLY):
{
  "branches": [
    {
      "path": "boolean condition describing when this path is taken",
      "outcome": {
        "returns": "value returned by the function, or null",
        "raises": {
          "exception": "ExceptionType",
          "message": "error message"
        }
      }
    }
  ]
}

OUTCOME RULES:
- Use "returns" ONLY if the function returns a value
- Use "raises" ONLY if the function raises an exception
- Never include both
- If a path returns, "raises" must be null
- If a path raises, "returns" must be null
- If a function returns an enum, represent it exactly (e.g., "Access.FULL")

PATH RULES:
- Combine conditions explicitly
- Include all prior conditions implied by execution order
- Always include the default return path explicitly

IMPORTANT:
- Do NOT introduce success/failure semantics
- Do NOT invent error messages
- Describe only what the code explicitly does

--------------------
EXAMPLE (FOLLOW THIS STYLE EXACTLY)
--------------------

CODE:
{code}


""".replace(
        "{code}", code
    )
    response = call_llm(prompt)
    if response is None:
        raise ValueError("response sis not return anything")
    parsed_response = commonUtils.extract_json(response)
    # print(response)
    return parsed_response
