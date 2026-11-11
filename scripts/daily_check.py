
import subprocess
import sys
from datetime import date


def run_git(command):
    return subprocess.run(
        command,
        capture_output=True,
        text=True
    )


def main():
    today = date.today().isoformat()

    print("100 Days of Machine Learning")
    print("Date:", today)

    status = run_git(["git", "status", "--short"])

    if status.returncode != 0:
        print("Error: Not inside a Git repository.")
        sys.exit(1)

    if not status.stdout.strip():
        print("No changes detected.")
        print("Nothing to commit.")
        return

    print("\nActual changes detected:")
    print(status.stdout)

    print("\nReview your changes before committing.")
    print("Run git diff and git status to inspect them.")


if __name__ == "__main__":
    main()
