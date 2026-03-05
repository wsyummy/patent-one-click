# -*- coding: utf-8 -*-
"""
专利skill配置
整合patent-specialist和patent-search的专业能力
"""

import os

# Skill路径配置
SKILLS_DIR = r"H:\智能体技能合集\good_skills-main"
PATENT_SPECIALIST_DIR = os.path.join(SKILLS_DIR, "patent-specialist")
PATENT_SEARCH_DIR = os.path.join(SKILLS_DIR, "patent-search")

# Skill文件路径
PATENT_SPECIALIST_SKILL = os.path.join(PATENT_SPECIALIST_DIR, "SKILL.md")
PATENT_SEARCH_SKILL = os.path.join(PATENT_SEARCH_DIR, "SKILL.md")

# 防御性创新扩展策略
INNOVATION_EXTENSIONS = {
    "维度扩展": {
        "description": "单一指标场景",
        "example": "并发数 → 并发数+吞吐量+延迟"
    },
    "场景扩展": {
        "description": "特定输入场景",
        "example": "短文本 → 短文本+长文本+多模态"
    },
    "层级扩展": {
        "description": "单一技术层级",
        "example": "模型层 → 模型层+调度层+存储层"
    },
    "稳定性扩展": {
        "description": "容错要求",
        "example": "正常流程 → 正常流程+异常处理+回退机制"
    },
    "自动化扩展": {
        "description": "手动操作场景",
        "example": "参数配置 → 参数配置+自动校准+在线学习"
    }
}

# 技术术语规范
TECH_TERMS = {
    "配置": {"recommended": "配置为", "avoid": "设置为"},
    "响应": {"recommended": "响应于", "avoid": "当...时"},
    "确定": {"recommended": "基于...确定", "avoid": "计算出"},
    "判定": {"recommended": "判断...是否", "avoid": "检查"},
    "执行": {"recommended": "执行...操作", "avoid": "做"},
    "调整": {"recommended": "动态调整", "avoid": "改变"},
    "优化": {"recommended": "优化调整", "avoid": "改进"}
}

# 专利撰写四原则
PATENT_PRINCIPLES = {
    "公开充分": "技术方案必须足够详细，本领域技术人员能够实现",
    "保护范围合理": "权利要求书的保护范围既不能太大（被无效），也不能太小（失去保护意义）",
    "创新性突出": "突出与现有技术的区别，建立技术贡献的清晰叙事",
    "层次分明": "从独立权利要求到从属权利要求，形成金字塔结构"
}


def load_patent_specialist_knowledge() -> str:
    """加载patent-specialist的核心知识"""
    try:
        if os.path.exists(PATENT_SPECIALIST_SKILL):
            with open(PATENT_SPECIALIST_SKILL, 'r', encoding='utf-8') as f:
                return f.read()
    except Exception as e:
        print(f"加载patent-specialist失败: {e}")
    return ""


def load_patent_search_knowledge() -> str:
    """加载patent-search的核心知识"""
    try:
        if os.path.exists(PATENT_SEARCH_SKILL):
            with open(PATENT_SEARCH_SKILL, 'r', encoding='utf-8') as f:
                return f.read()
    except Exception as e:
        print(f"加载patent-search失败: {e}")
    return ""


# 可用的专利数据库
PATENT_DATABASES = {
    "CNIPA": {"name": "中国国家知识产权局", "url": "https://www.cnipa.gov.cn"},
    "USPTO": {"name": "美国专利商标局", "url": "https://patents.google.com"},
    "EPO": {"name": "欧洲专利局", "url": "https://worldwide.espacenet.com"},
    "Google Patents": {"name": "Google Patents", "url": "https://patents.google.com"},
    "WIPO": {"name": "世界知识产权组织", "url": "https://patentscope.wipo.int"}
}


def check_skills_available() -> dict:
    """检查skill是否可用"""
    return {
        "patent_specialist": os.path.exists(PATENT_SPECIALIST_DIR),
        "patent_search": os.path.exists(PATENT_SEARCH_DIR),
        "patent_specialist_file": os.path.exists(PATENT_SPECIALIST_SKILL),
        "patent_search_file": os.path.exists(PATENT_SEARCH_SKILL)
    }
