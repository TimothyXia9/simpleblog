# Django Playground

## 这是什么

学 django, vue 创建的项目

暂时准备做一个简单的笔记、文件网站

## 环境

    python=3.8.17
    django=4.2.3
    vue3
    样式:element-plus
    富文本:ckeditor

## 进度

-   [x] 项目创建
-   [x] 配置环境
-   [ ] 研究 vue
-   [ ] django

## note

### 1. staitc file 处理

在 settings.py 中配置

    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "staticfiles"),]

### 2. Vue 配置

直接查看网页

    npm run dev

打包给 django

    npm run build

将打包后的 dist 文件放入 static 文件夹中
