# MedTrack DV — Live Demo Narration Script
**Target: 5 minutes.** This is for the Live Demo segment — open the actual .pbix file and
follow along. Unlike the PPT script, this one has specific clicks built in, since the whole
point of a live demo is proving the thing is interactive, not just showing static screenshots.

Rehearse this with the file actually open at least twice before presenting — clicking while
talking is harder than it sounds under time pressure.

---

## Opening (10s)
*[Screen: Hospital Overview page, all filters on "All"]*

> "So this is the live dashboard — everything you're about to see is real, filterable data,
> not screenshots. I'll walk through all four pages and show a couple of the interactions
> that make this actually useful for a hospital administrator, not just a static report."

---

## Page 1 — Hospital Overview (70s)

> "This is the landing page — Hospital Overview. Up top I've got six KPI cards: total
> admissions, occupancy rate, average length of stay, readmission rate, bed utilization,
> and discharge count. These aren't static numbers — watch what happens when I filter."

**[Action: Click the Hospital slicer → select "City Care Hospital"]**

> "The moment I select one hospital, every number on this page recalculates — total
> admissions drops, and you can see the occupancy rate change too. That's the whole point:
> an administrator isn't stuck reading a static report, they're asking their own questions
> in real time."

**[Action: Reset Hospital slicer back to "All"]**

> "Below the KPIs, these three trend lines show admissions, occupancy, and readmission rate
> by month — so you can spot seasonal patterns instead of just seeing one flat number for
> the year."

**[Action: Hover over a point on the Admissions Trend line]**

> "And every chart has tooltips — hovering gives the exact figure for that month, not just
> the visual trend."

---

## Page 2 — Patient Flow (45s)

**[Action: Click "Patient Flow" in the sidebar]**

> "Moving to Patient Flow — this page is about where patients are coming from and how they
> move through the system. The treemap here breaks admissions down by region."

**[Action: Click on the "Asia" block in the treemap]**

> "If I click into a region — say, Asia — watch the bar chart and donut next to it filter
> down to just that region's numbers. That's a cross-filter action: clicking one visual
> automatically filters the others on the same page."

**[Action: Click the same block again to deselect / reset]**

---

## Page 3 — Department Analytics (75s)
*This is your strongest page — spend the most time here.*

**[Action: Click "Department Analytics" in the sidebar]**

> "This page is where the interesting insight actually lives. On the left is a summary
> table — every department, its total admissions, readmission rate, and average length of
> stay, side by side."

**[Action: Point to the scatter chart, bottom right]**

> "But the real story is in this scatter chart — average length of stay on the X-axis,
> readmission rate on the Y-axis, and each dot is a department, sized by patient volume."

**[Action: Hover over the ICU dot, isolated top-right]**

> "And look at ICU — it's sitting completely on its own, away from every other department.
> Longest average stay, highest readmission rate. That's not something you'd catch scanning
> a table of numbers, but the moment you see it plotted like this, it's obvious this
> department needs attention that the others don't."

**[Action: Click the ICU dot to filter the page, if drillthrough/cross-filter is set up — otherwise skip]**

> "This is exactly the kind of insight a dashboard should surface automatically, instead of
> making someone dig for it."

---

## Page 4 — Resource Utilization (40s)

**[Action: Click "Resource Utilization" in the sidebar]**

> "Last page — Resource Utilization. This is built for capacity planning: bed utilization
> rate as a gauge, and a comparison of occupancy rate against total bed capacity across all
> five hospitals."

**[Action: Click the Hospital slicer → select a specific hospital]**

> "If a planner wants to check one hospital specifically — say, whether Green Valley has
> room to take more patients — one click filters everything on this page down to just that
> hospital's numbers."

**[Action: Reset filter back to "All"]**

---

## Closing (15s)

**[Action: Click back to Hospital Overview, reset all filters to "All"]**

> "So that's all four pages, working together as one connected dashboard — six KPIs on the
> landing page, patient flow by region, department-level efficiency comparisons, and
> resource planning, all filterable from the same four controls at the top of every page.
> Happy to take questions, or filter into anything specific you'd like to see."

---

## Timing checklist
| Section | Target time |
|---|---|
| Opening | 10s |
| Hospital Overview | 70s |
| Patient Flow | 45s |
| Department Analytics | 75s |
| Resource Utilization | 40s |
| Closing | 15s |
| **Total** | **~4:15** (leaves ~45s buffer for a panel question mid-demo, or slower clicking) |

## Rehearsal tips specific to a live demo
- **Practice the clicks, not just the words.** A live demo fails when the presenter fumbles
  finding the right filter — know exactly where every slicer is before you start talking.
- **Have a fallback.** If something breaks live (a visual doesn't load, a filter freezes),
  don't troubleshoot in front of the panel — say "let me flip back to this view" and
  continue, or reference the screenshot in your PPT instead.
- **Reset filters before you start.** Walking in with a stale filter applied from your last
  test run makes your opening numbers look wrong immediately.
- **The ICU scatter-chart moment (Department Analytics) is your best beat** — don't rush it,
  that's the one insight a panelist is likely to remember and ask about.
