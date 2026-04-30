#!/usr/bin/env python3
"""古文字OCR推理 — PaddleOCR Baseline"""
import json, os
from pathlib import Path
from paddleocr import PaddleOCR

def main():
    data_dir = Path("/saisdata") if Path("/saisdata").exists() else Path(".")
    out_dir = Path("/saisresult") if Path("/saisresult").exists() else Path(".")
    out_dir.mkdir(parents=True, exist_ok=True)

    ocr = PaddleOCR(use_angle_cls=False, lang='ch', show_log=False, use_gpu=False)
    png_files = sorted(data_dir.glob("*.png")) or sorted(Path(".").glob("*.png"))
    print(f"找到 {len(png_files)} 个文件")

    submission = {}
    for img_path in png_files:
        fname = img_path.name
        print(f"  处理: {fname}")
        result = ocr.ocr(str(img_path), cls=False)
        chars = []
        if result and result[0]:
            for line in result[0]:
                bbox, (text, conf) = line
                xs, ys = [p[0] for p in bbox], [p[1] for p in bbox]
                chars.append({
                    "text": text,
                    "bbox": [int(min(xs)), int(min(ys)), int(max(xs)-min(xs)), int(max(ys)-min(ys))],
                    "confidence": round(float(conf), 4)
                })
        submission[fname] = chars

    out_path = out_dir / "prediction.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(submission, f, ensure_ascii=False, indent=2)
    print(f"完成: {out_path} | {sum(len(v) for v in submission.values())} 字符")

if __name__ == '__main__':
    main()