# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Maria Sophia B. Olayta
**Section:** 9 - Silicon
**Last Name:** Olayta
**Date:** 17/08/2026
---

## Step 1: Identify the Big Problem
### Main Problem
Inefficient manual ordering, checkout, and inventory operations at the canteen.
---
## Step 2: Identify the Sub-Problems
1. Slow customer decision making.
2. Manual and slow checkout process.
3. Lack of inventory tracking.
4. Data disjointness.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Slow customer decision making. | Abstraction | Create a simplified user interface that filters items by categories, highlights daily bestsellers and hides non-essential product details to reduce choice paralysis. |
| Manual and slow checkout process. | Algorithmic Thinking | Design a step-by-step automated workflow using barcode scanning and integrated digital payment gateways to eliminate manual data entry. |
| Lack of inventory tracking. | Pattern Recognition | Implement an automated data logging loop that cross-references sale spiles and historical buying trends to predict stock storages in real-time. |
| Data disjointedness. | Decomposition | Break the fragmented system down to isolated data streams and unify them using a centralized database. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Write the sub-problem you selected.
### Pseudocode
START

  // 1. Unified Setup
  CONNECT to CentralDatabase

  // 2. Automated Checkout (Barcode & Payment Workflow)
  PRINT "Scan item barcode:"
  READ Barcode
  
  FIND Item IN CentralDatabase USING Barcode
  IF Item EXISTS AND Item.Stock > 0 THEN
    PROCESS DigitalPayment(Item.Price)
    UPDATE CentralDatabase: Reduce Item.Stock by 1
    LOG Sale(Item.ID, CurrentTime)
    PRINT "Receipt printed. Success!"
  ELSE
    PRINT "Item unavailable."
  END IF

  // 3. Simple Pattern Recognition (Stock Prediction)
  READ TotalSalesLastWeek FROM CentralDatabase
  
  IF Item.Stock < TotalSalesLastWeek THEN
    PRINT "ALERT: Reorder stock immediately!"
  END IF

END
Write your algorithm here.
END
---
