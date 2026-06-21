from pathlib import Path

RESOURCE_ROOT = Path("resources")
OUTPUT = Path("docs/课程索引.md")


def main() -> int:
    lines = ["# 课程索引", ""]

    for meta in sorted(RESOURCE_ROOT.rglob("course-meta.yml")):
        course_dir = meta.parent
        readme = course_dir / "README.md"
        rel = course_dir.as_posix()
        name = course_dir.name
        if readme.exists():
            lines.append(f"- [{name}](../{rel}/README.md)")
        else:
            lines.append(f"- {name}：`{rel}`")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"generated {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
