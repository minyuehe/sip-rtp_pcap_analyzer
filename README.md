# Flask-vue-pcap-analysis
A single page application with Flask and Vue.

### 前言
这是一个前端用 Vue，后端用 Python 的 Web 框架 Flask 开发的sip/rtp协议数据包（pcap）解析工具。这个小项目作为自己毕业设计

课题来完成。感兴趣可以clone下来自己玩哈～

### 目录结构

先简单看一下项目的目录结构，backend 是 Flask 实现的服务端，frontend 是 Vue 实现的前端。

```
.
├── ./README.md
├── ./backend
│   ├── ./backend/app
│   └── ./backend/pcap-analysis.py
└── ./frontend
    ├── ./frontend/README.md
    ├── ./frontend/build
    ├── ./frontend/config
    ├── ./frontend/dist
    ├── ./frontend/index.html
    ├── ./frontend/node_modules
    ├── ./frontend/package-lock.json
    ├── ./frontend/package.json
    └── ./frontend/src
```
> Vue 是渐进式 JavaScript 框架。[Vue官网](https://cn.vuejs.org/)

> Flask 是一个使用 Python 编写的轻量级 Web 应用框架。[Flask 学习资源](https://dormousehole.readthedocs.io/en/latest/)

再来看一下目前代码的运行效果：

![image-20220418102030715](README/image-20220418102030715.png)

### 本地部署

#### 后台-开发环境

1. 进入backend

   ```
   cd backend
   ```

2. 准备环境

   ```
   pip install requirements.txt
   ```

3. 运行Flask app

   ```
   flask run
   ```

   - 默认打开本地5000端口
   - 也可以通过-h和-p自行设计ip和port

#### 前端-开发环境

1. 进入frontend

   ```
   cd frontend
   ```

2. 环境准备

   首选需要安装nodeJS

   ```
   npm install
   ```

3. 执行开发环境运行

   ```
   npm run dev
   ```

   - 默认会在8080端口打开对应上面展示效果图的Web应用
   - 也可以在config/index.js中修改对应HOST
