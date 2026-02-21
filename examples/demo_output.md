# NeuroUI Agent — Demo Output

*These are real, unedited responses from the NeuroUI Agent.*

---

## Example 1: ADHD Task Management

**Prompt:** "I need a task management component for users with ADHD"

**Tool calls:**
```
[Tool Call] get_guidelines({"condition": "ADHD"})
  [Tool Call] search_components({"query": "task", "condition": "ADHD"})
  [Tool Call] generate_component_code({"component_id": "card", "custom_props": {"variant": "outlined", "interactive": true}})
  [Tool Call] generate_component_code({"component_id": "checkbox"})
  [Tool Call] generate_component_code({"component_id": "badge"})
  [Tool Call] generate_component_code({"component_id": "button"})
```

**Agent response:**

## Complete Task Management Example

```jsx
import { Card } from '@neuroui/components';
import { Checkbox } from '@neuroui/components';
import { Badge } from '@neuroui/components';
import { Button } from '@neuroui/components';

function TaskList() {
  const [tasks, setTasks] = React.useState([
    { id: 1, title: "Review project documentation", completed: false, priority: "high" },
    { id: 2, title: "Reply to client email", completed: false, priority: "medium" },
    { id: 3, title: "Update design mockups", completed: true, priority: "low" }
  ]);

  const handleToggle = (taskId) => {
    setTasks(tasks.map(task => 
      task.id === taskId ? { ...task, completed: !task.completed } : task
    ));
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {tasks.map(task => (
        <Card key={task.id} variant="outlined" interactive>
          <Card.Header>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <Checkbox 
                label={task.title}
                checked={task.completed}
                onChange={() => handleToggle(task.id)}
              />
              <Badge variant={
                task.priority === 'high' ? 'error' : 
                task.priority === 'medium' ? 'warning' : 
                'info'
              }>
                {task.priority}
              </Badge>
            </div>
          </Card.Header>
          {/* Optional: Add more details in Body */}
          <Card.Footer>
            <Button variant="ghost" size="sm">Edit</Button>
            <Button variant="ghost" size="sm">Delete</Button>
          </Card.Footer>
        </Card>
      ))}
    </div>
  );
}
```

## Why This Combination Works for ADHD:

✅ **Single-task focus**: Each card represents one clear unit of work  
✅ **Immediate feedback**: Checkbox state changes instantly  
✅ **Clear visual hierarchy**: Card structure + Badge priorities provide organization without mental effort  
✅ **Reduced clutter**: One task per card minimizes competing visual stimuli  
✅ **Progress visibility**: Completed checkboxes provide dopamine feedback (important for ADHD motivation)  
✅ **No autoplay or motion distractions**: All components use motion-safe principles  

## Alternative: **Accordion Component**

If you need to manage many tasks in limited space, the **Accordion** component is another excellent choice:

```jsx
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@neuroui/components';

<Accordion type="single">
  <AccordionItem value="task-1">
    <AccordionTrigger value="task-1">
      <Checkbox label="Review project documentation" />
    </AccordionTrigger>
    <AccordionContent value="task-1">
      {/* Task details, notes, subtasks */}
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

This uses **progressive disclosure** to hide non-essential details, further reducing cognitive load by only showing what's relevant at each moment.

Would you like me to generate code for any additional features, like timer integration or progress tracking?

---

## Example 2: Autistic User Notification System

**Prompt:** "What notification system would work best for autistic users?"

**Tool calls:**
```
[Tool Call] get_guidelines({"condition": "autism"})
  [Tool Call] search_components({"query": "notification", "condition": "autism"})
  [Tool Call] generate_component_code({"component_id": "toast", "custom_props": {"title": "Settings saved", "description": "Your preferences have been updated successfully", "variant": "success", "closable": true}})
```

**Agent response:**

## Implementation Code:

```tsx
// 1. Wrap your app with ToastProvider (typically in your root layout/App.tsx)
import { ToastProvider, Toaster } from '@neuroui/components';

function App() {
  return (
    <ToastProvider>
      {/* Your app content */}
      <YourContent />
      
      {/* Add the Toaster component to render notifications */}
      <Toaster />
    </ToastProvider>
  );
}

// 2. Use the toast hook in your components
import { useToast } from '@neuroui/components';

