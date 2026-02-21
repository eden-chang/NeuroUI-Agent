# NeuroUI Agent — Demo Output

## Example 1: ADHD Task Management

```
You: I need a task management component for users with ADHD

Agent is thinking...

  [Tool Call] get_guidelines({"condition": "ADHD"})
  [Tool Call] search_components({"query": "task", "condition": "ADHD"})
  [Tool Call] generate_component_code({"component_id": "card"})
  [Tool Call] generate_component_code({"component_id": "checkbox"})

Agent: Based on cognitive science principles for ADHD, I recommend combining
the **Card** and **Checkbox** components from NeuroUI. Here's why:

### Cognitive Science Reasoning

ADHD affects executive function and working memory. The prefrontal cortex shows
reduced activity, making it harder to maintain focus on multi-step tasks. Our UI
needs to **externalize cognitive scaffolding** — providing structure that
compensates for difficulties in self-regulation.

### Recommended Components

1. **Card** — Use as a container for each task group. The `variant="outlined"`
   style creates clear visual boundaries that help segment information, reducing
   demands on working memory.

2. **Checkbox** — For individual task items. The clear label and visual
   completion state provides **immediate feedback**, which is critical for ADHD
   users who benefit from external reward signals.

### Code

import { Card, Checkbox } from '@neuroui/components';

<Card variant="outlined">
  <Card.Header>Today's Tasks</Card.Header>
  <Card.Body>
    <Checkbox label="Review pull request" />
    <Checkbox label="Update documentation" />
    <Checkbox label="Run test suite" />
  </Card.Body>
</Card>
```

## Example 2: Autistic User Notification System

```
You: What notification system would work best for autistic users?

Agent is thinking...

  [Tool Call] get_guidelines({"condition": "autism"})
  [Tool Call] search_components({"query": "notification", "condition": "autism"})
  [Tool Call] generate_component_code({"component_id": "toast"})
  [Tool Call] generate_component_code({"component_id": "alert"})

Agent: For autistic users, I recommend using the **Toast** system for transient
notifications and **Alert** for persistent messages. Here's the reasoning:

### Cognitive Science Reasoning

Autism involves differences in predictive processing. The brain's ability to
form and update predictive models may work differently, making **unexpected
changes particularly disruptive**. Additionally, sensory processing differences
mean that stimuli that are neutral for neurotypical users may be overwhelming.

### Recommended Approach

1. **Toast** — The timing-aware duration system adapts to user preferences:
   patient mode shows toasts for 10 seconds (more processing time), and density
   mode limits visible toasts to 1 in minimal mode, preventing sensory overload.

2. **Alert** — For important information that shouldn't disappear. The explicit
   state indicators (icons + text + color) provide **multimodal cues** rather
   than relying on implicit signals.

### Code

import { ToastProvider, Toaster, useToast, Alert } from '@neuroui/components';

// Wrap your app
<ToastProvider>
  <App />
  <Toaster />
</ToastProvider>

// In your component
const { toast } = useToast();
toast({
  title: 'Document saved',
  description: 'Your changes have been saved successfully.',
  variant: 'success'
});

// For persistent critical info
<Alert variant="warning" title="Maintenance scheduled" closable>
  The system will be unavailable on March 1st from 2-4 PM.
</Alert>
```
