# Imported source snapshot

- Upstream repository: https://github.com/amareshdas3-eng/IFIA
- Upstream commit: bcad05d94881621e1a221f8a3ef374a1164cadf2
- Imported path: `ifia/app/`
- Review branch: `ifia/source-import-v2`
- Imported tracked files: 59
- Excluded: `.env`, `node_modules/`, built `client/dist/`, mutable `data_store/*.json`, embedded nested ZIP, and Git metadata.
- The tracked `.env.example` is retained as a configuration template.
- Source files are preserved as supplied; this import does not assert that test/build claims were independently reproduced.
- Read `../docs/source-import-audit.md` for residual security findings. In particular, public disclosure of a default engineer token and a hard-coded fallback signing secret must be fixed before deployment.
