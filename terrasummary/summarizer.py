from mistralai import Mistral

def summarize_terraform_plan(plan_text: str, api_key: str, model: str = "magistral-small-2506") -> str:
    """
    Summarize terraform plan using Mistral native API.

    Args:
        plan_text: The terraform plan output to summarize.
        api_key: Your Mistral API key.
        model: Model name (e.g., 'magistral-small-2506').

    Returns:
        Summarized text.
    """
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following terraform plan:\n\n{plan_text}"
            }
        ],
        temperature=0.2,
        max_tokens=512,
    )

    # The response contains choices; return the first completion's message content
    return response.choices[0].message.content
