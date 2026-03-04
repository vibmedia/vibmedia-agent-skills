---
name: ml-engineer
description: When the user wants to set up LLM evaluations, implement model fine-tuning workflows, or tune RAG pipelines. Trigger on "ML engineer", "LLM evals", "fine-tuning", "RAG tuning", "model training", "vector database".
category: ai
profile: dev
---

# Machine Learning Engineering (LLMs)

> Advanced frameworks for evaluating, fine-tuning, and architecting production-ready Large Language Model applications and robust Retrieval-Augmented Generation (RAG) systems.

## When to Use

- "Set up an eval pipeline to catch regression in our prompt outputs."
- "How do I fine-tune a Llama 3 model on my company's codebase?"
- "Our RAG system is retrieving the wrong chunks; how do we optimize the vector search?"
- "Implement a hybrid search (semantic + keyword) architecture."
- "Help me structure datasets for DPO (Direct Preference Optimization)."

## Before Starting

Ask context-gathering questions if not provided:

1. **The Bottleneck:** What is failing? (Accuracy/Hallucinations, Cost, Latency, Data Privacy).
2. **Infrastructure:** Are they managing open-weights models (vLLM, Ollama, HuggingFace) or using managed APIs (OpenAI, Anthropic, Gemini)?
3. **Data Quality:** Is the fine-tuning/eval dataset clean, labeled, and representative of production workloads?

## Core Framework

### 1. Evaluation Pipelines (LLM Evals)

| Eval Methodology             | Purpose                                                                                                         | Anti-Pattern                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **LLM-as-a-Judge**           | Using an advanced model (e.g., GPT-4o) to grade the output of a smaller model based on a strict rubric.         | Relying solely on exact string matching (`assert output == expected`) for conversational generation. |
| **RAG Metric Hub**           | Measuring Context Precision, Context Recall, Faithfulness, and Answer Relevance (e.g., using Ragas or TruLens). | Eyeballing a few generation results in a chat UI and calling it "good enough."                       |
| **Deterministic Benchmarks** | Checking strict schema outputs, parseable JSON ratios, or function calling accuracy.                            | Skipping CI/CD integration for evals—evals must block deployments.                                   |

### 2. Retrieval-Augmented Generation (RAG) Tuning

| Tuning Strategy      | Best Practice                                                                                                        | Common Mistake                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Chunking**         | Use semantic chunking or windowed overlap to preserve context across paragraph boundaries.                           | Splitting giant documents by an arbitrary character count (e.g., every 500 chars), splitting sentences in half.   |
| **Embedding Models** | Choose task-specific embedding models from the MTEB leaderboard that match the domain language.                      | Using outdated embeddings (like `text-embedding-ada-002`) blindly without testing newer open-source alternatives. |
| **Hybrid Retrieval** | Combine Dense Vector Search (semantic meaning) with Sparse Keyword Search (BM25) using Reciprocal Rank Fusion (RRF). | Relying 100% on vector similarity when searching for specific UUIDs or SKUs.                                      |
| **Re-ranking**       | Use a Cross-Encoder (like Cohere Re-rank) to re-score the top 20 retrieved chunks before feeding them to the LLM.    | Shoving 100 unsorted chunks into the prompt context window and causing the "Lost in the Middle" phenomenon.       |

### 3. Fine-Tuning Workflows

| Phase             | Recommendation                                                                                                                     | Do Not                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Data Curation** | Focus intensely on quality over quantity. 1,000 perfect, human-verified examples > 100,000 synthetic trash examples.               | Fine-tune just to "teach the model facts." (Use RAG for facts, Fine-tune for behavior/tone/format).   |
| **Methodology**   | Use LoRA/QLoRA (Low-Rank Adaptation) for parameter-efficient, fast, and cheap fine-tuning on consumer hardware.                    | Attempt Full-Parameter fine-tuning on a 70B model unless you have a dedicated supercomputing cluster. |
| **Alignment**     | Use RLHF (Reinforcement Learning from Human Feedback) or DPO (Direct Preference Optimization) to train against negative behaviors. | Fine-tune purely on completions (SFT) and expect the model to natively reject toxic inputs.           |

## Output Format

When advising on ML architectures or evaluation code:

1. **Strategic Assessment**: Clear distinction on whether the user needs Prompt Engineering, RAG, or Fine-Tuning (often users ask for Fine-Tuning when RAG is the correct answer).
2. **Metric Definitions**: A bulleted list defining the exact metrics being evaluated (e.g., "Faithfulness: Prevents hallucinations from the context").
3. **The Script**: The Python code, preferably utilizing common libraries (LangChain/LlamaIndex for RAG, Pytest/Promptflow for evals, Unsloth for fine-tuning).
4. **Cost/Latency Alert**: A quick disclaimer on how this architecture impacts production costs or inference latency.

## Common Mistakes

- ❌ **"Fine-Tuning for Knowledge"**: Attempting to fine-tune an LLM on an entire company Wiki to make it a support bot. The model will hallucinate. Always use RAG for dynamic/factual knowledge.
- ❌ **Ignoring Overfitting**: Fine-tuning an LLM so aggressively on a specific JSON schema that it forgets how to converse normally in English (Catastrophic Forgetting).
- ❌ **Vibes-based Engineering**: Pushing a new system prompt to production because it "felt better" during 3 manual test queries.
- ❌ **Blindly trust Vector Search**: Not testing the actual retreived chunks before passing them to the LLM. If the retrieval is garbage, the generation will be garbage (Garbage In, Hella Garbage Out).

## Related Skills

- **prompt-engineering**: Use when optimizing the input text, few-shot examples, or system messages _before_ resorting to training models.
- **cloud-infrastructure**: Use when the focus shifts from ML testing to actually provisioning the GPU clusters required to run inference.
