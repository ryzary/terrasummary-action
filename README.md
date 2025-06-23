# 📖 Terrasummary

[![GitHub release](https://img.shields.io/github/release/ryzary/terrasummary-action.svg)](https://github.com/ryzary/terrasummary-action/releases)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-terrasummary-blue?logo=github)](https://github.com/marketplace/actions/terrasummary)

Terrasummary is a GitHub Action that intelligently summarizes Terraform plan output using an LLM. It transforms verbose `terraform plan` output into clear, concise summaries that are easy to understand and review.

<div align="center">
  <img src="assets/demo.gif" width="600" height="300">
</div>


## ✨ Features

- 🤖 **LLM-Powered Summarization**: Uses Mistral AI's `devstral-small-2505` model for analysis
- 📊 **Clear Output**: Converts complex Terraform plans into readable summaries
- ⚡ **Fast**: Lightweight action that integrates seamlessly into your CI/CD pipeline
- 🔒 **Secure**: API keys are handled securely through GitHub Secrets

## 🚀 Quick Start

### Prerequisites

- A Mistral AI API key ([Get one here](https://docs.mistral.ai/getting-started/quickstart/))
- Terraform configuration in your repository

### Setup

1. **Get your Mistral API Key**
   - Visit the [Mistral AI documentation](https://docs.mistral.ai/getting-started/quickstart/) to create an account
   - Generate an API key from your Mistral dashboard

2. **Add API Key to GitHub Secrets**
   - Navigate to your repository → **Settings** → **Secrets and variables** → **Actions**
   - Click **New repository secret**
   - Name: `MISTRAL_API_KEY`
   - Value: Your Mistral API key

3. **Add to Your Workflow**

```yaml
name: Terraform Plan Summary

on:
  pull_request:
    branches: [ main ]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.5.0

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan 2>&1 | tee tfplan.log
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: us-east-1

      - name: Summarize Terraform Plan
        uses: ryzary/terrasummary-action@v1.0.0
        with:
          mistral_api_key: ${{ secrets.MISTRAL_API_KEY }}
          plan_file: tfplan.log
```

## 📋 Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `mistral_api_key` | Your Mistral AI API key | ✅ Yes | - |
| `plan_file` | Path to the Terraform plan output file | ✅ Yes | - |




## 🔧 Troubleshooting

### Common Issues

**Issue**: "Plan file not found"
- **Solution**: Ensure the `plan_file` path is correct and the file exists
- **Tip**: Use `${{ github.workspace }}/filename.log` for files in the repository root

**Issue**: "API key authentication failed"
- **Solution**: Verify your Mistral API key is correctly set in GitHub Secrets
- **Tip**: Check that the secret name matches exactly: `MISTRAL_API_KEY`

**Issue**: "Empty or invalid plan output"
- **Solution**: Ensure your Terraform plan generates output and isn't empty
- **Tip**: Check that `terraform plan` runs successfully before the summarization step

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Versioning

We use [SemVer](http://semver.org/) for versioning. For available versions, see the [tags on this repository](https://github.com/ryzary/terrasummary-action/tags).


---

Made with ❤️ by [Ryza Ry](https://github.com/ryzary)
