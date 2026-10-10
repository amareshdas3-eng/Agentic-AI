# Industrial Failure Intelligence Agent (IFIA)

**Status: documentation imported; application source code not yet imported.**

IFIA is described in the available Antigravity implementation report as an LLM-assisted industrial electrical failure root-cause analysis (RCA) workflow. Its stated design principle is:

> The LLM proposes; evidence constrains; engineering standards guide; statistics qualify; policy governs; an authorized human engineer approves.

This directory preserves the reported implementation scope and verification claims without representing missing source files as present. The repository inspection found only the existing root `README.md`; no IFIA application source files were present in this repository at the time of import.

## Contents

- [Implementation report](docs/implementation-report.md) — structured summary of the supplied report.
- [Architecture inventory](docs/architecture-inventory.md) — reported components and paths, not source-code verification.
- [Verification status](docs/verification-status.md) — reported tests and sandbox results, clearly marked as not independently rerun here.
- [Engineering safety notes](docs/engineering-safety.md) — limits on operational use and validation requirements.

## Reported capabilities

The supplied report describes evidence-linked RCA hypotheses, Zod contracts, a Claude API client with prompt-injection defenses, an independent QA auditor, human engineering approval, CMMS sandbox work-order drafting, duplicate-dispatch prevention, synthetic electrical cases, benchmark/ROI views, and printable RCA reports.

## Source import checklist

- [ ] Export the complete Antigravity project as a ZIP or provide its source repository.
- [ ] Review file tree, package manifests, build scripts, tests, and configuration.
- [ ] Scan for secrets and remove any real credentials before committing.
- [ ] Import the actual application source and assets; do not reconstruct missing files from this report.
- [ ] Install dependencies and run tests in a controlled environment.
- [ ] Record exact runtime, test, and benchmark results in CI.
- [ ] Review all engineering actions and standards references with qualified site/OEM personnel before any real-world use.

Until the source project is provided and validated, this directory is documentation-only. No executable IFIA application has been added by this commit.
