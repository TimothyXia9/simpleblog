# Django Playground

## 这是什么

随意使用django创建的项目, 瞎玩

## 环境

    python=3.8.17
    django=4.2.3

安装依赖

    pip install -r requirements.txt 

## 进度

- [x] 项目创建
- [X] 配置环境
- [ ] 更改base.html
  
## note

### 1. staitc file处理

   在settings.py中配置

    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "staticfiles"),]

### 2. bootstrap配置

下载bootstrap文件, 放在static文件夹下, 在base.html中引入

另需下载jquery.min.js
