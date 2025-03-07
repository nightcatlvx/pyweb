# 修改为使用项目根目录绝对路径
$env:PYTHONPATH = "G:/pyweb/src"
uvicorn apps.api.main:app --host 0.0.0.0 --port 8081 --no-use-colors