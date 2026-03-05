#!/bin/bash
# Patent One Click - 安装脚本

echo "========================================="
echo "  Patent One Click 安装程序"
echo "========================================="

# 检查Python
if ! command -v python &> /dev/null; then
    echo "Error: Python not found. Please install Python 3.8+"
    exit 1
fi

echo "Python found: $(python --version)"

# 安装依赖
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "========================================="
echo "  安装完成!"
echo "========================================="
echo ""
echo "使用方法:"
echo "  python patent_one_click.py \"专利题目\""
echo ""
echo "示例:"
echo '  python patent_one_click.py "一种基于区块链的绿电溯源与认证系统"'
echo ""
