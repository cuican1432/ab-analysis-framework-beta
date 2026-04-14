# Memory

## Stable Working Memory

- Prefer doc-first analysis.
- Use live Libra extraction only when it is truly needed.
- New experiments must be analyzed from their own source materials.
- Old experiment outputs are not valid evidence for new experiments.
- Global metrics are the main decision evidence.
- Drilldown and slice analysis are supporting evidence unless the task explicitly centers on drilldown.

## Artifact Convention

- This convention is the default when the environment supports local files.
- The goal is to prevent cross-run context contamination and enable audit.
- Store outputs under:

```text
experiment/<experiment_id>/version_<yyyymmdd>/
```

- Keep A / B / C outputs together under the same version directory.
- If the same experiment is rerun, create a new version directory instead of overwriting the old one.
- Always write a run signature file for each run:
  - `run_signature.json` (or `run_signature.md`) containing:
    - source URLs (PRD + Raw Data)
    - `source_hash` (hash of the normalized source URLs + extracted header/config snapshot)
    - extraction time
    - experiment_id and the extracted data date range
- If a new run has similar sources but a different `source_hash`, warn the user and confirm it is a new run rather than an update of a previous experiment.
