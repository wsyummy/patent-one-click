# -*- coding: utf-8 -*-
"""
电网相关专利模板系统
包含多个技术领域的专利模板，可根据题目自动填充
"""

# 技术领域配置
TECH_FIELDS = {
    "数字孪生": {
        "name": "数字孪生电网",
        "keywords": ["数字孪生", "虚拟电网", "仿真模型", "实时映射"],
        "core_tech": "数字孪生技术",
        "application": "电网运维与调度"
    },
    "人工智能": {
        "name": "人工智能电网",
        "keywords": ["人工智能", "AI", "机器学习", "深度学习", "神经网络"],
        "core_tech": "人工智能算法",
        "application": "电网智能决策"
    },
    "储能": {
        "name": "储能系统",
        "keywords": ["储能", "电池", "电化学", "能量管理"],
        "core_tech": "储能技术",
        "application": "新能源消纳与调峰"
    },
    "特高压": {
        "name": "特高压技术",
        "keywords": ["特高压", "UHV", "直流输电", "换流站"],
        "core_tech": "特高压输电",
        "application": "远距离电能输送"
    },
    "区块链": {
        "name": "区块链电力交易",
        "keywords": ["区块链", "智能合约", "分布式账本", "电力交易"],
        "core_tech": "区块链技术",
        "application": "电力市场交易"
    },
    "虚拟电厂": {
        "name": "虚拟电厂",
        "keywords": ["虚拟电厂", "VPP", "需求响应", "聚合商"],
        "core_tech": "多能互补协调控制",
        "application": "分布式资源管理"
    },
    "6G通信": {
        "name": "6G电网通信",
        "keywords": ["6G", "卫星通信", "物联网", "通信融合"],
        "core_tech": "6G通信技术",
        "application": "电网全域覆盖"
    },
    "联邦学习": {
        "name": "联邦学习电网",
        "keywords": ["联邦学习", "隐私计算", "协同学习", "数据共享"],
        "core_tech": "联邦学习框架",
        "application": "跨区域电网协同"
    }
}


def detect_tech_field(topic: str) -> str:
    """
    从专利题目检测技术领域

    Args:
        topic: 专利题目

    Returns:
        匹配的技术领域名称
    """
    topic_lower = topic.lower()

    for field_key, field_info in TECH_FIELDS.items():
        for keyword in field_info["keywords"]:
            if keyword.lower() in topic_lower:
                return field_key

    # 默认返回"人工智能"
    return "人工智能"


def get_template(topic: str, tech_field: str = None) -> dict:
    """
    获取专利模板

    Args:
        topic: 专利题目
        tech_field: 技术领域（可选，自动检测）

    Returns:
        专利内容模板
    """
    if not tech_field:
        tech_field = detect_tech_field(topic)

    field_info = TECH_FIELDS.get(tech_field, TECH_FIELDS["人工智能"])

    # 构建模板
    template = {
        "title": topic,
        "tech_field": field_info["name"],
        "core_tech": field_info["core_tech"],
        "application": field_info["application"],
        "field_key": tech_field,
        # 摘要模板
        "abstract": _generate_abstract(topic, field_info),
        # 背景技术模板
        "background": _generate_background(topic, field_info),
        # 发明内容模板
        "invention": _generate_invention(topic, field_info),
        # 具体实施方式模板
        "implementation": _generate_implementation(topic, field_info),
        # 权利要求模板
        "claims": _generate_claims(topic, field_info),
    }

    return template


def _generate_abstract(topic: str, field_info: dict) -> str:
    """生成摘要"""
    return f"""本发明公开了一种{topic}。该方法包括：接收电网运行数据和用户需求；通过{field_info['core_tech']}进行数据处理和分析；采用智能算法实现电网优化决策；生成对应的控制指令并执行。所述方法能够有效提升电网的运行效率和可靠性，降低运维成本，提高新能源消纳能力。实施例表明，本发明可使电网运行效率提升15%以上，故障响应时间缩短30%。"""


def _generate_background(topic: str, field_info: dict) -> str:
    """生成背景技术"""
    return f"""随着电网规模的不断扩大和新能源的快速接入，电网运行面临着越来越多的挑战。传统的电网调度方式已经难以满足现代电网的需求。

{field_info['application']}是当前电网发展的重要方向。然而，现有技术在数据处理精度、响应速度和智能化程度方面存在不足。

{field_info['core_tech']}在电网领域的应用研究已经取得了一定进展，但在实际应用中仍存在以下问题：
1. 数据处理效率低，难以满足实时性要求
2. 模型泛化能力不足，无法适应复杂场景
3. 与现有系统的兼容性差

因此，需要一种新的{topic}来解决上述问题。"""


def _generate_invention(topic: str, field_info: dict) -> str:
    """生成发明内容"""
    return f"""本发明的目的是提供一种{topic}，以解决现有技术中存在的上述问题。

本发明采用以下技术方案：

一种{topic}，其特征在于，包括：
a. 数据采集模块，用于收集电网实时运行数据；
b. 数据处理模块，基于{field_info['core_tech']}对采集的数据进行分析；
c. 决策优化模块，采用智能算法生成优化方案；
d. 执行控制模块，负责将优化方案下发至相关设备。

进一步的，所述数据处理模块采用多源数据融合技术，提高数据质量。

本发明具有以下有益效果：
1. 提高了电网运行的智能化水平
2. 缩短了故障处理时间
3. 降低了运维成本
4. 提升了新能源消纳能力"""


