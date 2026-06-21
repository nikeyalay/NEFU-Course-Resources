from pathlib import Path
import sys

RESOURCE_ROOT = Path("resources")
REQUIRED_COURSE_FILES = {"README.md", "course-meta.yml"}


def is_course_dir(path: Path) -> bool:
    return (path / "course-meta.yml").exists()


def main() -> int:
    if not RESOURCE_ROOT.exists():
        print("resources directory does not exist")
        return 1

    errors: list[str] = []
    for path in RESOURCE_ROOT.rglob("*"):
        if not path.is_dir() or not is_course_dir(path):
            continue
        missing = [name for name in REQUIRED_COURSE_FILES if not (path / name).exists()]
        if missing:
            errors.append(f"{path}: missing {', '.join(missing)}")

    if errors:
        print("以下课程目录缺少必要文件：")
        for item in errors:
            print(f"- {item}")
        return 1

    print("课程元数据检查通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
