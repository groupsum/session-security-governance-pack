"""Inspect the installed pack identity."""

from session_security_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:session-security"
print(metadata["origin"]["id"])
