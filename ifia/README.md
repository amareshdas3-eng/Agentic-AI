# Industrial Failure Intelligence Agent (IFIA)

**Status: Antigravity source ZIP received and inspected; documentation imported; full application source transfer into GitHub is pending.**

IFIA is described in the available Antigravity implementation report as an LLM-assisted industrial electrical failure root-cause analysis (RCA) workflow. Its stated design principle is:

> The LLM proposes; evidence constrains; engineering standards guide; statistics qualify; policy governs; an authorized human engineer approves.

This directory preserves the reported implementation scope and verification claims without representing missing source files as present. The initial repository inspection found only the existing root `README.md`. The user has since provided `RCA AGENT.zip`; its source tree has now been inspected, and an initial security review is recorded in [source-import-audit.md](docs/source-import-audit.md). The application source files themselves have not yet been transferred into this repository.

## Contents

- [Implementation report](docs/implementation-report.md) — structured summary of the supplied report.
- [Architecture inventory](docs/architecture-inventory.md) — reported components and paths, not source-code verification.
- [Verification status](docs/verification-status.md) — reported tests and sandbox results, clearly marked as not independently rerun here.
- [Engineering safety notes](docs/engineering-safety.md) — limits on operational use and validation requirements.
- [Source import and security audit](docs/source-import-audit.md) — findings from archive inspection and attempted tests.

## Reported capabilities

The supplied report describes evidence-linked RCA hypotheses, Zod contracts, a Claude API client with prompt-injection defenses, an independent QA auditor, human engineering approval, CMMS sandbox work-order drafting, duplicate-dispatch prevention, synthetic electrical cases, benchmark/ROI views, and printable RCA reports.

## Source import checklist

- [x] Receive and inspect the Antigravity source ZIP and project inventory.
- [x] Review package manifest, test files, API routes, and key security controls.
- [x] Scan archive for obvious credential material; exclude `.env` from any source import.
- [ ] Transfer reviewed application source files into `ifia/app/` without `node_modules/`, built output, or mutable data-store records.
- [ ] Install dependencies cleanly for the target platform and rerun tests.
- [ ] Record exact runtime, test, and benchmark results in CI.
- [ ] Review all engineering actions and standards references with qualified site/OEM personnel before any real-world use.

This directory currently contains documentation only. The archive has been reviewed, but no executable IFIA application files have been added to GitHub yet. The source audit identifies issues that must be addressed before production use.


## Updated Antigravity source

The reviewed source snapshot is available under [`app/`](app/) on the `ifia/source-import-v2` review branch. It was copied from upstream `amareshdas3-eng/IFIA` commit `bcad05d94881621e1a221f8a3ef374a1164cadf2`. Review [the source audit](docs/source-import-audit.md) before deployment; authentication hardening and independent build/test verification remain open.
