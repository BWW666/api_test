# 接口自动化测试项目 (API Automation Test)

## 项目简介
基于 Python + pytest + requests 搭建的接口自动化测试框架。采用数据驱动（参数化）设计，支持统一请求封装、日志记录及 HTML 测试报告生成。

## 技术栈
- 语言：Python 3.12
- 框架：pytest
- 请求库：requests
- 报告：pytest-html
- 其他：JSON数据驱动、logging日志封装

## 目录结构
```text
api_test/
├── common/          # 公共方法（请求封装、日志封装）
├── config/          # 配置文件（全局URL、超时时间）
├── data/            # 测试数据存放
├── reports/         # 测试报告生成目录
├── test_cases/      # 测试用例目录
├── conftest.py      # pytest全局配置
├── mock_server.py   # 本地 Mock 服务（用于模拟接口返回，避免外网超时）
└── README.md        # 说明文档