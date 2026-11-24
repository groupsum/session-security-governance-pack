# Session Security Governance pack guide

Governance for authenticated-session issuance, binding, rotation, expiration, reauthentication, step-up, logout, invalidation, fixation, CSRF, failure, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `session-security-governance-pack` is an installable SSOT governance pack for Session Security. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for session security, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`session-security-governance-pack`](https://pypi.org/project/session-security-governance-pack/)
- GitHub package repository: [`groupsum/session-security-governance-pack`](https://github.com/groupsum/session-security-governance-pack)
- Import package: `session_security_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:session-security`
- PyPI package: `session-security-governance-pack`
- Import package: `session_security_governance_pack`
- GitHub repository: [groupsum/session-security-governance-pack](https://github.com/groupsum/session-security-governance-pack)
- Reservation owner: `extension-pack:session-security-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Session Security

## Authority Sources

- [NIST SP 800-63B-4: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [RFC 6265: HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc6265)

## Included ADRs

- [`adr:authenticated-sessions-begin-after-authentication`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/adr/ADR-1000-authenticated-sessions-begin-after-authentication.yaml) - Authenticated Sessions Begin After Authentication
- [`adr:reauthentication-and-step-up-triggers-are-explicit`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/adr/ADR-1001-reauthentication-and-step-up-triggers-are-explicit.yaml) - Reauthentication And Step Up Triggers Are Explicit
- [`adr:logout-and-session-invalidation-are-security-events`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/adr/ADR-1002-logout-and-session-invalidation-are-security-events.yaml) - Logout And Session Invalidation Are Security Events

## Included SPECs

- [`spc:session-issuance-and-binding-contract`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/specs/SPEC-2000-session-issuance-and-binding-contract.yaml) - Session Issuance And Binding Contract
- [`spc:session-rotation-idle-and-absolute-timeout-contract`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/specs/SPEC-2001-session-rotation-idle-and-absolute-timeout-contract.yaml) - Session Rotation Idle And Absolute Timeout Contract
- [`spc:reauthentication-and-step-up-contract`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/specs/SPEC-2002-reauthentication-and-step-up-contract.yaml) - Reauthentication And Step Up Contract
- [`spc:logout-revocation-and-invalidation-contract`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/specs/SPEC-2003-logout-revocation-and-invalidation-contract.yaml) - Logout Revocation And Invalidation Contract
- [`spc:session-fixation-csrf-and-failure-contract`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/specs/SPEC-2004-session-fixation-csrf-and-failure-contract.yaml) - Session Fixation CSRF And Failure Contract
- [`spc:session-audit-evidence-contract`](https://github.com/groupsum/session-security-governance-pack/blob/master/src/session_security_governance_pack/templates/specs/SPEC-2005-session-audit-evidence-contract.yaml) - Session Audit Evidence Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect session_security_governance_pack
uvx --from ssot-registry ssot pack preflight . session_security_governance_pack --all
uvx --from ssot-registry ssot pack sync . session_security_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from session_security_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-session-issuance-and-binding-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/session-security-governance-pack](https://github.com/groupsum/session-security-governance-pack)
- PyPI package: [session-security-governance-pack](https://pypi.org/project/session-security-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the session security governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
