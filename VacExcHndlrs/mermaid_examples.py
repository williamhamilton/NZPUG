### Introduction to Mermaid for Markdown Diagrams

---

### **What is Mermaid?**

#### **Overview of Mermaid**
Mermaid is a JavaScript-based diagramming tool that allows users to create diagrams directly within Markdown. It supports several diagram types, such as flowcharts, sequence diagrams, Gantt charts, and more.

#### **Benefits of Using Mermaid**
- **Integrates seamlessly with Markdown**: Ideal for documentation and README files.
- **Easy to learn**: Uses simple text-based syntax.
- **Dynamic and customisable**: Supports various styles and themes.

#### **Common Use Cases**
- Flowcharts for process visualisation.
- Sequence diagrams for depicting interactions in systems.
- Gantt charts for project timelines.

---

### **Setting Up Mermaid**

#### **Enabling Mermaid in Markdown**
- **GitHub**: Mermaid diagrams are automatically rendered in Markdown files.
- **VS Code**: Use extensions like "Markdown Preview Mermaid Support" to render Mermaid diagrams.

#### **Basic Mermaid Syntax**
```markdown
```mermaid
flowchart TD
    A --> B
    B --> C
    C --> D
```
- **Backticks** (` ``` `) denote code blocks.
- **`mermaid`** specifies the Mermaid block.
- **Flowchart TD**: Defines a top-down flowchart.

```mermaid
flowchart TD
    A --> B
    B --> C
    C --> D
```

---

### **Creating Basic Diagrams**

#### **Flowcharts**
- **Syntax**: 
  ```mermaid
  flowchart LR
      A[Start] --> B[Process]
      B --> C{Decision}
      C -->|Yes| D[End]
      C -->|No| E[Another Process]
  ```
  - **Nodes**: `A[Text]`, `C{Text}`.
  - **Links**: `-->`, `-->|Text|`.

#### **Sequence Diagrams**
- **Syntax**:
  ```mermaid
  sequenceDiagram
      participant A as Alice
      participant B as Bob
      A->>B: Hello Bob
      B-->>A: Hi Alice
  ```
  - **Participants**: `participant A as Alice`.
  - **Messages**: `A->>B: Hello Bob`.

#### **Exercise**
- Create a flowchart that depicts a decision-making process.
- Create a sequence diagram showing a simple interaction.

---

### **Customising Diagrams**

#### **Basic Customisation**
- Change **node shapes** using different brackets:
  - `[Text]` for rectangles.
  - `{Text}` for diamonds (decision points).
- **Colours and themes**: Use class definitions or themes for styling.

#### **Example**:
```mermaid
flowchart TD
    classDef blue fill:#1f77b4,color:#ff;
    A[Start]:::blue --> B[Process]
```
Using with Themes and themeVariables

https://mermaid.js.org/config/theming.html
```mermaid
%%{init: {'theme':'neutral'}}%%
flowchart LR
    A[Start] --> B{Decision Point}
    B -->|Yes| C[Positive Outcome]
    B -->|No| D[Negative Outcome]
    
    C --> E[Further Action]
    D --> F[Alternative Action]

    subgraph SubProcess1
        E --> G[Step 1]
        G --> H[Step 2]
    end

    subgraph SubProcess2
        F --> I[Step A]
        I --> J[Step B]
    end

    class A,B,C,D,E,F positive;
    class G,H,I,J negative;
```

```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#FF5733',
      'primaryTextColor': '#ffffff',
      'primaryBorderColor': '#C70039',
      'lineColor': '#FFC300',
      'secondaryColor': '#28A745',
      'tertiaryColor': '#DAF7A6'
    }
  }
}%%
flowchart LR
    A[Start] --> B{Decision Point}
    B -->|Yes| C[Positive Outcome]
    B -->|No| D[Negative Outcome]
    
    C --> E[Further Action]
    D --> F[Alternative Action]

    subgraph SubProcess1
        E --> G[Step 1]
        G --> H[Step 2]
    end

    subgraph SubProcess2
        F --> I[Step A]
        I --> J[Step B]
    end

    class A,B,C,D,E,F positive;
    class G,H,I,J negative;
```

---

### **Quick Tips and Best Practices**

