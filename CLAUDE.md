# Workspace

AI UGC video ads for Meta/TikTok. Stage-specific know-how lives in `.claude/skills/` (loaded on demand); keep this file to what applies to every task.

## Layout
- `brand/<brand>/` — source of truth per brand. Current brand: `annuity-heritage-group`.
  - `claims.md` compliance limits · `presenter.md` locked presenter + still rules · `best-scripts.txt` winners · `reviews.md` customer language · `batch-01.md` batch log (large, read only the section you need) · `hero-ad-*.md` hero ad specs/QC · `infinite-ugc-input.md` video-tool input
- `.claude/skills/` — pipeline skills (angle mining → scripts → scenes → results) and motion-design-editor.
- `claude-ai-uploads/` — original skill zips, archive only; never read.

## Working efficiently
- Read only the brand files the task needs; grep `batch-01.md` and `presenter.md` instead of reading them whole.
- Send bulk digging to a subagent and keep only its conclusion: competitor-ad sweeps, review scraping, long Higgsfield/Meta/Windsor listings, CSV exports.
- Ask MCP list/search tools for small pages and minimal output; don't pull full job, ad or transaction histories into the conversation.
- Results analysis: run `python3 .claude/skills/ugc-results-analysis/scripts/group_results.py <csv>` and read its summary, never the raw CSV.
- Paid generations (Higgsfield credits, ad launches): quote cost first, batch independent jobs, wait with `jobs_wait`, show results once.
- Record lessons and final choices in the brand files and commit them, so the next session starts from the file and not a long chat history.