function YourComponent() {
  const { toast } = useToast();
  
  const handleSave = () => {
    // Perform save operation...
    
    // Show success notification
    toast({
      title: 'Settings saved',
      description: 'Your preferences have been updated successfully',
      variant: 'success',
      closable: true
    });
  };
  
  const handleError = () => {
    toast({
      title: 'Error occurred',
      description: 'Please try again or contact support',
      variant: 'error',
      duration: 10000, // Keep error messages visible longer
      closable: true,
      action: {
        label: 'Retry',
        onClick: () => handleSave()
      }
    });
  };
  
  return (
    <button onClick={handleSave}>Save Settings</button>
  );
}
```

## Additional Best Practices:

1. **Use descriptive titles**: Be explicit and literal (avoid metaphors or ambiguous language)
2. **Provide context in descriptions**: Explain what happened and what comes next
3. **Consider longer durations**: Override the default with longer durations for complex messages
4. **Include action buttons**: When appropriate, provide clear next steps rather than forcing users to figure out what to do
5. **Consistent patterns**: Use the same notification approach throughout your app to build predictable expectations

This notification system respects the cognitive science behind autism—it provides explicit, clear communication without sensory overwhelm or disruption to established patterns.

---

## Example 3: Dyslexia Reading App

**Prompt:** "I'm building a reading app for users with dyslexia. What components should I use?"

**Tool calls:**
```
[Tool Call] get_guidelines({"condition": "dyslexia"})
  [Tool Call] search_components({"query": "reading", "condition": "dyslexia"})
  [Tool Call] search_components({"query": "text", "condition": "dyslexia"})
  [Tool Call] search_components({"query": "font", "condition": "dyslexia"})
  [Tool Call] search_components({"query": "spacing", "condition": "dyslexia"})
  [Tool Call] search_components({"query": "settings", "condition": "dyslexia"})
  [Tool Call] search_components({"query": "button", "condition": "dyslexia"})
  [Tool Call] search_components({"query": "slider", "condition": "dyslexia"})
  [Tool Call] generate_component_code({"component_id": "select", "custom_props": {"label": "Font Size", "options": [{"value": "small", "label": "Small (16px)"}, {"value": "medium", "label": "Medium (18px)"}, {"value": "large", "label": "Large (20px)"}, {"value": "xlarge", "label": "Extra Large (24px)"}]}})
  [Tool Call] generate_component_code({"component_id": "card"})
  [Tool Call] generate_component_code({"component_id": "button"})
  [Tool Call] generate_component_code({"component_id": "tabs"})
  [Tool Call] generate_component_code({"component_id": "accordion"})
