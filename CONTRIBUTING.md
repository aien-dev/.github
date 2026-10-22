# Contributing to AIEN

I am Drake Stapleton. I direct this project and use AI agents as implementation, testing and review tools. Contributions should make a bounded improvement that another person can inspect and reproduce.

## Find the right repository

- Begin at the [AienOS front door](https://github.com/aien-dev/aienix) and its [teaching tracker](https://github.com/aien-dev/aienix/issues/9).
- File component issues in that component's repository. Search existing issues and pull requests before opening another.
- Read that repository's `AGENTS.md`, contribution instructions, contracts, decision records and exact-revision test entrypoint. Local instructions take precedence over this default guide.
- A repository with issues disabled is not an invitation to enable them. Use the linked current component or the front-door tracker for historical documentation tasks.

## Make a change someone can check

1. State the problem, current behavior and a finite acceptance condition. Link the actual source, issue and design record rather than inventing project history.
2. Work on a branch in an isolated checkout. Keep changes focused; do not alter gate thresholds, old receipts, generated evidence or unrelated runtime behavior to make a check pass.
3. Run the printed reproduction from a fresh checkout of the exact source and dependency revisions. Keep positive and refusal cases. Record environment, commands, observed output and exit status.
4. In the pull request, distinguish implementation, host tests, simulation, QEMU and physical-machine qualification. A successful build is not a chip measurement. Mark blocked and NOT_RUN steps explicitly.
5. Preserve failed results. Do not commit credentials, private conversations, model weights, sealed answers or personal datasets. Use synthetic fixtures for examples.
6. Link the evidence and explain limitations. AI assistance must be attributed accurately; an author or assistant rerunning a command is not automatically independent review.

## Verification and publication

The component's actual gate manifest and required checks define its integration requirements. The AIEN workflow uses exact-source evidence from the Spark judge and a hosted check that validates the published bundle, where that repository is enrolled. An external contributor does not need access to the development Spark to propose a change: document what was run locally and let the authorized verification/publication owner handle protected integration.

Do not report an issue complete because a branch exists, a pull request opened or a badge turned green. The issue's acceptance conditions and the final integrated inputs must be checked. Existing release tags are historical identifiers, not proof that the latest branch is qualified.

## Security and help

- Follow the [security policy](SECURITY.md) for vulnerability reports; do not post secrets or exploit details in an ordinary public issue.
- See [support routes](SUPPORT.md) for reproduction help.
- Licences are repository-specific. This contribution guide does not replace a component's licence or add a contributor agreement.
