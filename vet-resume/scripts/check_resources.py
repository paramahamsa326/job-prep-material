from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/templates/Canonical_Overleaf_Resume_Template.tex",
    "references/formatting.md",
    "references/review-rubric.md",
    "references/java-engineering-patterns.md",
    "references/candidate/core-profile.md",
    "references/candidate/java-full-time.md",
    "references/candidate/java-contract.md",
    "references/candidate/servicenow.md",
    "references/candidate/quality-engineering.md",
    "scripts/inspect_docx.py",
)


def main() -> None:
    missing = [path for path in REQUIRED if not (SKILL_ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing skill resources:\n- " + "\n- ".join(missing))
    print(f"OK: {len(REQUIRED)} required resources found in {SKILL_ROOT}")


if __name__ == "__main__":
    main()
