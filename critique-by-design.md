# Critique & Redesign: Global EV Market Share

## Step one: the visualization

Original source: [Counterpoint Research, "Global Passenger Electric Vehicle Market Share: By Quarter"](https://www.counterpointresearch.com/wp-content/uploads/2023/03/Global-Passenger-Electric-Vehicle-Market-Share.pdf) (MakeoverMonday 2023, Week 7)

I picked this one because the "visualization" isn't actually a chart at all. It's a plain percentage table showing four EV manufacturers (BYD, Tesla, Volkswagen, and an "Others" catch-all) by quarter from Q2 2021 to Q1 2023. I wanted a redesign target where the core problem wasn't bad chart choices but the complete absence of visual encoding. The underlying story, a Chinese automaker overtaking Tesla in under two years, is genuinely interesting, but the table hides it behind eight columns of numbers you have to compare by eye.

## Step two: the critique

Completed the Google Form using Stephen Few's Data Visualization Effectiveness Profile. Summary of scores and reasoning:

- **Usefulness (4):** Technically contains what an analyst would want to know, but only after doing the comparison work themselves.
- **Completeness (7):** All the necessary fields are there with no clutter, but "Others" swallows 56 to 64 percent of the market into one unlabeled bucket, which is the largest and least informative category in the table.
- **Perceptibility (2):** The weakest score. No pre-attentive cue for trend. The BYD/Tesla crossover is real but invisible until you trace numbers across all eight quarters.
- **Truthfulness (7):** Numbers appear accurate, but the undifferentiated "Others" bucket risks flattening a story that's really about several distinct rising competitors, not just three named brands.
- **Intuitiveness (5):** Easy to read (it's just a table), but does none of the interpretive work.
- **Aesthetics (2):** Unstyled table sitting in a PDF report footer.
- **Engagement (2):** Nothing invites a closer look, despite a genuinely compelling underlying story.

Biggest takeaway: the data's real narrative is a fast reordering of market leaders, but the presentation is completely static. The "Others" bucket is the single biggest weakness since it hides where the actual movement is happening.

## Step three: Sketch a solution

For my redesign, I focused on fixing the biggest issue from my critique: no visual encoding of the trend or the BYD/Tesla crossover. I sketched a multi-line chart tracking BYD, Tesla, and Volkswagen by quarter, with "Others" pushed back as a muted dashed reference line rather than removed entirely, so the total market composition is still visible without letting it dominate.

<img width="801" height="363" alt="EV market share redesign sketch" src="https://github.com/user-attachments/assets/5e43bcc9-0fc0-4afb-af79-dc2e769b23c0" />

One data decision worth noting: I considered adding Geely as a fourth named brand, since Counterpoint's later reports break it out separately. But Geely only appears as its own line starting in Q3 2023, after this dataset's range (Q2 2021 to Q1 2023) ends. Rather than estimate values for quarters where no sourced number exists, I kept the sketch to the three brands the original dataset actually supports.

## Step four: Test the solution

_(in progress)_

## Step five: build the solution

_(in progress)_

## References

Few, Stephen. "Data Visualization Effectiveness Profile," 2017. http://www.perceptualedge.com/articles/visual_business_intelligence/data_visualization_effectiveness_profile.pdf

Counterpoint Research. "Global Passenger Electric Vehicle Market Share: By Quarter." March 2023. https://www.counterpointresearch.com/wp-content/uploads/2023/03/Global-Passenger-Electric-Vehicle-Market-Share.pdf

## AI acknowledgements

_(fill in once the full assignment is done, so it covers everything in one place)_<img width="801" height="363" alt="Screenshot 2026-09-17 at 3 51 37 PM" src="https://github.com/user-attachments/assets/5e43bcc9-0fc0-4afb-af79-dc2e769b23c0" />
