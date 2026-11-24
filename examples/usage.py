"""Find a specification and its downstream path in the installed manifest."""

from session_security_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:session-issuance-and-binding-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-session-issuance-and-binding-contract.yaml"
