---
type: skill
priority: high
confidence: not-started
tags: [skills, paper2, bar-gate, stock-control, operations]
---

# Paper 2 Bar-Gate Stock Graphs

> [!info] Why this gets its own note
> A bar-gate stock graph appeared in **5 of the last 6 live Paper 2 sittings** (SAMs, 2020 KFC, 2022, 2023 Ocado, 2024). It is virtually guaranteed in 2026. Misreading it is the single most-flagged Paper 2 mistake in examiner reports.

## What the graph looks like

```
Stock
level
  ^
  |    ___
  |   /   \         ___
  |  /     \       /   \         ___
  | /       \     /     \       /
  |/         \   /       \     /
  |           \_/         \___/
  |  ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄  ← buffer stock line
  |
  +───────────────────────────────────> Time (days)
       |          |          |
   delivery   delivery    delivery
```

It looks like a **saw-tooth** pattern: stock falls along a sloped line as it is used, then jumps vertically up when a delivery arrives.

## The five things you must be able to read

| Feature | What it means | How you read it |
|---|---|---|
| **Buffer stock** | Minimum safety level — stock should never drop below this | Horizontal floor line, often dashed |
| **Re-order level** | Stock value that triggers placing a new order | The value where the curve crosses the order trigger (often shown as a horizontal line) |
| **Lead time** | Time from placing the order to it arriving | Horizontal distance between re-order level crossing and the next vertical jump |
| **Maximum stock** | Stock immediately after a delivery | The peak (top) of the saw-tooth |
| **Order size (delivery quantity)** | How much was delivered | **Max stock − buffer stock** (NOT max stock alone) |

## The four most common questions

### 1. "Identify the buffer stock" (1 mark)
Read the horizontal floor line off the y-axis.

### 2. "Calculate the size of the order delivered" (2 marks)
**= max stock − buffer stock.** Spot the peak (after a delivery) and subtract the floor line. **This is the question most students get wrong** — they write the peak value alone.

*KFC example (Nov 2020):* if max stock = 2,400 portions and buffer = 600 portions, order size = **1,800 portions**.

### 3. "How many days did the business run out of stock?" (1–2 marks)
Look for any flat segment along the x-axis at zero stock. Count the days that segment spans (KFC Nov 2020: **4 days**).

### 4. "How many days between deliveries / until next delivery?" (1–2 marks)
Count the horizontal distance (days) between two consecutive vertical jumps OR between today and the next jump.

*June 2024 Q3b:* last delivery on day 10, runs out on day 28 → **18 days**.

## Linked concepts to know

### Just-in-Time (JIT) stock control
Eliminates buffer stock — stock arrives only when needed.
- **Pros**: no storage cost, no obsolete stock, frees up cash
- **Cons**: any supplier delay = production stops (KFC's DHL crisis closed 900 restaurants — they were running JIT)
- **Best for**: predictable, large-volume operations with reliable suppliers (Tesla)

### Holding buffer stock
Maintains a safety floor.
- **Pros**: protects against supplier delays / demand spikes; uninterrupted production
- **Cons**: storage cost, ties up cash, risk of obsolescence (especially perishable goods like KFC chicken)
- **Best for**: businesses with unreliable supply or volatile demand

## Pitfalls flagged by examiners

> [!warning] Top 3 mistakes from examiner reports
> 1. **Forgetting to subtract buffer stock** when asked for delivery size — writing "2,400" instead of "1,800"
> 2. **Misreading the y-axis scale** — bar-gates are often in 100s, 1000s or thousands of portions
> 3. **Confusing lead time with re-order frequency** — lead time = order to delivery; re-order frequency = how often you order

## Practice questions to attempt

- **SAMs Paper 2 Q5(a)**: identify amount of ash wood Fender held as buffer stock
- **Nov 2020 Paper 2 Q5(a)**: calculate size of Order A from chicken portions bar-gate (KFC)
- **Nov 2020 Paper 2 Q5(b)**: identify days KFC ran out of chicken (= 4)
- **June 2022 Paper 2 Q1(a)**: MCQ — read minimum stock level off bar-gate (= 600)
- **June 2023 Paper 2 Q3**: total stock delivered (sum of three deliveries) — Ocado
- **June 2024 Paper 2 Q3(b)**: days to run out after last delivery (= 18 days)

## Related topics (Obsidian wiki-links)
- [[Chart and Graph Skills]]
- [[Quantitative Skills]]
- [[2.3 Making operational decisions]]
- [[2.4 Making financial decisions]]
- [[Command Words]]
