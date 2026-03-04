---
name: cloud-infrastructure
description: When the user wants to design cloud architecture, write infrastructure as code (IaC), or configure AWS/GCP/Azure resources. Trigger on "cloud architecture", "Terraform", "AWS", "GCP", "infrastructure", "provision servers".
category: devops
profile: dev
---

# Cloud Infrastructure & IaC

> Authoritative patterns for provisioning scalable, secure, and maintainable cloud infrastructure using Infrastructure as Code.

## When to Use

- "Write a Terraform script for an AWS EKS cluster."
- "What is the best architecture for a high-availability serverless app on GCP?"
- "Help me set up an Azure Virtual Network with public and private subnets."
- "Review my Terraform module for security flaws."
- "How do I manage Terraform state across a team?"

## Before Starting

Ask context-gathering questions if not provided:

1. **Cloud Provider:** Which cloud is primary? (AWS, GCP, Azure, DigitalOcean).
2. **IaC Tool:** Terraform, OpenTofu, Pulumi, AWS CDK, or CloudFormation?
3. **Scale & State:** Is this a single-environment prototype, or multi-environment enterprise setup? Where is the state stored?

## Core Framework

### 1. Architectural Patterns

| Architecture                            | Best For                                                     | Do                                                       | Don't                                                    |
| --------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------- | -------------------------------------------------------- |
| **Serverless (Lambda/Cloud Functions)** | Bursty workloads, event-driven tasks, unpredictable scaling. | Decouple logic via event queues (SQS/PubSub).            | Run long-running tasks (>15 mins) on serverless compute. |
| **Container Orchestration (K8s/ECS)**   | Consistent traffic, microservices, complex dependencies.     | Use managed control planes (EKS/GKE).                    | Manage your own EC2/VM-based raw Kubernetes cluster.     |
| **3-Tier Web App**                      | Traditional monolithic or semi-modular web services.         | Separate Web, App, and DB across Private/Public subnets. | Put the database in a public subnet.                     |

### 2. Infrastructure as Code (Terraform) Practices

| Practice             | Recommendation                                                                | Anti-Pattern                                                         |
| -------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **State Management** | Use remote state backends (S3 + DynamoDB for locking) with strict IAM roles.  | Commit `terraform.tfstate` directly into Git.                        |
| **Modularity**       | Build reusable modules for repeated components (e.g., standard VPC creation). | Copy-paste hundreds of lines of resource blocks across environments. |
| **Hardcoding**       | Pass environmental differences via `variables.tf` and `.tfvars` files.        | Hardcode AMI IDs or instance sizes directly inside `main.tf`.        |
| **Secrets Engine**   | Reference secrets via data sources (AWS Secrets Manager, HashiCorp Vault).    | Pass plaintext database passwords into Terraform variables.          |

### 3. Provider Specifics & Security

| Provider  | Security Best Practice                                                                                 | Common Mistake                                                         |
| --------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **AWS**   | Apply Principle of Least Privilege in IAM Policies using explicit `Action` and `Resource` constraints. | Using `Resource: "*"` and `Action: "*"` for application roles.         |
| **GCP**   | Utilize Workload Identity Federation instead of long-lived service account keys.                       | Exporting and downloading JSON Service Account keys.                   |
| **Azure** | Implement Managed Identities for cross-resource communication without credentials.                     | Storing connection strings in App Service configurations in plaintext. |

## Output Format

When generating IaC scripts or architectural advice, structure the response as follows:

1. **Architecture Overview**: A 2-sentence summary of the design.
2. **Prerequisites**: What assumes the user already has (e.g., an existing VPC, a configured provider block).
3. **The Code**: Provide the IaC scripts separated by logical files (e.g., `main.tf`, `variables.tf`, `outputs.tf`).
4. **Deployment Strategy**: Explicit commands to safely apply the changes (`terraform init`, `terraform plan`, `terraform apply`).

## Common Mistakes

- ❌ **ClickOps over Code**: Modifying resources in the AWS/GCP console manually after they were provisioned by Terraform, leading to state drift.
- ❌ **Missing Tagging Strategy**: Failing to enforce consistent tags (e.g., `Environment`, `Project`, `CostCenter`) leading to billing nightmares.
- ❌ **Public Buckets**: Leaving S3/GCS buckets public unless explicitly serving web assets.
- ❌ **Ignoring Blast Radius**: Putting entire massive infrastructures in a single state file instead of splitting by domain/lifecycle.

## Related Skills

- **devops-engineer**: Use when focusing on CI/CD pipelines, GitHub Actions, and code deployment, rather than raw server provisioning.
- **server-management**: Use when debugging Linux processes or scaling a specific VM _after_ it has been provisioned.
