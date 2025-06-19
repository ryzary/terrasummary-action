# 📖 Terrasumary
Terrasummary is an `Actions` that can be used to sumarize output of `terraform plan` command using LLM. The current version (`v1.0.0`) uses Mistral AI's `devstral-small-2505` model. 


## 🧩 How to Use
1. Terrasumary uses Mistral AI models for text summarization. To use it, you need a `MISTRAL_API_KEY`. 
    - Please refer to this [page](https://docs.mistral.ai/getting-started/quickstart/) to set-up a Mistral account and get your API key.

2. Store the api key as a github secret.
    - Go to your repository and select `setting`.
    - Select `Secrets and Variables` and then `Actions`.
    - Create a `New Repository Secret`. Input your api key and name it `MISTRAL_API_KEY`.

3. Call the `terrasummary action` in your workflow.

    Make sure that you pipe the output of `terraform plan` to a file and use it as an input for Terrasummary.
```
      - name: Terraform Plan
        run: terraform plan -no-color > tfplan.log
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: us-east-1

      - name: Terrasummary
        uses: ryzary/terrasummary-action@v1.0.0
        with:
          mistral_api_key: ${{ secrets.MISTRAL_API_KEY }}
          plan_file: tfplan.log
```
