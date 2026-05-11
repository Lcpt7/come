# 精神内耗鼓励网站

这是一个简单的中文正能量网站，帮助在内卷和精神内耗中迷茫的年轻人找到鼓励和积极向上的动力。

## 项目结构

- `app.py` - Flask 后端，提供鼓励语句接口
- `templates/index.html` - 网站前端页面
- `static/style.css` - 页面样式
- `static/script.js` - 前端交互逻辑
- `requirements.txt` - Python 依赖
- `render.yaml` - Render 部署配置（可选）

## 本地运行

1. 安装依赖：

```bash
pip install -r requirements.txt
```

2. 启动服务：

```bash
python app.py
```

3. 打开浏览器访问 `http://127.0.0.1:5000`

## 在 Render 上部署

1. 将此项目上传到 GitHub 仓库。
2. 登录 https://render.com ，创建一个新的 `Web Service`。
3. 选择你的 GitHub 仓库。
4. 设置环境：
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. 保存并部署。

如果使用 `render.yaml`，Render 会自动读取配置，默认服务名称和启动命令已经在文件中定义。

## 说明

前端已实现互动输入功能，用户可以输入当前心情或烦恼，后端会返回一句古代名言和一句鼓励建议。该网站鼓励积极奋斗，减少精神内耗。