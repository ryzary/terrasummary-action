# 📖 Terrasumary
Terrasummary is a tool to sumarize output of `terraform plan` command.

It is available as an `Actions` that can be used in your GitHub Actions workflow.

## 🧩 How to Use
1. Terrasumary uses Mistral AI models for text summarization. To use it, you need a `MISTRAL_API_KEY`. 
    - Please refer to this [page](https://docs.mistral.ai/getting-started/quickstart/) to set-up a Mistral account and get your API key.

2. Store the api key as a github secret.
    - Go to your repository and select `setting`.
    - Select `Secrets and Variables` and then `Actions`.
    - Create a `New Repository Secret`. Input your api key and name it `MISTRAL_API_KEY`.

3. Call the terrasummary action in your workflow as follows. Make sure that you put it after a terrafrom-plan step.
```
TODO
```
