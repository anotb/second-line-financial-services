# Releasing

The runbook for changing and releasing this plugin. It applies to any person or agent.

## How the repo is set up

- One plugin, at `plugins/second-line-financial-services/`. Do not split it into several. The maintainer chose one install and one listing over 12, because the directory takes one submission per folder.
- The directory listing is at https://claude.ai/directory/manage/plugins/98fa919d-dd33-4941-9ae7-67f7417954ab. It reads only the plugin folder and tracks `main`.
- Installs receive only the plugin folder, so nothing in it may point outside it. Use full GitHub URLs for repo-level files such as `ROADMAP.md`.
- A GitHub push webhook tells the directory about each push within minutes. A scheduled check also runs about every 6 hours.

## Release steps

1. Branch from `main`. Don't commit to `main` directly, because every commit on `main` becomes a scanned version.
2. Make the change, following the rules below.
3. Raise `version` in `plugins/second-line-financial-services/.claude-plugin/plugin.json`. Users on a pinned version get nothing until it changes. Docs-only changes outside the plugin folder need no raise.
4. Add a `CHANGELOG.md` entry and update the release number in `STATUS.md`.
5. Run the checks. All must pass:

   ```bash
   python3 scripts/check.py
   python3 scripts/check-skill-content.py
   claude plugin validate plugins/second-line-financial-services --strict --profile directory
   claude plugin validate . --strict
   ```

6. Push the branch. If the change touches the plugin folder, run the portal's Validate against it: https://claude.ai/directory/manage/new/plugin, Repository `anotb/second-line-financial-services@<branch>`, Plugin path `plugins/second-line-financial-services`. Only validate. A second submission for this folder isn't possible, and drafts count toward the 10 per 24 hours limit, so don't continue through the form.
7. Open a PR and merge to `main`.
8. Open the listing page and confirm the new version on the Versions tab, then its scan result on the Review tab. A scan takes about 5 to 10 minutes.

Merging during a review starts a new scan and moves the status back to Scanning for a few minutes, so batch changes while a review is open.

## Rules that keep the scan clean

`scripts/check.py` enforces each of these, except the two marked.

| Rule | What the directory does otherwise |
|---|---|
| 512 files or fewer in the plugin. Add overlays and examples as sections in the skill's existing files. | Holds the version for a reviewer |
| No `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, or `termsOfServiceUrl` in `plugin.json`. The listing already has them. | Warns on every version |
| Never write "pass" followed by a word, such as "pass criterion" or "pass / fail". Write "success criterion" or "clear or fail". "pass-through" is fine. | Reads it as a password and holds the version |
| Write USD 50B, not a dollar sign and digit, in `SKILL.md` and `README.md`. | Reads it as a command built at run time |
| Keep each skill `description` to 120 characters or fewer (`scripts/check-skill-content.py`). | Nothing in the directory, but Claude Code's listing budget is 1% of context and drops descriptions that don't fit, so skills stop triggering |
| Text files plus the one icon PNG only. No scripts, hooks, or MCP servers unless the README and `PRIVACY.md` disclose them (not enforced). | Holds the version, and can fail the security scan |
| Keep the `## Human review and AI disclosure` section in every skill and in the README (not enforced). | Breaks the Usage Policy's high-risk requirements, which the directory requires |

## Listing details

The portal recorded the display name, description, icon, keywords, and links when the plugin was submitted, and its Listing tab says newer versions don't update them. The exceptions are the display name and short description, which follow the live version.

- `assets/icon.png` stays in the plugin. It may be needed if the listing is ever recreated.
- The privacy and terms links on the listing point at `PRIVACY.md` and `TERMS.md` on `main`, so don't move those files.
- If the plugin ever gets a new submission, add the five listing fields back to `plugin.json` first, along with `LISTING_ONLY_FIELDS` allowances in `scripts/check.py`, because those fields are read at first save. Remove them again afterwards.
- `name` is permanent. Don't rename the plugin.

## What needs a person

- Accepting legal acknowledgements on a submission.
- Webhook secrets. They are shown once and belong to the maintainer. Don't read or type one. To replace one, use **Rotate secret** on the listing's Settings tab, then update it in GitHub.
- Withdrawing, delisting, or publishing the plugin, or answering a reviewer.
- Signing in. Never sign out of or change the account in a browser session.

## Windows and Syncthing

The working copy syncs between machines through Syncthing, so coordinate concurrent edits.

- `core.autocrlf=true` checks files out as CRLF on Windows. Restore LF after a pull so the Mac copy stays clean.
- `scripts/check*.py` can show a 755 to 644 mode change on Windows. It's noise, so don't commit it. If it blocks `git switch`, use `git -c core.filemode=false switch <branch>`. After staging an edit to those scripts, run `git update-index --chmod=+x <file>`.

## Other known state

The old submission at the repo root (`c82eca96-286e-42a4-9195-252706c4793d`) was rejected and is not scanned or listed. It has no Withdraw control, only Contact Anthropic. Leave it alone.
