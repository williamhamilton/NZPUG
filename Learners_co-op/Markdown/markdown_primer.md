

# A Markdown Cheat Sheet

Markdown is a lightweight markup language that allows you to add formatting elements to plaintext documents. Created by John Gruber in 2004, it is now the gold standard for developers, writers, and note-takers.

> [!TIP]
> This guide follows **GitHub Flavored Markdown (GFM)**. While universal for web platforms (GitHub, GitLab, Obsidian, Discord), some advanced features like tables or task lists might not render in basic "Vanilla" Markdown editors.

---

## 1. Structure & Organization

### Headings
Headings organize your document and generate automatic IDs for internal linking.

| Level | Syntax | Preview |
| :--- | :--- | :--- |
| H1 | `# Title` | # Title |
| H2 | `## Section` | ## Section |
| H3 | `### Sub-section` | ### Sub-section |

### Horizontal Rules
Use three or more hyphens, asterisks, or underscores to create a thematic break.
```markdown
---
```

---

## 2. Text Styling

Standard emphasis rules for professional readability.

*   **Bold**: `**Strong**` or `__Strong__` $\rightarrow$ **Strong**
*   **Italic**: `*Emphasis*` or `_Emphasis_` $\rightarrow$ *Emphasis*
*   **Strikethrough**: `~~Mistake~~` $\rightarrow$ ~~Mistake~~
*   **Combined**: `***Extreme***` $\rightarrow$ ***Extreme***
*   **Highlight**: `==Highlighted==` (Note: supported in Obsidian/Notion, not standard GFM).

---

## 3. Lists & Tasks

### Unordered & Ordered
You can mix and match these. Note that for ordered lists, the actual numbers you type don't matter; Markdown increments them automatically.

```markdown
1. First item
1. Second item (I typed '1' again, but it renders as '2')
   - Indent two spaces for sub-bullets
   - Use a hyphen for variety
```

### Task Lists (GFM)
Perfect for project management and "To-Do" logs.
- [x] Write the documentation
- [ ] Get feedback from the team
- [ ] Deploy to production

---

## 4. Assets: Links & Images

### Links
*   **Standard**: `[Google](https://google.com)`
*   **With Hover Text**: `[Google](https://google.com "The Search Engine")`
*   **Internal Anchor**: `[Back to Top](#the-ultimate-markdown-cheat-sheet)` (Lowercase, hyphens instead of spaces).

### Images
The syntax is identical to links, but starts with an exclamation mark.
`![Alt text for screen readers](https://example.com/image.jpg)`

---

## 5. Code & Technical Snippets

### Inline Code
Wrap short snippets in backticks: `` `npm install` ``.

### Code Blocks
Use "fenced" code blocks with triple backticks. Pro tip: Always specify the language for **Syntax Highlighting**.

```python
def greet(name):
    return f"Hello, {name}!"
```

---

## 6. Data Organization (Tables)

Alignment is handled by the placement of colons in the separator row.

| Syntax | Description | Alignment |
| :--- | :---: | ---: |
| `:---` | Left-aligned | Default |
| `:---:` | Centered | Balanced |
| `---:` | Right-aligned | Numbers/Prices |

---

## 7. Advanced GFM Features

### Blockquotes
> "Markdown is intended to be as easy-to-read and easy-to-write as is feasible."
> — *John Gruber*

### Footnotes
Handy for citations without cluttering the body text.
```markdown
This is a claim that needs a source.[^1]

[^1]: This is the source appearing at the bottom.
```

### Math Expressions (LaTeX)
If your editor supports MathJax (like GitHub or Obsidian), use `$` for math.
$E = mc^2$

---

## 8. Pro-Tips & Best Practices

1.  **The "Blank Line" Rule**: When in doubt, add a blank line. Most rendering issues (especially with lists and blockquotes) are solved by giving elements "room to breathe."
2.  **Escape Character**: If you want to show a literal character that Markdown usually uses for formatting (like an asterisk), use the backslash: `\*Not Italic\*`.
3.  **Readability**: Keep your raw text clean. Use one space after `#` and one space after `-` or `1.`.
4.  **Semantic Headings**: Don't use bold text to act as a header. Use actual `#` tags so screen readers and Table of Contents generators can find them.

---
