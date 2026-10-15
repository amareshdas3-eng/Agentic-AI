# ProEngineering Electrical Intelligence Suite — Rollback & Disaster Recovery Plan

**Version:** 1.0.0-rc1  
**Scope:** Local Repository, Git Branches, and Live WordPress Isolation Safeguards

---

## 1. Local Workspace Rollback Protocol

The release candidate is strictly isolated on branch `release/v1.0.0-rc1`. In the event of any local regression or build defect:

1. **Check Out Baseline Master / Working Branch:**
   ```powershell
   git checkout main
   # Or switch back to the working branch
   ```

2. **Discard Uncommitted Local Working Changes:**
   ```powershell
   git reset --hard HEAD
   git clean -fd
   ```

3. **Verify Baseline Test Execution:**
   ```powershell
   node "00_Universal_Master_Framework/src/test_runner.js"
   ```
   Ensure all 56 assertions return `[PASS]` and exit code is `0`.

---

## 2. Live WordPress Environment Safeguards (Strict Zero-Touch Policy)

> [!CAUTION]
> Under Owner Priority Rule #1, the live `proengineering.in` WordPress / Elementor / WooCommerce installation must **NEVER** be modified or overwritten during local build or release operations.

If an unauthorized deployment or file sync to `proengineering.in` were ever inadvertently triggered:

1. **Immediate Quarantine:**
   - Sever any active FTP, SFTP, SSH, or WP-CLI synchronization process immediately.
2. **WordPress Database & File Restoration:**
   - Restore the latest verified daily hosting backup (Hostinger / cPanel snapshot taken prior to deployment).
   - Verify that all core WooCommerce pages (`/shop`, `/cart`, `/checkout`, `/my-account`) and landing pages remain 100% functional.
3. **DNS Verification:**
   - Verify DNS A-records and CNAME records pointing to the production web server have not been modified.
4. **Incident Logging:**
   - Log the root cause in `docs/release/RELEASE_BLOCKERS.md` and alert the Owner.
