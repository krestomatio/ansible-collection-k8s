# Repository guidance

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
