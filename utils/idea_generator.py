# idea_generator.py
# Small wrapper that would call an LLM (OpenAI) to generate ideas.
import os

try:
    import openai
except Exception:
    openai = None


def generate_ideas(prompt: str, n=5):
    """Return a list of content/post ideas based on prompt.

    This is a lightweight fallback that uses OpenAI if configured, otherwise a deterministic stub.
    """
    if openai and os.getenv("OPENAI_API_KEY"):
        resp = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt + "\n\nProvide a numbered list of short post ideas:",
            max_tokens=200,
            n=1,
            temperature=0.8,
        )
        text = resp.choices[0].text.strip()
        # naive split
        return [line.strip() for line in text.splitlines() if line.strip()][:n]

    # Fallback deterministic ideas
    base = [
        f"Quick how-to on {prompt}",
        f"Top 10 tips about {prompt}",
        f"Common mistakes when working with {prompt}",
        f"A case study: {prompt} in action",
        f"A short checklist to get started with {prompt}",
    ]
    return base[:n]
