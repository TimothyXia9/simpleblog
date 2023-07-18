# Django Playground

## 这是什么

随意使用django创建的项目, 瞎玩

## 环境

    python=3.8.17
    django=4.2.3
    vue3

安装依赖

    pip install -r requirements.txt 

## 进度

- [x] 项目创建
- [X] 配置环境
- [ ] 研究vue
- [ ] django
  
## note

### 1. staitc file处理

   在settings.py中配置

    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "staticfiles"),]

### 2. Vue 配置

直接查看网页

    npm run serve

打包给django

    npm run build

将打包后的dist文件放入static文件夹中
