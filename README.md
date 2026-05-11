# 青年心力补给站

一个面向年轻人的积极心理互动网站。用户可以输入自己的压力、迷茫或内耗状态，网站会返回中国古代先贤名句、现代解释和一个当天可执行的小行动。

## 技术栈

- 后端：Python + Flask
- 前端：HTML + CSS + JavaScript
- 部署：Render Web Service

## 本地运行

```bash
pip install -r requirements.txt
python app.py
```

打开 `http://127.0.0.1:5000`。

## Render 部署

仓库已包含 `render.yaml`。在 Render 新建 Web Service，连接 GitHub 仓库后，Render 会自动识别配置。
