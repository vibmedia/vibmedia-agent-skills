---
name: data-analysis
description: When the user wants to analyze data, write SQL reports, manipulate datasets with Python pandas, or create charts and visualizations. Trigger on "data analysis," "SQL reporting," "pandas," "data visualization," "sales report," "charting," or "EDA". For backend database schema design, see database-design.
category: analytics
profile: shared
---

# Data Analysis & Reporting

> Comprehensive methodology for extracting insights, cleaning data with Pandas, writing efficient SQL reports, and creating enterprise visualizations.

## When to Use

- "Analyze this CSV and tell me what the trends are"
- "Write a SQL query to get monthly recurring revenue"
- "Clean this dataset using pandas"
- "Create a data visualization for the Q3 sales report"
- "Perform exploratory data analysis on this log file"

## Before Starting

Ask context-gathering questions if not provided:

1. **Goal:** What specific business question are we trying to answer with this data?
2. **Data Structure:** What does the schema or format of the data look like?
3. **Scale:** Are we dealing with small CSVs (pandas in-memory) or massive databases (SQL)?
4. **Audience:** Who is the report/chart for? (Execs need summaries, analysts need details).

## Core Framework

### 1. SQL Reporting Best Practices

| Implementation         | Do                                                                         | Don't                                                |
| ---------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------- |
| **CTEs vs Subqueries** | Use Common Table Expressions (CTEs) for readable, modular logic            | Nest deep subqueries that are impossible to decipher |
| **Aggregations**       | Group by explicit column names (e.g., `GROUP BY department_name`)          | Group by numeric positions (e.g., `GROUP BY 1, 2`)   |
| **Dates**              | Use standardized date truncation (e.g., `DATE_TRUNC('month', created_at)`) | Rely on string manipulation for dates                |
| **Performance**        | Filter early using `WHERE` before joining large tables                     | Join massive tables and filter at the very end       |
| **Null Handling**      | Use `COALESCE(val, 0)` for predictable math operations                     | Leave nulls unhandled in sums and averages           |

### 2. Pandas Data Manipulation Techniques

| Operation        | Do                                                               | Don't                                                  |
| ---------------- | ---------------------------------------------------------------- | ------------------------------------------------------ |
| **Loading Data** | Specify `dtype` and `parse_dates` on load for memory efficiency  | Load massive CSVs with default inferred types          |
| **Iteration**    | Use vectorized operations (`df['A'] + df['B']`)                  | Use `iterrows()` or `apply()` for simple row math      |
| **Filtering**    | Use `.query("age > 30 and city == 'NY'")` for readable filtering | Chain endless bracket subsets `df[(df['age']>30)&...]` |
| **Missing Data** | Use `.fillna()` or `.dropna()` with clear intent                 | Ignore NaNs leading to silent math errors later        |
| **Chaining**     | Use method chaining with `.assign()` for clean pipelines         | Reassign the same dataframe variable 10 times          |

### 3. Enterprise Charting Methodologies

| Chart Type       | Best For                                                             | Anti-Pattern                                            |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------------------------- |
| **Bar / Column** | Comparing categories or showing changes over time (discrete periods) | 3D bar charts or missing zero-baselines                 |
| **Line**         | Time series trends with continuous data points                       | Using line charts for categorical, non-sequential data  |
| **Scatter Plot** | Identifying correlations between two numeric variables               | Overplotting without using transparency (alpha)         |
| **Pie / Donut**  | Showing a small number of parts-to-whole (max 3-4 slices)            | More than 5 slices; comparing values between two pies   |
| **Data Tables**  | When exact numbers matter more than trends                           | Highlighting every single row without conditional logic |

## Output Format

When delivering data analysis or code, structure your response as follows:

1. **Executive Summary**: 1-2 sentences answering the core business question.
2. **Methodology**: Brief explanation of how the data was transformed or queried.
3. **The Code**: The SQL query or Pandas script with clear comments.
4. **Insights / Caveats**: Any data anomalies (e.g., "Note: 10% of rows had missing dates").

## Common Mistakes

- ❌ **Analyzing without a goal**: Diving into code without knowing what question you are answering.
- ❌ **Ignoring data limits**: Trying to load a 10GB CSV into pandas instead of recommending SQL/Spark.
- ❌ **Overcomplicating visuals**: Adding too many colors, 3D effects, or dual y-axes that confuse the reader.
- ❌ **Silent drops**: Using inner joins or `.dropna()` without noting how much data was excluded.

## Related Skills

- **database-design**: Use when designing the underlying schema, table relationships, or ORMs rather than querying existing data.
- **performance-profiling**: Use when optimizing the execution speed of Python scripts or general application performance.
- **seo-audit**: Use when analyzing data specifically related to search engine rankings and web traffic.
