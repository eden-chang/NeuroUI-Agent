# NeuroUI Agent

An LLM-powered agent that recommends accessible UI components for neurodivergent users. It searches the [NeuroUI](https://github.com/eden-chang/NeuroUI) component library, references cognitive science-based accessibility guidelines, and generates ready-to-use code — all through natural language.

Built with the Anthropic Claude API using the tool-use (function calling) pattern, without any agent frameworks.

## Why This Exists

Neurodivergent users (ADHD, autism, dyslexia, sensory sensitivity) interact with interfaces differently. Designing for them requires understanding cognitive science principles — not just following a checklist. This agent bridges that gap by combining a component library with research-backed guidelines, so developers get recommendations grounded in *why* something works, not just *what* to use.

## Architecture

```
User Input
    │
    ▼
Claude API (tool-use loop)
    │
    ├── search_components()  →  NeuroUI Component Catalog (15 components)
    │
    ├── get_guidelines()     →  Cognitive Science Guidelines (5 conditions)
    │
    └── generate_component_code()  →  Import + Usage Code Generation
    │
    ▼
Reasoned Recommendation with Code
```

The agent runs an agentic loop: it receives a user request, decides which tools to call (and in what order), processes the results, and generates a final response that includes cognitive science reasoning and working code.

## Components & Conditions

**15 NeuroUI components** in the catalog:

| Category | Components |
|----------|-----------|
| Action | Button |
| Form | Input, Select, Checkbox, Radio/RadioGroup |
| Layout | Card |
| Navigation | Tabs, Navigation |
| Feedback | Alert, Badge, Toast |
| Overlay | Dialog, Tooltip |
| Disclosure | Accordion |
| Data Display | Table |

**5 neurodiversity conditions** with guidelines:

- **ADHD** — executive function, working memory, sustained attention
- **Autism** — predictive processing, sensory integration
- **Dyslexia** — phonological processing, reading demands
- **Sensory Sensitivity** — sensory overload, motion/flash safety
- **Motor Impairment** — keyboard access, target sizing

## Setup

### Prerequisites

- Python 3.10+
- Anthropic API key ([console.anthropic.com](https://console.anthropic.com))

### Install

```bash
git clone https://github.com/eden-chang/NeuroUI-Agent.git
cd neuroui-agent
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env
```

### Run

```bash
python main.py
```

## Example

```
You: I need a task management component for users with ADHD

Agent is thinking...

  [Tool Call] get_guidelines({"condition": "ADHD"})
  [Tool Call] search_components({"query": "task", "condition": "ADHD"})
  [Tool Call] generate_component_code({"component_id": "card", ...})
  [Tool Call] generate_component_code({"component_id": "checkbox"})
  [Tool Call] generate_component_code({"component_id": "badge"})
  [Tool Call] generate_component_code({"component_id": "button"})

Agent:

  import { Card, Checkbox, Badge, Button } from '@neuroui/components';

  <Card variant="outlined" interactive>
    <Card.Header>
      <Checkbox label={task.title} checked={task.completed} />
      <Badge variant={task.priority === 'high' ? 'error' : 'warning'}>
        {task.priority}
      </Badge>
    </Card.Header>
    <Card.Footer>
      <Button variant="ghost" size="sm">Edit</Button>
    </Card.Footer>
  </Card>

  Why This Combination Works for ADHD:
  - Single-task focus: Each card represents one clear unit of work
  - Immediate feedback: Checkbox state changes instantly
  - Clear visual hierarchy: Card + Badge priorities reduce mental effort
  - Progress visibility: Completed checkboxes provide dopamine feedback
```

See [`examples/demo_output.md`](examples/demo_output.md) for full outputs across ADHD, autism, dyslexia, and general neurodivergent use cases.

## Project Structure

```
neuroui-agent/
├── main.py              # CLI entry point
├── agent.py             # Agent loop (Claude API tool-use)
├── tools.py             # Tool functions (search, guidelines, codegen)
├── data/
│   ├── components.json  # NeuroUI component catalog
│   └── guidelines.json  # Cognitive science guidelines
├── examples/
│   └── demo_output.md   # Sample outputs
├── requirements.txt
└── .env.example
```

## Tech Stack

- **Python 3.10+**
- **Anthropic Claude API** — tool-use / function calling pattern
- **NeuroUI** — accessible React component library with cognitive accessibility built in

No agent frameworks (LangChain, etc.). The agentic loop is implemented directly with the Anthropic SDK to demonstrate understanding of how tool-use agents work at a fundamental level.

## Future Work

- Web interface (FastAPI + React frontend)
- Multi-turn conversation memory
- Component composition suggestions (combining multiple components)
- User preference profiles for personalized recommendations
- Integration with NeuroUI's `@neuroui/core` adaptive settings
