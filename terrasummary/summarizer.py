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
        Summarize the following Terraform plan output into a clear, **concise table**.

        📌 **Format**:
        Use a Markdown table with the following columns:

        | Action   | Resource Type         | Resource Name              | Details                         |
        |----------|-----------------------|----------------------------|---------------------------------|

        - **Action**: `Add`, `Change`, or `Destroy`
        - **Resource Type**: The type of the Terraform resource (e.g., `aws_s3_bucket`)
        - **Resource Name**: The resource name (e.g., `log_bucket`)
        - **Details**: Brief description of what's changing or being created/destroyed.

        Please output only the **Markdown table**.

        Here is the Terraform plan output:
        {plan_text}
        
        ---

        ### ✅ **Example Output:**
        | Action  | Resource Type      | Resource Name            | Details                                      |
        |---------|--------------------|--------------------------|----------------------------------------------|
        | Add     | aws_s3_bucket      | log_bucket               | Creates a new S3 bucket for logs             |
        | Change  | aws_instance       | web_server               | Instance type `t2.micro` → `t3.micro`       |
        | Destroy | aws_lambda_function| old_processor            | Function no longer needed, will be removed  |

        ---
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
