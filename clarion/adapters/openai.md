# Adapter: OpenAI (GPT-4o / GPT-4.1 / o-series)

Clarion's core is a plain system prompt, so it drops straight into the
`system` (or `developer`) role.

## Python

```python
from openai import OpenAI
from clarion import compose

client = OpenAI()
system_prompt = compose("full")  # or "concise" / "code"

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Should we shard our Postgres database?"},
    ],
)
print(resp.choices[0].message.content)
```

## Notes

- Use the `code` profile for coding agents; it adds the code-discipline module.
- Clarion does not fight your task instructions — it shapes *how* the model
  answers, not *what* it answers. Put task-specific instructions after the
  Clarion block in the same system message, or in a `developer` message.
- To gate quality in an eval harness, pipe the completion through
  `clarion.lint(text)` and assert `report.passed`.
