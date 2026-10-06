| [home page](https://cmustudent.github.io/tswd-portfolio-templates/) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# Wireframes / storyboards

**Topic change:** My Part I proposal was a personal Spotify listening story. For Part II I switched to the colors of noise (white, pink, brown) and focus.

**One-sentence summary:** [Draft to edit: Brown noise is everywhere as a focus aid, but the best review of the research found a small benefit only for people with ADHD symptoms, a slight cost for everyone else, and no studies of brown noise at all.]

**Storyboard** (draft Shorthand story: [link])

| # | Section | What the reader sees | Visual or sound |
|---|---|---|---|
| 1 | Hook | The question: does "brown noise for focus" actually work? | Headline, full-width image |
| 2 | Meet the colors | What white, pink and brown noise are | Three short clips I generate, plus a sketch of their spectra |
| 3 | What the research found | A small average benefit in ADHD or high-symptom groups | Dot plot with confidence interval |
| 4 | The catch | A slight cost in non-ADHD groups | Two-group comparison chart |
| 5 | The gap | 12 white, 1 pink, 0 brown noise studies | Bar chart with an empty brown bar, and a silent clip |
| 6 | Who was studied | Mostly children, brief lab tasks, only two adult samples | Simple icon or bar chart |
| 7 | Takeaway | Treat it as a personal experiment, and keep the volume low | Text only |

**Sketches:**
<img width="657" height="413" alt="Screenshot 2026-10-06 at 1 53 03 PM" src="https://github.com/user-attachments/assets/7054cca5-5985-4e9d-98ad-91e0106c5ee9" />

**Draft visualizations:** [embed your Datawrapper or Tableau charts here]

# User research 

## Target audience

I'm hoping to reach people aged 20-35 who have experienced significant life transitions (moving to a new country, changing careers, relocating for school or work) and who use music as a way to process emotions. My secondary audience is people interested in personal data stories and how immigration/cultural shift impacts lifestyle choices.

**Approach to identifying representatives:** I interviewed four people from my immediate network who fit this profile. They don't need to be Spotify users or music experts—just people who listen to music regularly and have lived through a major life change.

## Interview script

**Research Goal:** Understand whether my story about shifting music taste after moving from India to the US resonates emotionally, and whether my visualizations effectively communicate that transition. I also want to identify which elements of the story feel most authentic and which need clarification.

| Goal | Questions to Ask |
|------|------------------|
| Understand if the story is clear | What do you think this story is about? |
| Assess emotional resonance | Does this feel like a personal, authentic story to you? Did any part feel relatable to your own experience? |
| Identify strongest visualization | Which visualization was easiest to understand? Which one made the story clearest? |
| Find confusing elements | Was anything confusing or unclear? What would help you understand it better? |
| Get improvement ideas | What would make you want to read more? What's missing? |
| Understand data-emotion connection | Do you believe that the data actually shows what I'm saying it shows? |

## Interview findings

| Questions | Interview 1 (CMU classmate, moved from Vietnam) | Interview 2 (Zscaler colleague) | Interview 3 (Friend from India) | Interview 4 (Non-tech friend, moved for career) |
|-----------|------------|------------|------------|------------|
| What do you think this story is about? | "It's about how your music taste changed when you moved countries. Like, it's a personal story told through data." | "Your journey adapting to a new place, and how you found a way to feel energized instead of homesick." | "Moving away from home and finding new music instead of the old stuff. It's about growing up." | "Someone using music to escape or cope with being away from where they're from." |
| Does this feel authentic and relatable? | "100%. I listened to a lot of sad indie music when I first got here. This totally makes sense." | "Yes, but I related more to the stress management angle than the homesickness part. Different story for me." | "Very relatable. The shift from calm music to upbeat stuff—I did the exact same thing." | "Relatable but I wish you talked more about missing people vs. missing place. That's what I felt." |
| Which visualization was clearest? | "The timeline showing genre shift month by month. I could actually see when you switched." | "The bar chart comparing before/after genre distribution was super clear." | "The energy level chart across time was cool, showed the progression well." | "Honestly the simple line chart of energy levels over time was easiest to read." |
| What was confusing or unclear? | "I didn't understand what the 'clusters' in the scatter plot meant at first. Need a label." | "The genre categories felt too broad. Like, EDM covers so much—could you break that down more?" | "The narrative jumps around a bit. I wasn't sure exactly when the 'move' happened in the timeline." | "You mention homesickness a lot in text but I don't see 'lonely music' vs 'happy music' clearly in the data." |
| What would make you want to read more? | "Show me specific songs or playlists that changed. Like actual names of things you listened to." | "A comparison to other people's data—are you unique or is this common? That would be interesting." | "More about why EDM specifically? Like, what does that genre do for you emotionally?" | "Show the people side of it. Did you make new friends? Reconnect with old ones? How does music connect to that?" |
| Does the data match your understanding? | "Yeah, I believe it. The data looks honest, not cherry-picked." | "Mostly yes, but I'd want to see the raw data—like, how many hours per month?" | "Completely believable. I know you listened to this stuff." | "Yes, but it would hit harder if you showed it alongside timeline events (like when you moved, semester started, etc.)" |

## Key findings and patterns

**Consistent feedback across all interviews:**
- The core story (music shift = emotional coping) resonates strongly
- Timeline visualization and energy-level charts are the clearest elements
- All interviewees felt the story was authentic and personal

**Conflicting feedback:**
- Interview 2 wanted more genre specificity; Interview 1 felt the broad categories were fine
- Interview 4 wanted more narrative context (dates, life events); Interviews 1-3 felt the data was sufficient

**Critical gaps identified:**
- All four mentioned wanting either: (1) specific song/artist examples, (2) comparison to other people's data, or (3) more narrative detail about the "why"
- Scatter plot needs clearer labeling
- Genre breakdown (especially EDM) needs more detail

**Highest-value feedback:**
- Interview 4's suggestion to overlay life events (move date, semester start) on the timeline would make the data-emotion connection much clearer
- Interviews 1 and 3 want to see specific artists/songs, not just genres

# Identified changes for Part III

| Research synthesis | Anticipated changes for Part III |
|-------------------|----------------------------------|
| Timeline and energy-level visualizations are clear and effective | Keep these as centerpiece; add life event markers (move date, semester starts) as annotations |
| Users want to see specific artists/songs, not just broad genres | Add a secondary visualization showing top 10 artists before/after move |
| Genre categories feel too broad (especially EDM) | Break down EDM into subcategories (progressive house, techno, future bass) to show specificity |
| Scatter plot is confusing without clear labels | Redesign or remove scatter plot; replace with simpler genre breakdown chart |
| Story needs more narrative detail connecting data to emotional journey | Add explicit timeline callouts (e.g., "3 months after arriving in SF, energy level rises") |
| Users want context on "why EDM specifically" | Add 1-2 sentence explanation: EDM's high energy helped me stay motivated when I felt isolated |

# Moodboards / personas

*Not applicable for this project—data storytelling approach prioritizes authenticity over mood/persona*

# References

- Spotify Extended Streaming History data export (personal data)
- Good Charts by Scott Berinato—Chapter 7: Persuasion or manipulation
- Interview feedback collected September 25-27, 2026

# AI acknowledgements

Claude assisted with structuring the user research protocol, and organizing findings templates. The core story concept, interview execution, and data interpretation are my own. Interview data reflects actual feedback from four interviewees (anonymized per assignment guidelines).
