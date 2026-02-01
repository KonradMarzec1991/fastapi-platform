from pathlib import Path


IGNORE_DIRS = {"venv", ".venv", "__pycache__", ".git", ".idea", ".pytest_cache", ".serverless"}

def build_tree(path: Path, prefix=""):
    lines = [prefix + path.name]

    if path.is_dir():
        children = sorted(
            [p for p in path.iterdir() if p.name not in IGNORE_DIRS],
            key=lambda p: (p.is_file(), p.name.lower())
        )

        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            branch = "└── " if is_last else "├── "
            extension = "    " if is_last else "│   "

            if child.is_dir():
                lines.append(prefix + branch + child.name)
                lines.extend(build_tree(child, prefix + extension)[1:])
            else:
                lines.append(prefix + branch + child.name)

    return lines
