# Repository guidance

Before working, read these optional instruction files in order,
resolving these paths from this repository's root:

1. `.agents/organization/AGENTS.md`
2. `.agents/workspace/AGENTS.md`

Read each file if it resolves to a readable regular file.
Skip absent files; report broken or unreadable links.
Read each resolved file only once to avoid duplicate loading and cycles.

Resolve references inside imported files relative to their real target
directory after following symlinks.

Apply organization guidance, then workspace guidance, then the repository
instructions below. More specific applicable instructions take precedence.

Follow this repository's documentation and any more specific instructions for
the files being changed.

## Repository scope

- This collection provides modules, inventory plugins, filters, and `v1alpha1`
  roles used by Krestomatio's Ansible-based Kubernetes operators.
- Public module arguments, role variables, return values, and generated docs are
  downstream contracts. Keep compatibility with the operator CRDs and playbooks.
- `plugins/`, `roles/`, and `tests/` are source; generated documentation under
  `docs/` must stay aligned when an exposed interface changes.

## Validation

- Initialize the pinned `hack/mk` submodule before using Make targets.
- Run `make ansible-lint` and `make test-sanity`; run the relevant unit tests under
  `tests/unit/` for Python behavior and regenerate docs when public interfaces move.
