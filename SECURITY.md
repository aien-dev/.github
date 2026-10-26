# Security policy

This policy covers every aien-dev repository that has no `SECURITY.md` of its own. A repository's own policy takes precedence.

## Reporting a vulnerability

Report privately. Do not open a public issue, pull request or discussion about it.

- **GitHub:** open the repository's **Security** tab and choose **Report a vulnerability**. This creates a private advisory that only the maintainers can see.
- **Email:** aien@aienos.com

Please include the repository, the commit or version, the steps to reproduce, and what an attacker could do with it. If the report involves a secret, describe where it was exposed; do not send the secret itself.

## Status of the code

AienOS is in alpha testing. The alpha bundle (Core engine, Omega install wizard, CUDA++ user-space replacement) is distributed through GitHub Releases on [aienos-releases](https://github.com/aien-dev/aienos-releases); only the latest alpha release and `main` are supported. The other AIEN repositories are research-grade, pre-alpha software with no public release; reports for them are handled against `main`.

## Where a report belongs

- A flaw in INTERPLANE, the interoperability protocol, belongs to [interplane](https://github.com/aien-dev/interplane/blob/main/SECURITY.md).
- If you are unsure which repository is affected, report it on the one you found it in, or by email.
