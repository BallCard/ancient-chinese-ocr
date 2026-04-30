FROM python:3.10-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev \
    libgomp1 wget && \
    rm -rf /var/lib/apt/lists/*

# 安装Python依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制推理脚本
COPY infer.py .
COPY run.sh .
RUN chmod +x run.sh

# 运行时入口
CMD ["bash", "run.sh"]
