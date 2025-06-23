# 📖 Terrasummary

[![GitHub release](https://img.shields.io/github/release/ryzary/terrasummary-action.svg)](https://github.com/ryzary/terrasummary-action/releases)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-terrasummary-blue?logo=github)](https://github.com/marketplace/actions/terrasummary)

Terrasummary is a GitHub Action that intelligently summarizes Terraform plan output using AI. It transforms verbose `terraform plan` output into clear, concise summaries that are easy to understand and review.

## ✨ Features

- 🤖 **AI-Powered Summarization**: Uses Mistral AI's `devstral-small-2505` model for intelligent analysis
- 📊 **Clear Output**: Converts complex Terraform plans into readable summaries
- 🔒 **Secure**: API keys are handled securely through GitHub Secrets
- ⚡ **Fast**: Lightweight action that integrates seamlessly into your CI/CD pipeline
- 🎯 **Focused**: Highlights key changes, additions, and deletions in your infrastructure

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
        run: terraform plan -no-color 2>&1 | tee tfplan.log
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

## 📤 Outputs

The action generates a comprehensive summary that includes:

- **Overview**: High-level summary of planned changes
- **Resources**: Detailed breakdown of resources being created, modified, or destroyed
- **Impact Analysis**: Assessment of the changes' significance
- **Recommendations**: Suggestions for review or potential issues to consider

## 💡 Usage Tips

### Best Practices

1. **Capture Complete Output**: Use `2>&1 | tee` to capture both stdout and stderr
2. **Use No-Color Flag**: Add `-no-color` to terraform plan for cleaner output
3. **File Naming**: Use descriptive names for plan files (e.g., `tfplan-prod.log`)

### Example with Multiple Environments

```yaml
- name: Terraform Plan (Production)
  run: terraform plan -var-file="prod.tfvars" -no-color 2>&1 | tee tfplan-prod.log

- name: Summarize Production Plan
  uses: ryzary/terrasummary-action@v1.0.0
  with:
    mistral_api_key: ${{ secrets.MISTRAL_API_KEY }}
    plan_file: tfplan-prod.log
```

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

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting) above
2. Search existing [issues](https://github.com/ryzary/terrasummary-action/issues)
3. Create a new issue with detailed information about your problem

---

Made with ❤️ by [Ryza Ry](https://github.com/ryzary)
