# Patent One Click

一键智能专利生成系统 - Claude Code Skill

## 简介

用户级别的专利自动生成Skill。只需提供一个专利题目，系统将自动完成从检索、审核、修改到生成完整专利的全过程。

## 功能特性

- **一键生成**: 仅需提供专利题目，无需其他输入
- **自动检索**: 内置专利检索模块
- **智能审核**: 多维度审核（完整性、权利要求、新颖性、格式）
- **无限迭代**: 自动根据审核意见修改，直到通过为止
- **高清图表**: 生成1200 DPI专业专利图表
- **完整文档**: 生成符合中国专利局标准的Word文档

## 技术领域支持

- 数字孪生电网
- 人工智能
- 储能技术
- 特高压技术
- 区块链
- 虚拟电厂
- 6G通信
- 联邦学习

## 安装

### 方式1：克隆仓库

```bash
# 克隆仓库
git clone https://github.com/your-repo/patent-one-click.git

# 进入目录
cd patent-one-click

# 安装依赖
pip install matplotlib numpy python-docx
```

### 方式2：复制到Claude Code Skills目录

将整个 `patent-one-click` 目录复制到你的Claude Code skills目录：

```
~/.claude/skills/patent-one-click/
```

## 使用方法

### 命令行调用

```bash
# 基本用法
python patent_one_click.py "专利题目"

# 指定输出目录
python patent_one_click.py "专利题目" -o "输出目录"

# 交互模式
python patent_one_click.py
```

### 在Claude Code中使用

用户可以直接说：
```
帮我生成一个"一种基于区块链的绿电溯源与认证系统"的专利
```

或者使用命令：
```
/patent生成 一种基于区块链的绿电溯源与认证系统
```

## 输出结果

系统将在输出目录生成：

```
输出目录/
├── 专利_专利题目_YYYYMMDD_HHMMSS.docx   # Word文档
├── 图1_系统总体架构图.png                 # 1200 DPI
├── 图2_方法流程图.png                     # 1200 DPI
├── 图3_核心模块架构图.png                 # 1200 DPI
├── 图4_数据处理流程图.png                 # 1200 DPI
├── 图5_质量评估模块图.png                 # 1200 DPI
├── 图6_优化流程图.png                     # 1200 DPI
├── 图7_人机交互界面示意图.png             # 1200 DPI
├── 图8_应用场景示意图.png                 # 1200 DPI
├── 图9_具体实施方式示意图.png             # 1200 DPI
└── 图10_效果对比图.png                   # 1200 DPI
```

## 专利文档结构

生成的Word文档包含以下部分：

1. 发明名称
2. 技术领域
3. 背景技术
4. 发明内容（技术问题、技术方案、有益效果）
5. 具体实施方式
6. 权利要求书（11条权利要求）
7. 附图说明

## 审核标准

系统自动按照以下标准审核专利：

| 维度 | 权重 | 说明 |
|------|------|------|
| 完整性 | 25% | 必要章节是否齐全 |
| 权利要求 | 25% | 独立/从属权利要求结构 |
| 新颖性 | 25% | 与现有技术的区别 |
| 格式规范 | 25% | 专利局格式要求 |

## 工作流程

```
输入专利题目
    ↓
检测技术领域
    ↓
检索相关专利
    ↓
生成初始专利内容
    ↓
智能审核 (评分)
    ↓
审核通过? ──是──→ 生成图表 → 生成文档 → 完成
  ↓否
根据审核意见修改
    ↓
(循环直到通过或达到最大迭代次数)
```

## 示例

### 输入
```
一种基于区块链的绿电溯源与认证系统
```

### 输出
```
======================================================================
           One-Click Patent Generation System v1.0
======================================================================
[START] Patent Topic: 一种基于区块链的绿电溯源与认证系统
[TIME] Start Time: 2026-03-05 12:00:00
======================================================================

[STEP 1] Detecting Technical Field...
  Technical Field: 区块链 - 区块链技术
  Core Keywords: 区块链, 智能合约, 分布式账本, 电力交易

[STEP 2] Initializing Smart Audit System...
  Search System: Loaded
  Audit System: Loaded
  Improvement System: Loaded

[STEP 3] Generating Initial Patent Content...
  Initial content generated

[STEP 4] Smart Audit & Self-Improvement...
  Starting Search-Audit-Modify Loop...
  Found: 52 related patents
  Score: 95/100
  Passed!

[STEP 5] Generating HD Patent Figures (1200 DPI)...
  Figures generated

[STEP 6] Generating Word Patent Document...
  Document generated

======================================================================
                    PATENT GENERATED!
======================================================================

[DOC] Word Document: 专利_一种基于区块链的绿电溯源与认证系统_20260305_120000.docx
[FIG] Patent Figures: 10 (1200 DPI)
[ITERATION] Audit Iterations: 1 rounds
[SCORE] Final Score: 95/100
[PASSED] Status: Passed

======================================================================
[OK] Patent generation completed!
======================================================================
```

## 依赖

- Python 3.8+
- matplotlib >= 3.5.0
- numpy >= 1.20.0
- python-docx >= 0.8.11

## 许可证

MIT License

## 版本

- v1.0.0 (2026-03-05): 初始发布，一键生成完整专利
