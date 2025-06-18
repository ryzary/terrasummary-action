import os
import sys
from .summarizer import summarize_terraform_plan

def main():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        sys.exit(1)

    # Check if a filename was passed as a command-line argument
    if len(sys.argv) > 1:
        file = sys.argv[1]
        with open(file, "r") as f:
            plan = f.read()
    else:
        plan = sys.stdin.read()

    summary = summarize_terraform_plan(plan_text=plan, api_key=api_key, model="magistral-small-2506")
    print(summary)

if __name__ == "__main__":
    main()
