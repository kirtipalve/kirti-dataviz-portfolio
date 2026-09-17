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

I showed the sketch to two classmates cold, without explaining it first, and asked the questions below.

Questions asked:

- Can you tell me what you think this is?
- Can you describe to me what this is telling you?
- Is there anything you find surprising or confusing?
- Who do you think is the intended audience for this?
- Is there anything you would change or do differently?

Results:

| Question | Interview 1 (classmate) | Interview 2 (classmate) |
|----------|-------------|-------------|
| What do you think this is? | How well automobile companies are doing / the rise of EV companies | The progression of companies over time |
| What is it telling you? | Confirmed time series was the right chart choice for this data | Whether buyers should opt for EV cars |
| Anything surprising or confusing? | Colors aren't tied to any inherent meaning; not enough explanation of what "market share" means or which market it covers | Meaning of the dotted line (Others) at the top was unclear |
| Who is the intended audience? | Investors | Car buyers |
| Anything you would change? | Not directly addressed | Add more charts |

Synthesis:

Both interviewees read the chart as being about EV manufacturer performance over time, which confirms the redesign succeeds at conveying the core trend that the original table hid. But a mismatch emerged from Interview 2 specifically: they named car buyers as the audience and read the data as answering whether buyers should opt for EVs. Market-share-by-manufacturer data does not actually contain any information relevant to a purchase decision (no price, reliability, range, or safety data), so a viewer walking away thinking it answers that question would be drawing a conclusion the chart cannot support. Interview 1's investor framing fits the underlying data much better.

Combined with the missing-definition and unclear-line-labeling feedback from Interview 1 and 2, the through-line is that the chart needs to more clearly signal its own scope, both to prevent readers from importing questions it doesn't answer, and to close the terminology gaps around what "market share" means and what the dotted line represents.

Based on this feedback, I plan to make the following changes in my final redesign:

1. Add a title or subtitle defining "market share" and its scope, framed toward an investor/analyst audience rather than leaving it open to a buyer-decision reading
2. Label or caption the "Others" line directly instead of leaving it as an unexplained dotted line
3. Consider whether the "add more charts" note points at something specific, like a companion chart showing total EV sales volume alongside share percentages, or whether one focused chart is the right scope for this story
4. Use brand-consistent colors for BYD, Tesla, and Volkswagen instead of arbitrary line colors

## Step five: build the solution

For my final redesign, I built an interactive line chart in Datawrapper tracking BYD, Tesla, and Volkswagen's global EV market share by quarter, with "Others" kept as a labeled reference line rather than removed, so the total market composition stays visible without dominating the story. The chart directly addresses the gaps found in Step Four: the title and subtitle now define what "market share" means and which market it covers (global passenger EV sales by unit volume), the "Others" line is labeled explicitly instead of left as an unexplained dotted line, and each brand's line uses its own brand-associated color instead of arbitrary defaults. I also added an annotation marking where BYD's line crosses above Tesla's, since that crossover was the core story hidden in the original table and neither interviewee would have been able to find it without deliberate effort in the original static version.

Compared to the original percentage table, this version does the perceptual work the source completely lacked: a viewer can see the trend and the crossover in seconds rather than tracing eight columns of numbers by hand. It's not a complete fix, the "add more charts" feedback from Interview 2 is one I chose not to act on, since I decided a single focused chart told this specific story more clearly than a multi-chart dashboard would have, but it resolves the specific comprehension gaps that came up in testing.


<iframe title="Global EV market share by manufacturer, Q2 2021–Q1 2023" aria-label="Line chart" id="datawrapper-chart-cUdtG" src="https://datawrapper.dwcdn.net/cUdtG/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="410" data-external="1"></iframe>
<script type="text/javascript">(function(){function e(){window.addEventListener('message',function(e){if(e.data['datawrapper-height']!==void 0){var t=document.querySelectorAll('iframe');for(var n in e.data['datawrapper-height'])for(var r=0,i;i=t[r];r++)if(i.contentWindow===e.source){var a=e.data['datawrapper-height'][n]+'px';i.style.height=a}}})}e()})();</script>


## References

Few, Stephen. "Data Visualization Effectiveness Profile," 2017. http://www.perceptualedge.com/articles/visual_business_intelligence/data_visualization_effectiveness_profile.pdf

Counterpoint Research. "Global Passenger Electric Vehicle Market Share: By Quarter." March 2023. https://www.counterpointresearch.com/wp-content/uploads/2023/03/Global-Passenger-Electric-Vehicle-Market-Share.pdf

## AI acknowledgements
I used AI this assignment for the following:

- Searching MakeoverMonday's archive to identify a suitable pre-April-2023 challenge, and researching the original source data behind the challenge (Counterpoint Research's EV market share reports)
- Explaining Stephen Few's Data Visualization Effectiveness Profile criteria before I completed the Google Form and to study and understand it better 
- Discussing my critique scores and reasoning as I worked through the form
- Brainstorming the sketch to be used 

All data, critique scores, sketch content, interview responses, and design decisions are my own. AI was used for research assistance, and help articulating my reasoning in writing, not for generating the underlying analysis or feedback itself.
