# Adapter: Google Gemini

Clarion maps to Gemini's `system_instruction`.

## Python

```python
import google.generativeai as genai
from clarion import compose

genai.configure(api_key="...")
model = genai.GenerativeModel(
    "gemini-1.5-pro",
    system_instruction=compose("full"),
)

resp = model.generate_content("Should we shard our Postgres database?")
print(resp.text)
```

## Notes

- Gemini honors a single `system_instruction`; concatenate Clarion first, then
  any task instructions, keeping Clarion's ordering intact.
- If you hit context-budget pressure, switch to the `concise` profile — it drops
  the code and refusal modules, which most non-agent chat flows don't need.
