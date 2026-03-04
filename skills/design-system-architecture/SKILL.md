---
name: design-system-architecture
description: When the user wants to build a design system, integrate Figma syncing, or enforce strict UI component token management for frontend teams. Trigger on "design system", "Figma sync", "design tokens", "component library", "storybook".
category: frontend
profile: dev
---

# Design System Architecture

> Blueprint for establishing robust, token-driven, scalable UI architectures bridging the gap between designers (Figma) and engineers (React/CSS/Tailwind).

## When to Use

- "Create a token architecture for our new dark mode."
- "How do I sync Figma variables over to my Tailwind config?"
- "We are building a React Native + Web component library, how do we structure the props?"
- "What is the best way to document components for marketing developers?"
- "Define a color palette token system using base, semantic, and component tiers."

## Before Starting

Ask context-gathering questions if not provided:

1. **Source of Truth:** Is Figma the source of truth, or is the code repo the source of truth for the design tokens?
2. **Framework Alignment:** What UI framework are they using? (Tailwindcss v4, Vanilla Extract, Styled Components, CSS Modules, React Native StyleSheet).
3. **Usage:** Is this an internal company monorepo, or an open-source library distributed via NPM?

## Core Framework

### 1. Token Tiering Strategy

| Tier                 | Purpose                                                                          | Example                                                                   | Anti-Pattern                                                         |
| -------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Core / Base**      | Raw values representing the brand scale.                                         | `color-blue-500: #3B82F6` <br> `spacing-md: 16px`                         | Hardcoding hex codes directly into CSS classes or style sheets.      |
| **Semantic / Alias** | Contextual meaning for core tokens.                                              | `color-primary: {color-blue-500}` <br> `color-success: {color-green-500}` | `color-button: #3B82F6` (Tying semantic alias directly to hex).      |
| **Component**        | Specific tokens restricted to a single component (optional for massive systems). | `button-bg-hover: {color-primary}` <br> `card-shadow: {elevation-high}`   | Overloading semantic tokens for one component's weird design choice. |

### 2. Figma to Code Synchronization

| Strategy                | Do                                                                                                                        | Don't                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Figma Variables**     | Map Figma Variables (colors, spacing, radii) directly to CSS/Tailwind variables.                                          | Rely on handoff tools to inspect raw hex codes during every PR.              |
| **Automation Workflow** | Use a tool (like Style Dictionary or Figma REST API Actions) to transform JSON tokens into CSS/SCSS/TS variables on push. | Manually update `tailwind.config.js` every time a designer nudges a hex hue. |
| **Iconography**         | Export SVGs from a dedicated Figma icon library into a React SVG component generator (like SVGR).                         | Copy-pasting random unoptimized `<svg>` blobs into JSX files.                |

### 3. Component Library API Design (React)

| Best Practice            | Implementation Guideline                                                                                                | Common Mistake                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Polymorphism**         | Use the `as` prop to allow semantic HTML rendering (e.g., render a Button as an `<a>` tag for SEO).                     | Creating an entirely separate `LinkButton` component.                       |
| **Variant Props**        | Use tools like CVA (Class Variance Authority) to type-safely define `intent` (primary/secondary) and `size` (sm/md/lg). | Managing 15 distinct boolean flags (e.g., `<Button isPrimary isLarge />`).  |
| **Accessibility (a11y)** | Ensure interactive components forward refs (`forwardRef`) and implement native ARIA attributes.                         | Ignoring keyboard navigation and screen reader support on custom dropdowns. |

## Output Format

When providing design system guidance or token architectures, structure the response as follows:

1. **Architecture Intent**: A brief summary of why you chose a specific token structure.
2. **Token JSON/CSS**: The raw token outputs (e.g., CSS Variables or Tailwind v4 `@theme` configuration).
3. **Component Structure**: The API of the React/HTML component, highlighting prop design.
4. **Handoff Process**: A note on how designers should update this in Figma.

## Common Mistakes

- ❌ **Building everything from scratch**: Re-inventing accessible primitives (Modals, Selects, Accordions) instead of using headless UI libraries like Radix UI or React Aria.
- ❌ **The "Everything is a prop" anti-pattern**: Making a single `<Card />` component take 40 props for text alignment, border color, and padding instead of composing smaller subcomponents (`<Card.Header>`, `<Card.Body>`).
- ❌ **Ignoring Dark Mode**: Hardcoding hex colors instead of using semantic variables (`var(--bg-primary)`) that flip based on system themes.
- ❌ **Lack of Isolation**: Developing components directly inside the main application without using Storybook or a dedicated playground, leading to tightly coupled domain logic.

## Related Skills

- **frontend-design**: Use when making specific aesthetic choices (typography scales, color harmony) rather than building the architecture/infrastructure to support those aesthetics.
- **tailwind-patterns**: Use when the focus is strictly on Tailwind configuration rather than the theoretical bridge between Figma and code.
