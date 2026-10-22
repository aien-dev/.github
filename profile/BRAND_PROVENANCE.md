# GitHub brand assets: actual renderer pixels

The organization avatar and AienOS front-door social preview are crops/resizes of [Allen's existing kernel-rendered banner](assets/allen-banner.jpg), not generated artwork or a stock illustration. The inherited profile records that banner as host-rendered kernel UI, not a new physical iMac observation.

Input provenance:

- Existing source asset at profile branch commit [`4e044f3526d28ac18a849ad2f694eda42f04de60`](https://github.com/aien-dev/.github/blob/4e044f3526d28ac18a849ad2f694eda42f04de60/profile/assets/allen-banner.jpg).
- Input SHA-256: `5ee0ac5854f9e32fd9a84406fd37b0a460a6eb87f096772f0f84064121a48fc6`.
- Original implementation family: [Aienux native/kernel/ui](https://github.com/aien-dev/aienux/tree/main/native/kernel/ui). This pass did not rerun the kernel renderer or qualify a hardware frame.

## Reproduce the derived images

Prerequisites: Python 3 and Pillow in an isolated environment. From this repository root:

```sh
python3 profile/tools/make_github_previews.py
```

[The script](tools/make_github_previews.py) preserves aspect ratio and letterboxes the original pixels onto a 1280×640 canvas for [the social preview](assets/aienos-social-preview.png). For [the avatar](assets/allen-avatar.png), it measures the brightest central rendered orb pixel, observed at `(802, 290)` in the original image, takes a 360×360 crop without the UI caption and resizes it to 1024×1024. No stars, galaxies, black holes or orb points are synthesized in this transformation. Both PNG files are below GitHub's 1 MB limit.

## Observed GitHub settings, 2026-10-22

- Organization avatar: uploaded through GitHub's native organization settings, confirmed through the crop dialog, then read back as the actual rendered orb in the saved settings page. GitHub warned that other cached avatar sizes can take minutes to update.
- Public repository pins: saved through GitHub's native chooser and independently read back through `organization.pinnedItems`: six public entries, `aienix`, `aienux`, `omega-mv`, `CUDApp`, `aien-sovereign-core-mv` and `aien-architecture-mv`.
- AienOS front-door repository social preview: uploaded through native repository settings. GraphQL readback returned `usesCustomOpenGraphImage: true` and [this stored image](https://repository-images.githubusercontent.com/1422324345/b2836202-4f5b-4875-89fd-bc246afbe10a). The settings page showed the rendered banner, not the previous default card.
- Seventeen public repositories' About descriptions, homepage URLs and actual topics were updated and read back. Private repository topics were not changed: GitHub documents that topic names themselves are public.

The profile README and community defaults on this branch still require authorized desk integration. Applied metadata, avatar/pins and a custom social image are separate facts from README publication. No Git tag or release was created, moved, deleted or promoted for appearance. No visibility, protection, disabled-issue setting or default branch was changed.
