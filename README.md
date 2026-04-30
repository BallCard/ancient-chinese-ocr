# 古文字OCR识别 - AI4S竞赛提交

## 项目说明
本项目用于AI4S古文字OCR识别竞赛，基于PaddleOCR实现古代文字的检测与识别。

## 文件结构
```
├── Dockerfile          # Docker镜像构建文件
├── run.sh              # 竞赛平台入口脚本
├── infer.py            # PaddleOCR推理脚本
├── requirements.txt    # Python依赖
└── prediction.json     # 示例输出格式
```

## 使用方法

### 本地测试
```bash
python infer.py
```

### Docker构建
```bash
docker build -t ancient-ocr:latest .
docker run -v /path/to/data:/saisdata -v /path/to/output:/saisresult ancient-ocr:latest
```

## 竞赛要求
- 输入路径: `/saisdata/*.png`
- 输出路径: `/saisresult/prediction.json`
- 入口脚本: `/app/run.sh`

## 技术栈
- PaddleOCR 2.7+
- PaddlePaddle 2.6.1
- Python 3.10
