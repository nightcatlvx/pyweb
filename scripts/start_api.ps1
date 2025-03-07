# 使用相对于脚本文件的路径
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONPATH = "$ProjectRoot/src"
uvicorn apps.api.main:app --host 0.0.0.0 --port 8081 --no-use-colors