```

**Agent response:**

## **Ready-to-Use Code:**

```jsx
// Import all necessary components
import { Card, Select, Button, Tabs, TabList, Tab, TabPanel, Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@neuroui/components';

// Reading App with Customization Panel
function ReadingApp() {
  const [fontSize, setFontSize] = useState('medium');
  const [lineSpacing, setLineSpacing] = useState('normal');
  const [fontFamily, setFontFamily] = useState('sans-serif');
  
  return (
    <Tabs defaultValue="reading">
      <TabList>
        <Tab value="reading">📖 Read</Tab>
        <Tab value="settings">⚙️ Settings</Tab>
        <Tab value="library">📚 Library</Tab>
      </TabList>
      
      {/* Reading View */}
      <TabPanel value="reading">
        <Card variant="outlined">
          <Card.Header>
            <h2>Chapter 1: Introduction</h2>
          </Card.Header>
          <Card.Body>
            <p>Your main reading content goes here...</p>
            
            {/* Optional/supplementary content */}
            <Accordion type="single">
              <AccordionItem value="footnote-1">
                <AccordionTrigger value="footnote-1">
                  📝 Footnote 1
                </AccordionTrigger>
                <AccordionContent value="footnote-1">
                  Additional context that doesn't clutter the main text
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          </Card.Body>
          <Card.Footer>
            <Button variant="outline">← Previous</Button>
            <Button variant="primary">Next →</Button>
          </Card.Footer>
        </Card>
      </TabPanel>
      
      {/* Settings Panel */}
      <TabPanel value="settings">
        <Card variant="outlined">
          <Card.Header>
            <h2>Reading Preferences</h2>
          </Card.Header>
          <Card.Body>
            {/* Font Size Selector */}
            <Select 
              label="Font Size" 
              hint="Larger text reduces reading fatigue"
              options={[
                {value: 'small', label: 'Small (16px)'}, 
                {value: 'medium', label: 'Medium (18px)'}, 
                {value: 'large', label: 'Large (20px)'}, 
                {value: 'xlarge', label: 'Extra Large (24px)'}
              ]}
              value={fontSize}
              onChange={(e) => setFontSize(e.target.value)}
            />
            
            {/* Line Spacing */}
            <Select 
              label="Line Spacing" 
              hint="More space between lines improves readability"
              options={[
                {value: 'compact', label: 'Compact (1.3)'}, 
                {value: 'normal', label: 'Normal (1.5)'}, 
                {value: 'relaxed', label: 'Relaxed (1.8)'}, 
                {value: 'loose', label: 'Loose (2.0)'}
              ]}
              value={lineSpacing}
              onChange={(e) => setLineSpacing(e.target.value)}
            />
            
            {/* Font Family */}
            <Select 
              label="Font Style" 
              hint="Sans-serif fonts are easier to read"
              options={[
                {value: 'sans-serif', label: 'Sans Serif (Recommended)'}, 
                {value: 'opendyslexic', label: 'OpenDyslexic'}, 
                {value: 'comic-sans', label: 'Comic Sans'}
              ]}
              value={fontFamily}
              onChange={(e) => setFontFamily(e.target.value)}
            />
            
            {/* Color Scheme */}
            <Select 
              label="Color Theme" 
              hint="Avoid pure black on white for less visual stress"
              options={[
                {value: 'cream', label: 'Cream Background'}, 
                {value: 'blue-tint', label: 'Blue Tint'}, 
                {value: 'gray', label: 'Gray Background'},
                {value: 'dark', label: 'Dark Mode'}
              ]}
            />
          </Card.Body>
          <Card.Footer>
            <Button variant="primary">💾 Save Preferences</Button>
          </Card.Footer>
        </Card>
      </TabPanel>
      
      {/* Library View */}
      <TabPanel value="library">
        <Card variant="outlined">
          <Card.Header>
            <h2>Your Library</h2>
          </Card.Header>
          <Card.Body>
            {/* Book list would go here */}
          </Card.Body>
        </Card>
      </TabPanel>
    </Tabs>
  );
}
```

---

## **Key Design Principles Applied:**

1. **Reduced Phonological Demands**: Icons (📖, ⚙️, 📚) paired with text provide visual cues that reduce reliance on reading for navigation

2. **Progressive Disclosure**: Accordion hides footnotes/references until needed, keeping the main reading area clean

3. **User Control**: Select components give users power over their reading environment (font, spacing, colors) — critical because dyslexia presents differently for each individual

4. **Structured Layout**: Card components create clear visual boundaries and predictable sections

5. **Multimodal Communication**: Hints on Select components explain WHY each option matters, supporting informed decision-making

6. **Cognitive Load Management**: Tabs separate concerns (reading vs. settings) so users aren't overwhelmed by options while trying to focus on content

7. **Motion-Safe**: All components use subtle, non-distracting animations that won't cause visual stress during extended reading sessions

---

## **Additional Recommendations:**

1. **Store preferences in localStorage** so users don't have to reconfigure each session
2. **Consider adding text-to-speech integration** using the Web Speech API
3. **Add a "reading ruler"** feature (a highlighted line that follows along) to help with visual tracking
4. **Implement bookmark functionality** using the Card component for each saved position
5. **Consider adding a distraction-free mode** that hides all UI except the text

The NeuroUI components automatically handle ARIA compliance, keyboard navigation, and responsive spacing, so you can focus on the reading experience itself!

---

## Example 4: Neurodivergent Navigation

**Prompt:** "Recommend a navigation component that works well for neurodivergent users in general"

**Tool calls:**
```
[Tool Call] search_components({"query": "navigation"})
  [Tool Call] get_guidelines({"condition": "ADHD"})
  [Tool Call] get_guidelines({"condition": "autism"})
  [Tool Call] get_guidelines({"condition": "dyslexia"})
  [Tool Call] generate_component_code({"component_id": "navigation"})
```

**Agent response:**

## Recommendation: **Navigation Component**

This is the best choice for general neurodivergent accessibility because it addresses core cognitive needs across multiple conditions:

### Why This Component Works

**For Users with ADHD:**
- **Predictable layout with adaptive spacing** reduces visual clutter, which minimizes demands on working memory and executive function. The prefrontal cortex in ADHD shows reduced activity for task management, so the UI must provide clear structural scaffolding
- **Clear active state styling** provides immediate visual feedback about location, supporting orientation without requiring users to hold multiple mental states

**For Autistic Users:**
- **Consistent, predictable layout** supports pattern recognition and reduces cognitive load from unpredictable changes. Since autism involves differences in predictive processing, maintaining stable navigation patterns helps the brain form reliable mental models
- **Explicit state indicators** (clear active states) provide unambiguous feedback without relying on subtle implicit cues that may be harder to process

**For Users with Dyslexia:**
- **Icon support** (via the `icon` prop) provides multimodal information channels, reducing reliance on text-only navigation. This compensates for the increased cognitive resources dyslexia demands for reading
- **Adaptive spacing** improves readability by preventing visual crowding of navigation labels

**For Motor Impairments:**
- **Full keyboard navigation** eliminates the need for precise mouse movements, which can be fatiguing or difficult
- **Generous spacing** creates larger click/tap targets, reducing motor precision requirements

### Implementation Code

```jsx
import { Navigation } from '@neuroui/components';

<Navigation label="Main menu" orientation="horizontal">
  <NavigationItem href="/" active>Home</NavigationItem>
  <NavigationItem href="/about">About</NavigationItem>
</Navigation>
```

### Key Features
- **Semantic HTML** with proper ARIA roles for screen reader users
- **Keyboard accessible** with intuitive focus management
- **Adaptive spacing** that respects user cognitive load preferences
- **Clear visual hierarchy** with distinct active states
- **Flexible orientation** (horizontal/vertical) to fit different layouts

This component embodies the principle of **cognitive scaffolding** — providing external structure that compensates for various cognitive differences while remaining intuitive for all users.