#### **Best Practices**
- Keep diagrams simple for readability.
- Use meaningful labels and consistent shapes.
- Use Mermaid's inline documentation for complex diagrams.

#### **Troubleshooting**
- **Syntax errors**: Ensure correct brackets and symbols.
- **Rendering issues**: Check if Mermaid is enabled in the Markdown viewer.

#### **Additional Resources**
- [Mermaid Official Documentation](https://mermaid-js.github.io/mermaid/#/)
- Markdown editor plugins with Mermaid support.

---


---

### A couple that I am using to confirm existing process for a client
```mermaid
graph TD
A[Start - cmdProcess_Click] --> B{Share Reconciliation OK?}
B -- No --> C(Display Share Mismatch Message)
C --> D(Open Investment Summary Report)
D --> G[Exit Sub]
B -- Yes --> E{Display Confirmation to Proceed}
E -- No --> G
E -- Yes --> F{Backup Taken?}
F -- No --> G
F -- Yes --> H{Queries Printed?}
H -- No --> G
H -- Yes --> I(Run Query: Copy Prior Data)
I --> J(Run Query: Update Current Data)
J --> K(Run Query: Update Total Shares)
K --> L(Display Completion Message)
L --> M[Call cmdExit_Click]
M --> G
G[End]
```
```mermaid
flowchart TD
A[Start Tax Letter Processing] --> B{EOY Processing Completed?}
B -- No --> C[Display Error & Cancel]
B -- Yes --> D{Previous Year File Exists?}
D -- No --> E[Create New Tax Letter File]
D -- Yes --> F(Rename & Create New File)
F --> G(Prompt for Investment Data Import)
G --> H{Data Imported?}
H -- Yes --> I(Generate Tax Letters)
I --> J(Check Formatting Errors)
J -- No --> K(Generate Reports & PDFs)
K --> L[Backup Database]
J -- Yes --> M[Restart Process]
```
## Other examples
### Gantt Chart
```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %b %d, %Y

    section Planning
    Task A       :a1, 2025-01-01, 5d
    Task B       :after a1, 3d

    section Development
    Task C       :c1, 2025-01-08, 7d
    Task D       :after c1, 4d

    section Testing
    Task E       :2025-01-20, 3d
    Task F       :2025-01-23, 2d

    section Deployment
    Task G       :2025-01-26, 1d
```

### Class Diagram
```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }

    class Dog {
        +String breed
        +bark()
    }

    class Cat {
        +String color
        +meow()
    }

    Animal <|-- Dog
    Animal <|-- Cat
```

### Entity Relationship Diagram
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER {
        string name
        string address
        string phone
    }
    ORDER {
        int order-number
        string date
    }
    LINE-ITEM {
        int quantity
        float price
    }
```

### Pie Chart
Try with pie showData or just pie

```mermaid
%%{init: {"pie": {"textPosition": 0.5}, "theme":"forest"} }%%
pie showData
    title Distribution of Sales
    "Product A" : 45
    "Product B" : 25
    "Product C" : 15
    "Product D" : 35
```

### State Diagram
```mermaid
%%{init: {'theme':'neutral'}}%%
stateDiagram
    [*] --> S1
    S1 --> S2 : Transition1
    S1 --> S3 : Transition2
    S2 --> [*]
    S3 --> S2
```

### Network Diagram
```mermaid
%%{init: {'theme':'base'}}%%
graph TD
    A[Client] --> B[Load Balancer]
    B --> C[Server1]
    B --> D[Server2]
    B --> E[Server3]
```

### Sequence Diagram
```mermaid
sequenceDiagram
    participant A as Alice
    participant B as Bob
    A->>B: Hello Bob
    B-->>A: Hi Alice
```

### Git Diagram
```mermaid
gitGraph
    commit id: "Initial Commit"
    branch dev
    commit id: "Dev Commit 1"
    commit id: "Dev Commit 2"
    checkout main
    merge dev id: "Merge Dev into Main"
    commit id: "Main Commit 1"
```

### Journey Diagram
```mermaid
journey
    title User Journey
    section Sign-Up
      Start: 5: User
      Fill Form: 3: User
      Submit Form: 4: User
    section Onboarding
      Welcome Email: 5: System
      Complete Profile: 2: User
      First Purchase: 4: User
```

