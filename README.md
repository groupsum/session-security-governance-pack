# session-security-governance-pack

Governance for authenticated-session issuance, binding, rotation, expiration, reauthentication, step-up, logout, invalidation, fixation, CSRF, failure, and audit evidence.

## Package identity

- Pack ID: `pack:session-security`
- PyPI distribution: `session-security-governance-pack`
- Python import: `session_security_governance_pack`
- Reservation owner: `extension-pack:session-security-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add session-security-governance-pack
uv run ssot pack sync . session_security_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://pages.nist.gov/800-63-4/sp800-63b.html
- https://www.rfc-editor.org/rfc/rfc6265
