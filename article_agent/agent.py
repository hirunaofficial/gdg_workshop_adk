from google.adk.agents import LlmAgent, SequentialAgent

GEMINI_MODEL = "gemini-1.5-flash-latest"

# --- Sub-Agent 1: Draft article ---
article_drafter = LlmAgent(
    name="ArticleDrafter",
    model=GEMINI_MODEL,
    instruction="""You are a technical writer. Write a clear, well-structured technical article for the following topic:
    
Topic: {message}

Include:
- Title
- Introduction
- At least two main sections with relevant code examples where appropriate
- Conclusion

Your audience is intermediate-level developers who want to learn new technologies.
Focus on clarity, practical examples, and educational value.

Output only the article text.
""",
    description="Writes the initial draft of the article.",
    output_key="draft_article"
)

# --- Sub-Agent 2: Review the article ---
article_reviewer = LlmAgent(
    name="ArticleReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a technical editor. Review the article below for clarity, structure, and accuracy.

Article:
{draft_article}

Return your review as a concise, bulleted list of improvements. Focus on:
- Technical accuracy
- Code example quality and correctness
- Flow and structure
- Clarity for intermediate developers

If the article is excellent, just write: "No major issues found."
""",
    description="Reviews the draft article.",
    output_key="review_notes"
)

# --- Sub-Agent 3: Finalize the article based on feedback ---
article_finalizer = LlmAgent(
    name="ArticleFinalizer",
    model=GEMINI_MODEL,
    instruction="""You are a professional tech editor. Improve the draft article using the review notes below.

Original Article:
{draft_article}

Review Notes:
{review_notes}

Apply the improvements suggested in the review notes to create a final polished version.
Maintain the original structure but enhance clarity, examples, and explanations.
Add proper markdown formatting including code blocks with language tags.

Return only the final improved version of the article with proper markdown formatting.
""",
    description="Improves and finalizes the article.",
    output_key="final_article"
)

# --- Sequential Agent Pipeline ---
root_agent = SequentialAgent(
    name="TechArticlePipelineAgent",
    description="A multi-stage agent to write, review, and finalize technical articles.",
    sub_agents=[article_drafter, article_reviewer, article_finalizer]
)