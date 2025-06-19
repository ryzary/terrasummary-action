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
    prompt = f"""
        You are an expert DevOps engineer helping review Terraform plans.

        Your task is to summarize the Terraform plan output below into a **clear, readable summary** suitable for code reviews or pull requests.

        📌 **Format**:
        - Use **headings** for *Resources to be Added*, *Changed*, and *Destroyed*.
        - Group by **resource type** (e.g., `aws_s3_bucket`, `azurerm_virtual_machine`, etc.).
        - Use ✅ **green** for additions, ⚠️ **yellow** for changes, and ❌ **red** for deletions.
        - Provide a **concise explanation** for each change (what it is, why it might matter).

        🎨 **If possible, use ANSI color codes** to make ✅ additions green, ⚠️ changes yellow, ❌ deletions red for terminal output. Otherwise, use **Markdown** format for GitHub.

        Below is the Terraform plan output:
        {plan_text}
        """
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=512,
    )

    # The response contains choices; return the first completion's message content
    return response.choices[0].message.content
