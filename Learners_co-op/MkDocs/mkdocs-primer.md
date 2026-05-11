
# MkDocs Primer: From Markdown to Documentation Site

Think of MkDocs as your publishing pipeline:

*   **Markdown files** = your content
*   **`mkdocs.yml`** = site behaviour and navigation
*   **Theme + extensions** = visual style and specialised rendering features

## 1. Why use MkDocs?

Markdown is excellent for individual notes, but MkDocs adds site-level capabilities:

*   **Navigation:** organise pages into clear menus.
*   **Search:** built-in instant site search.
*   **Styling:** apply a consistent theme (the "Material" theme is widely used).
*   **Extensions:** support for task lists, footnotes, math, Mermaid, and admonitions.

## 2. Quick Start

Run these commands in your terminal to start a local project:

### Recommended: use a virtual environment first

Proper OS
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```
Windows
```bash
python -m venv .venv
source .venv\Scripts\activate
python -m pip install --upgrade pip
```
### Install and run MkDocs

```bash
python -m pip install mkdocs-material
mkdocs new my-project
cd my-project
mkdocs serve
```

The preview is usually available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) while the local server is running.

### Optional: pin docs dependencies

Create a `requirements-docs.txt` file so everyone in the group installs the same docs tooling versions.

```text
mkdocs-material
```

Then install with:

```bash
python -m pip install -r requirements-docs.txt
```

## 3. Project Structure

MkDocs expects all your content files to live inside the `docs/` folder:

```text
my-project/
├── mkdocs.yml            # The configuration file
└── docs/                 # All .md files go in here
    ├── index.md          # Your home page
    ├── markdown_primer.md
    ├── mkdocs-primer.md
    ├── mermaid_examples.md
    └── javascripts/      # Custom scripts
        └── mermaid-init.js
```

## 4. Feature Mapping: Markdown to MkDocs

Use this when something works on GitHub but not in your local docs site. This map tells you which extension needs enabling in your configuration.

| Feature | Example file | Setting required |
| :--- | :--- | :--- |
| **Tables** | `markdown_primer.md` | `tables` |
| **Task lists** (`- [x]`) | `markdown_primer.md` | `pymdownx.tasklist` |
| **Footnotes** (`[^1]`) | `markdown_primer.md` | `footnotes` |
| **Math** (`$...$`) | `markdown_primer.md` | `pymdownx.arithmatex` + MathJax |
| **Highlight** (`==text==`) | `markdown_primer.md` | `pymdownx.mark` |
| **Admonitions** (`!!! note`) | learner exercises | `admonition` + `pymdownx.details` |
| **Mermaid diagrams** | `mermaid_examples.md` | `pymdownx.superfences` + Mermaid JS |

## 5. Standard `mkdocs.yml` for the Co-op

Use this baseline for your learner projects. It ensures all previous unit examples render correctly.

```yaml
site_name: Learners Co-op Docs
site_url: https://your-github-handle.github.io/repository-name/

theme:
  name: material
  features:
    - navigation.tabs
    - search.suggest
    - content.code.copy

nav:
  - Home: index.md
  - Writing:
      - Markdown Primer: markdown_primer.md
      - MkDocs Primer: mkdocs-primer.md
  - Diagrams:
      - Mermaid Examples: mermaid_examples.md

markdown_extensions:
  - admonition
  - attr_list
  - footnotes
  - tables
  - pymdownx.details
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.mark
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format

extra_javascript:
  - https://unpkg.com/mermaid@11/dist/mermaid.min.js
  - javascripts/mermaid-init.js
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

### YAML pitfalls to avoid

*   Use spaces, not tabs.
*   Keep indentation consistent (especially under `nav:` and `markdown_extensions:`).
*   Copy carefully: one extra space can break the build.

### Essential: Creating the Mermaid Helper
For diagrams to render, you must create `docs/javascripts/mermaid-init.js` with this code:

```javascript
document$.subscribe(function () {
  mermaid.initialize({ startOnLoad: true });
});
```

## 6. File naming and nav stability

To reduce broken links and 404s:

*   Prefer lowercase, hyphenated file names (for example, `data-cleaning.md`).
*   Avoid spaces and mixed case in file names.
*   Ensure each `nav` path exactly matches the file in `docs/`.

Example:

*   Better: `docs/mermaid-examples.md` and `- Mermaid Examples: mermaid-examples.md`
*   Risky: `docs/Mermaid Examples.md` and `- Mermaid Examples: mermaid_examples.md`

## 7. Images and asset paths

Store images under `docs/images/` and link them relative to the current page.

```markdown
![Process overview](images/process-overview.png)
```

If an image does not render, check the folder name, file name, and case.

## 8. Callouts: GitHub vs MkDocs

A common point of confusion:
*   GitHub callouts use `> [!TIP]` syntax.
*   MkDocs Material uses "Admonitions".

**Always prefer admonitions for your documentation pages:**

```markdown
!!! tip "Pro tip"
    Use `!!!` for a standard block.
    Use `???` for a collapsible block (useful for "hidden" answers).
```

## 9. Troubleshooting

*   **Mermaid shows as raw code:** check `pymdownx.superfences` is in the config and confirm `docs/javascripts/mermaid-init.js` exists.
*   **Math shows raw `$...$`:** confirm both `pymdownx.arithmatex` and the MathJax script are in the config.
*   **404 from navigation:** ensure the file path in the `nav` section matches the file under `docs/` exactly.

## 10. Build and Publish

```bash
# Creates a 'site/' folder with your static HTML
mkdocs build

# Publishes directly to GitHub Pages
mkdocs gh-deploy
```

`mkdocs gh-deploy` publishes to a GitHub Pages branch. It is safest to run it when your work is committed and your local branch is clean.

## 10.1 Daily workflow (three-step loop)

1.  Start preview: `mkdocs serve`
2.  Edit your Markdown and `mkdocs.yml`
3.  Watch terminal warnings and fix issues immediately

## 11. Learner Exercises

1.  **Style Update:** Convert one `> [!TIP]` block in your old notes to `!!! tip` syntax.
2.  **Expansion:** Add a new file `docs/extra.md`, add it to the `nav`, and confirm it appears in the menu.
3.  **Visuals:** Add one sequence diagram and one class diagram from last week's Mermaid work to a new "Gallery" page.
4.  **Error Handling:** Intentionally misspell a file name in the `nav` section, observe the error in your terminal, then fix it.

## 12. Maintainability checklist

Before publishing, quickly check:

*   Navigation includes all new pages.
*   One topic per page, with clear headings.
*   Admonition style is consistent across pages.
*   Links and images render correctly in local preview.

https://github.com/mkdocs/catalog


