from pathlib import Path
import re
import sys

RESOURCE_ROOT = Path("resources")
ALLOWED_METADATA = {"README.md", "course-meta.yml", ".gitkeep"}
RESOURCE_PATTERN = re.compile(r"^(\d{4}|未知年份)-.+-.+-.+\.[^.]+$")


def main() -> int:
    if not RESOURCE_ROOT.exists():
        print("resources directory does not exist")
        return 1

    errors: list[str] = []
    for path in RESOURCE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if "教材" in path.parts:
            continue
        if "99-资源索引" in path.parts and path.suffix.lower() == ".md":
            continue
        if path.name in ALLOWED_METADATA:
            continue
        if path.suffix.lower() in {".yml", ".yaml"}:
            continue
        if not RESOURCE_PATTERN.match(path.name):
            errors.append(str(path))

    if errors:
        print("以下资料文件命名不符合规范：")
        for item in errors:
            print(f"- {item}")
        return 1

    print("文件命名检查通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
