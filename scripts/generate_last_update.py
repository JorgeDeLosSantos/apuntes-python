from datetime import datetime
from pathlib import Path
import subprocess


OUTPUT_FILE = Path("_generated/last_update.md")


def get_last_commit_date() -> datetime:
    """Return the date of the most recent Git commit."""
    value = subprocess.check_output(
        ["git", "log", "-1", "--format=%cI"],
        text=True,
    ).strip()
    return datetime.fromisoformat(value)


def main() -> None:
    date = get_last_commit_date()
    formatted_date = date.strftime("%d/%m/%Y")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        f"**Fecha de última actualización: {formatted_date}**\n",
        encoding="utf-8",
    )

    print(f"Generated {OUTPUT_FILE}: {formatted_date}")


if __name__ == "__main__":
    main()
