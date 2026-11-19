# Contributing

Thanks for helping. Discuss larger changes in an issue first.

## Sign off every commit (DCO)

This project uses the Developer Certificate of Origin 1.1 (https://developercertificate.org). Sign off each commit to certify you have the right to submit it:

```text
git commit -s
```

This adds a line like `Signed-off-by: Your Name <you@example.com>`. CI rejects pull requests with unsigned commits.

## Changing the shared standard

Never edit the copy inside a skill. Edit `shared/standard.md`, then run:

```text
python3 scripts/sync_standard.py
```

## Before you open a pull request

```text
python3 scripts/sync_standard.py --check
python3 scripts/check_skills.py
bash tests/test_sync.sh
claude plugin validate .
```

All four must pass. Changes to skill behaviour also need an updated eval in `evals/`.

## Reporting bugs

Open an issue with what you asked, what the skill did, and what you expected. Security problems go through `SECURITY.md` instead.

## Licences

By contributing you agree that code is licensed under Apache-2.0 and documentation under CC-BY-4.0.