def _generate_implementation(topic: str, field_info: dict) -> str:
    """生成具体实施方式"""
    return f"""下面结合具体实施例对本发明进行详细说明。

实施例1：系统架构

本发明所述的{topic}，包括数据采集层、数据处理层和应用层。数据采集层负责从SCADA系统、PMU装置和物联网传感器获取数据；数据处理层实现{field_info['core_tech']}的核心算法；应用层提供人机交互界面。

实施例2：数据处理流程

步骤S1：数据采集。通过部署在电网各节点的传感器采集电压、电流、功率等实时数据。

步骤S2：数据预处理。对采集的数据进行清洗、去噪和标准化处理。

步骤S3：智能分析。应用{field_info['core_tech']}进行模式识别和趋势预测。

步骤S4：决策优化。基于分析结果生成优化方案。

步骤S5：方案执行。将优化方案转化为控制指令并下发执行。

实施例3：应用场景

本发明可广泛应用于{field_info['application']}场景，包括电网调度、故障处理、负荷预测等。"""


def _generate_claims(topic: str, field_info: dict) -> list:
    """生成权利要求"""
    return [
        f"1. 一种{topic}，其特征在于，包括：",
        f"a. 数据采集模块，用于收集电网运行数据；",
        f"b. 数据处理模块，基于{field_info['core_tech']}进行数据分析和处理；",
        f"c. 决策优化模块，用于生成优化方案；",
        f"d. 执行控制模块，用于执行优化方案。",
        "",
        f"2. 根据权利要求1所述的{topic}，其特征在于，",
        f"所述数据采集模块支持多种数据源，包括SCADA、PMU和物联网传感器。",
        "",
        f"3. 根据权利要求1或2所述的{topic}，其特征在于，",
        f"所述数据处理模块采用{field_info['core_tech']}算法，",
        f"能够实现高精度的状态估计和趋势预测。",
        "",
        f"4. 根据权利要求1-3任一项所述的{topic}，其特征在于，",
        f"还包括人机交互模块，用于可视化展示和用户交互。",
        "",
        f"5. 根据权利要求1-4任一项所述的{topic}，其特征在于，",
        f"所述决策优化模块采用强化学习算法，能够自适应调整优化策略。",
    ]


def generate_figure_config(topic: str, tech_field: str) -> list:
    """
    根据题目生成图表配置

    Args:
        topic: 专利题目
        tech_field: 技术领域

    Returns:
        图表配置列表
    """
    field_info = TECH_FIELDS.get(tech_field, TECH_FIELDS["人工智能"])

    # 基础图表配置
    figures = [
        {
            "id": 1,
            "title": "系统总体架构图",
            "type": "architecture",
            "description": "展示系统的整体架构，包括数据采集、处理、应用层"
        },
        {
            "id": 2,
            "title": "方法流程图",
            "type": "flowchart",
            "description": "展示方法的执行流程"
        },
    ]

    # 根据技术领域添加特定图表
    if tech_field in ["数字孪生", "人工智能"]:
        figures.append({
            "id": 3,
            "title": f"{field_info['core_tech']}模型架构图",
            "type": "model",
            "description": "展示核心算法的模型结构"
        })
        figures.append({
            "id": 4,
            "title": "神经网络结构图",
            "type": "network",
            "description": "展示神经网络的层次结构"
        })
    elif tech_field == "储能":
        figures.extend([
            {
                "id": 3,
                "title": "储能系统架构图",
                "type": "architecture",
                "description": "展示储能系统的组成结构"
            },
            {
                "id": 4,
                "title": "能量管理流程图",
                "type": "flowchart",
                "description": "展示能量管理流程"
            }
        ])
    elif tech_field == "区块链":
        figures.extend([
            {
                "id": 3,
                "title": "区块链架构图",
                "type": "blockchain",
                "description": "展示区块链网络结构"
            },
            {
                "id": 4,
                "title": "智能合约流程图",
                "type": "flowchart",
                "description": "展示智能合约执行流程"
            }
        ])

    # 通用图表
    figures.extend([
        {
            "id": 5,
            "title": "质量评估模块图",
            "type": "module",
            "description": "展示质量评估模块结构"
        },
        {
            "id": 6,
            "title": "优化流程图",
            "type": "flowchart",
            "description": "展示优化决策流程"
        },
        {
            "id": 7,
            "title": "人机交互界面示意图",
            "type": "ui",
            "description": "展示用户界面设计"
        },
        {
            "id": 8,
            "title": "应用场景示意图",
            "type": "scenario",
            "description": "展示典型应用场景"
        },
        {
            "id": 9,
            "title": "具体实施方式示意图",
            "type": "implementation",
            "description": "展示实施方式示例"
        },
        {
            "id": 10,
            "title": "效果对比图",
            "type": "comparison",
            "description": "展示技术效果对比"
        }
    ])

    return figures


# 测试函数
def test_template():
    """测试模板生成"""
    test_topics = [
        "一种基于数字孪生的电网故障诊断方法",
        "一种基于人工智能的电网调度优化方法",
        "一种基于区块链的电力交易方法",
        "一种储能系统优化控制方法"
    ]

    for topic in test_topics:
        field = detect_tech_field(topic)
        template = get_template(topic, field)
        print(f"\n题目: {topic}")
        print(f"技术领域: {field}")
        print(f"摘要: {template['abstract'][:100]}...")


if __name__ == "__main__":
    test_template()
