---
name: prompt-engineering
description: When the user wants to optimize LLM interactions, write system prompts, create few-shot examples, or improve context window usage. Trigger on "prompt engineering", "system prompts", "few-shot patterns", "context window optimization", "improve prompt".
category: ai
profile: shared
---

# Prompt Engineering & Context Window Optimization

> Advanced methodology for writing resilient system prompts, utilizing few-shot learning effectively, and managing AI assistant context constraints.

## When to Use

- "Write a system prompt for my customer support bot."
- "My LLM is hallucinating formatting, how do I fix the prompt?"
- "Give me a few-shot pattern for categorizing support tickets."
- "How do I optimize the context window for this 10k token document?"
- "The AI is getting confused by its conversation history, help me rewrite the context."

## Before Starting

Ask context-gathering questions if not provided:

1. **Target LLM:** Which model is being targeted? (e.g., Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) Models react differently to formatting (like XML tags vs JSON).
2. **Goal:** What exactly should the AI output? (e.g., JSON only, conversational text, markdown).
3. **Guardrails:** What must the AI absolutely _never_ do?

## Core Framework

### 1. System Prompt Architecture

| Component               | Purpose                              | Do                                                                                              | Don't                                        |
| ----------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Role/Persona**        | Frames the AI's perspective          | "You are an expert PostgreSQL DBA focusing on query performance."                               | "You are a helpful assistant." (Too generic) |
| **Objective**           | Defines the exact task               | Use imperative verbs: "Analyze the provided code and list 3 bugs."                              | "Can you please maybe look at the code?"     |
| **Rules & Constraints** | Bounds the behavior (The Guardrails) | Provide numbered lists of strict rules: "1. Never use external libraries. 2. Output ONLY JSON." | Mix constraints into giant text paragraphs.  |
| **Tone/Style**          | Guides the language output           | "Professional, concise, and direct. Omit pleasantries."                                         | "Be nice and talkative."                     |

### 2. Few-Shot Prompting Patterns

| Pattern                    | Usage                                                       | Example Structure                                                                |
| -------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Standard Few-Shot**      | Teaching a specific output format to prevent hallucinations | `Input: [X]`<br>`Output: {"result": "Y"}`                                        |
| **Chain-of-Thought (CoT)** | Teaching the AI how to reason before answering              | `Input: [Math Problem]`<br>`Thought: [Step-by-step logic]`<br>`Output: [Answer]` |
| **Negative Examples**      | Explicitly showing the AI what NOT to do                    | `Bad Example Output: [Rambling text]`<br>`Good Example Output: [Concise JSON]`   |
| **Role-play Few-Shot**     | Establishing dynamic conversational tone                    | `User: "I'm angry!"`<br>`Agent: "I understand your frustration."`                |

### 3. Context Window Optimization

| Optimization             | Strategy                                                                                                                       | Why it Works                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Information Ordering** | Place the most critical instructions at the very beginning and the very end of the prompt (the "Needle in a Haystack" effect). | LLMs suffer from "Lost in the Middle" syndrome on long contexts.                               |
| **XML Tagging**          | Wrap data blocks, instructions, and examples in explicit `<tags>`.                                                             | Helps the LLM conceptually separate system instructions from user data.                        |
| **Context Pruning**      | Dynamically remove older, irrelevant conversational turns before sending the prompt.                                           | Saves tokens, speeds up generation, and prevents the LLM from getting confused by old context. |
| **Pre-computation**      | Summarize long reference documents before feeding them into the main prompt.                                                   | Reduces noise and density of the context window.                                               |

## Output Format

When generating prompts for the user, format your response as follows:

1. **The Strategy**: Briefly explain _why_ the prompt is structured the way it is.
2. **The Prompt Block**: Provide the exact prompt inside a Markdown code block, explicitly defining where variables go (e.g. `{{USER_INPUT}}`).
3. **Usage Variables**: A clear list of the variables the user needs to inject into the prompt at runtime.

## Common Mistakes

- ❌ **Politeness**: Begging the AI ("Please could you") wastes tokens. Be imperative and direct.
- ❌ **Negative Constraints (Irony)**: Saying "Do not think about a pink elephant" makes the AI think about it. Instead of "Don't write long intros", say "Start your answer immediately with the code."
- ❌ **Zero-shot for complex formats**: Expecting the LLM to nail a complex, deeply nested JSON structure without providing at least one few-shot example.
- ❌ **Context Stuffing**: Shoving 50 pages of irrelevant documentation into the prompt just because the context window is large enough to hold it.

## Related Skills

- **ai-seo**: Use when the goal is to optimize web pages to be understood by AI search engines, rather than writing prompts for an AI agent.
- **brainstorming**: Use when the user needs to brainstorm ideas, but hasn't reached the stage of actually writing the API prompts yet.
