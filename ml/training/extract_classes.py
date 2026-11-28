"""kfood.zip(AI Hub 한국 이미지(음식))에서 foods-v1.json의 클래스만 추출한다.

사용법:
    python ml/training/extract_classes.py <kfood.zip 경로> [--out ml/data/raw]

결과: <out>/<food_id>/<원본파일명>
kfood.zip은 대분류별 zip(구이.zip, 밥.zip ...)을 담은 중첩 zip이며, 안쪽 파일명은 cp949다.
"""
import argparse
import json
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}


def decode_name(info: zipfile.ZipInfo) -> str:
    name = info.filename
    if not info.flag_bits & 0x800:  # UTF-8 플래그가 없으면 cp949로 해석
        try:
            name = name.encode("cp437").decode("cp949")
        except UnicodeError:
            pass
    return name


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("kfood_zip", type=Path)
    ap.add_argument("--out", type=Path, default=ROOT / "ml" / "data" / "raw")
    ap.add_argument("--foods", type=Path, default=ROOT / "data" / "foods-v1.json")
    args = ap.parse_args()

    foods = json.loads(args.foods.read_text(encoding="utf-8"))["foods"]
    # "밥/비빔밥" -> 대분류 "밥", 클래스 "비빔밥"
    wanted = defaultdict(dict)
    for f in foods:
        group, cls = f["aihub_class"].split("/")
        wanted[group][cls] = f["food_id"]

    counts = Counter()
    with zipfile.ZipFile(args.kfood_zip) as outer:
        for info in outer.infolist():
            group = Path(decode_name(info)).stem
            if group not in wanted:
                continue
            print(f"[{group}] 처리 중...", flush=True)
            with zipfile.ZipFile(outer.open(info)) as inner:
                for item in inner.infolist():
                    if item.is_dir():
                        continue
                    parts = decode_name(item).strip("/").split("/")
                    if len(parts) < 3 or parts[1] not in wanted[group]:
                        continue
                    filename = Path(parts[-1]).name  # 경로 조작 방지
                    if Path(filename).suffix.lower() not in IMAGE_EXT:
                        continue
                    food_id = wanted[group][parts[1]]
                    dest = args.out / food_id / filename
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    with inner.open(item) as src, open(dest, "wb") as dst:
                        dst.write(src.read())
                    counts[food_id] += 1

    for f in foods:
        print(f"{counts[f['food_id']]:5d}  {f['food_id']}")
    missing = [f["food_id"] for f in foods if counts[f["food_id"]] == 0]
    if missing:
        raise SystemExit(f"이미지를 찾지 못한 클래스: {missing}")


if __name__ == "__main__":
    main()
