# Security policy

This policy covers every aien-dev repository that has no `SECURITY.md` of its own. A repository's own policy takes precedence.

## Reporting a vulnerability

Report privately. Do not open a public issue, pull request or discussion about it.

1. GitHub: open the repository's Security tab and choose "Report a vulnerability". This
   creates a private advisory that only the maintainers can see. If that option is not shown,
   private vulnerability reporting has not been enabled for that repository yet; use email.
2. Email: drake@aienos.com or aien@aienos.com, with the subject `[<repository>] security report`.

Include the repository, the commit or version you tested, the component (path), the steps to
reproduce, and what an attacker could do with it. If the report involves a secret, describe where
it was exposed; do not send the secret itself. Encrypted mail is not required; do not post
proof-of-concept payloads publicly.

## Response targets

This project has one maintainer; the targets below are best effort and stated honestly.

- Acknowledgement: within 3 working days.
- Triage and severity: within 7 days of acknowledgement.
- Fix or mitigation for confirmed issues: aim for 30 days for high and critical, 90 days
  otherwise, with a status update at least every 14 days until closed.
- Disclosure: coordinated. An advisory is published with credit (unless you ask otherwise)
  once the fix is on the default branch. Default embargo 90 days, negotiable.

## Scope

- This repository itself holds the organization profile and default community files
  (`profile/`, `CONTRIBUTING.md`, this file, `AGENT_CODE_OF_CONDUCT.md`, the pull request and
  issue templates). A vulnerability here is a secret, private address or personal data committed to
  a public file, or a template change that would lead contributors in every repository to disclose
  something they should not.
- For any other aien-dev repository without its own policy, the scope is that repository's code
  and workflows.
- A flaw in INTERPLANE, the interoperability protocol, belongs to
  [interplane](https://github.com/aien-dev/interplane/blob/main/SECURITY.md).
- If you are unsure which repository is affected, report it on the one you found it in, or by
  email.

## Supported versions

AienOS is in alpha testing. The alpha bundle (Core engine, Omega install wizard, CUDA++ user-space
replacement) is distributed through GitHub Releases on
[aienos-releases](https://github.com/aien-dev/aienos-releases); only the latest alpha release and
`main` are supported. The other AIEN repositories are research-grade, pre-alpha software with no
public release; reports for them are handled against `main`. Reports against older commits are
welcome but fixes land on the default branch only.

## Status

No certification and no bug bounty. This repository has no code, no build and no CI
(AGENTS.md). See AUDIT_SCOPE.md for what an auditor can review here.
