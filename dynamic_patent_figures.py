# -*- coding: utf-8 -*-
"""
动态专利附图生成模块
根据专利主题和技术领域自动生成对应的专利附图
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 颜色方案
COLORS = {
    'primary': '#1E88E5',    # 主色蓝色
    'secondary': '#43A047',  # 绿色
    'accent': '#FF7043',     # 橙色
    'dark': '#37474F',       # 深灰
    'light': '#ECEFF1',     # 浅灰
    'warning': '#FFA726',   # 警告色
    'purple': '#7E57C2',    # 紫色
    'cyan': '#26C6DA',      # 青色
    'gray': '#9E9E9E',      # 灰色
    'red': '#E53935',        # 红色
    'yellow': '#FDD835',    # 黄色
}

# 技术领域对应的颜色
FIELD_COLORS = {
    '数字孪生': '#7E57C2',
    '人工智能': '#1E88E5',
    '储能': '#43A047',
    '特高压': '#FF7043',
    '区块链': '#FFA726',
    '虚拟电厂': '#26C6DA',
    '6G通信': '#E53935',
    '联邦学习': '#7B1FA2',
}


def save_figure(fig, filepath, dpi=1200):
    """保存图片 - 1200 DPI超高清"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  [OK] 已保存: {os.path.basename(filepath)}")


def get_field_color(tech_field):
    """获取技术领域对应的颜色"""
    return FIELD_COLORS.get(tech_field, COLORS['primary'])


# ========== 图1: 系统总体架构图 ==========
def draw_system_architecture(topic, tech_field, output_dir):
    """生成系统总体架构图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    field_color = get_field_color(tech_field)

    ax.set_title('图1 系统总体架构图', fontsize=16, fontweight='bold', pad=20)

    # 主框 - 数据采集层
    layer1 = FancyBboxPatch((0.5, 7), 3, 2, boxstyle="round,pad=0.1",
                              facecolor=COLORS['primary'], edgecolor='black', linewidth=2)
    ax.add_patch(layer1)
    ax.text(2, 8, '数据采集层\n(传感器/SCADA/IoT)', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

    # 主框 - 数据处理层
    layer2 = FancyBboxPatch((4, 7), 3, 2, boxstyle="round,pad=0.1",
                              facecolor=COLORS['secondary'], edgecolor='black', linewidth=2)
    ax.add_patch(layer2)
    ax.text(5.5, 8, '数据处理层\n(数据清洗/特征提取)', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

    # 主框 - 核心处理层
    layer3 = FancyBboxPatch((7.5, 7), 3, 2, boxstyle="round,pad=0.1",
                              facecolor=field_color, edgecolor='black', linewidth=2)
    ax.add_patch(layer3)
    ax.text(9, 8, f'{tech_field}核心层\n({tech_field}处理)', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

    # 主框 - 应用层
    layer4 = FancyBboxPatch((11, 7), 2.5, 2, boxstyle="round,pad=0.1",
                              facecolor=COLORS['accent'], edgecolor='black', linewidth=2)
    ax.add_patch(layer4)
    ax.text(12.25, 8, '应用层\n(展示/控制)', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

    # 箭头连接
    ax.annotate('', xy=(4, 8), xytext=(3.5, 8), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(7.5, 8), xytext=(7, 8), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(11, 8), xytext=(10.5, 8), arrowprops=dict(arrowstyle='->', lw=2))

    # 下方模块
    modules = [
        (1, 4.5, '历史数据库', COLORS['dark']),
        (3.5, 4.5, '实时数据流', COLORS['dark']),
        (6, 4.5, '外部数据源', COLORS['dark']),
        (8.5, 4.5, '模型参数库', COLORS['dark']),
    ]

    for x, y, text, color in modules:
        rect = FancyBboxPatch((x, 3.5), 2.5, 1.5, boxstyle="round,pad=0.05",
                               facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x+1.25, 4.25, text, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')

    # 底部说明
    ax.text(7, 1.5, f'图1 {topic}系统架构', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图1_系统总体架构图.png')
    save_figure(fig, filepath)


# ========== 图2: 方法流程图 ==========
def draw_method_flowchart(topic, tech_field, output_dir):
    """生成方法流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('图2 方法流程图', fontsize=16, fontweight='bold', pad=20)

    # 流程步骤
    steps = [
        (1, 6, 'S1\n数据采集', COLORS['primary']),
        (3, 6, 'S2\n数据预处理', COLORS['secondary']),
        (5, 6, 'S3\n核心处理', get_field_color(tech_field)),
        (7, 6, 'S4\n分析决策', COLORS['purple']),
        (9, 6, 'S5\n执行控制', COLORS['accent']),
        (11, 6, 'S6\n结果输出', COLORS['dark']),
    ]

    for x, y, text, color in steps:
        rect = FancyBboxPatch((x-0.6, y-0.8), 1.8, 1.6, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.3, y, text, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')

    # 连接箭头
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1][0]-0.6, steps[i+1][1]),
                   xytext=(steps[i][0]+0.6, steps[i][1]),
                   arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # 底部循环说明
    ax.text(7, 3, '反馈优化循环', ha='center', va='center',
            fontsize=11, style='italic', color=COLORS['gray'])

    # 底部说明
    ax.text(7, 1, f'图2 {topic}方法流程', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图2_方法流程图.png')
    save_figure(fig, filepath)


# ========== 图3: 核心模块架构图 ==========
def draw_core_module(topic, tech_field, output_dir):
    """生成核心模块架构图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('图3 核心模块架构图', fontsize=16, fontweight='bold', pad=20)

    field_color = get_field_color(tech_field)

    # 核心处理模块
    core = FancyBboxPatch((4.5, 5.5), 5, 2.5, boxstyle="round,pad=0.2",
                           facecolor=field_color, edgecolor='black', linewidth=3)
    ax.add_patch(core)
    ax.text(7, 6.75, f'{tech_field}核心处理模块', ha='center', va='center',
            fontsize=14, color='white', fontweight='bold')

    # 四个子模块
    sub_modules = [
        (1.5, 3.5, '数据输入\n模块', COLORS['primary']),
        (4.5, 3.5, '算法处理\n模块', COLORS['secondary']),
        (7.5, 3.5, '优化决策\n模块', COLORS['purple']),
        (10.5, 3.5, '结果输出\n模块', COLORS['accent']),
    ]

    for x, y, text, color in sub_modules:
        rect = FancyBboxPatch((x-0.7, y-0.7), 1.8, 1.6, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.1, y, text, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')

    # 连接到核心模块的箭头
    for x, y, _, _ in sub_modules:
        ax.annotate('', xy=(x+0.1, 3.5), xytext=(x+0.1, 4.2),
                   arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # 底部数据流说明
    ax.text(7, 1.5, '数据流: 输入 -> 处理 -> 优化 -> 输出', ha='center', va='center',
            fontsize=11, style='italic')

    ax.text(7, 0.8, f'图3 {topic}核心模块架构', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图3_核心模块架构图.png')
    save_figure(fig, filepath)


# ========== 图4: 数据处理流程图 ==========
def draw_data_processing(topic, tech_field, output_dir):
    """生成数据处理流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('图4 数据处理流程图', fontsize=16, fontweight='bold', pad=20)

    # 左侧输入
    input_box = FancyBboxPatch((0.5, 5), 2, 2, boxstyle="round,pad=0.1",
                                facecolor=COLORS['primary'], edgecolor='black', linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.5, 6, '原始数据\n输入', ha='center', va='center',
            fontsize=11, color='white', fontweight='bold')

    # 三个处理阶段
    stages = [
        (3.5, 5, '数据清洗', COLORS['secondary']),
        (6.5, 5, '特征提取', COLORS['purple']),
        (9.5, 5, '数据融合', COLORS['accent']),
    ]

    for x, y, text, color in stages:
        rect = FancyBboxPatch((x-0.8, y-0.8), 1.8, 1.8, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.1, y, text, ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')

    # 连接箭头
    ax.annotate('', xy=(3.5, 6), xytext=(2.5, 6), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(6.5, 6), xytext=(5.5, 6), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(9.5, 6), xytext=(8.5, 6), arrowprops=dict(arrowstyle='->', lw=2))

    # 右侧输出
    output_box = FancyBboxPatch((11.5, 5), 2, 2, boxstyle="round,pad=0.1",
                                 facecolor=COLORS['dark'], edgecolor='black', linewidth=2)
    ax.add_patch(output_box)
    ax.text(12.5, 6, '处理后\n数据', ha='center', va='center',
            fontsize=11, color='white', fontweight='bold')

    ax.annotate('', xy=(11.5, 6), xytext=(10.3, 6), arrowprops=dict(arrowstyle='->', lw=2))

    # 底部说明
    ax.text(7, 2, '数据处理流水线', ha='center', va='center',
            fontsize=14, fontweight='bold', color=COLORS['dark'])

    ax.text(7, 1, f'图4 {topic}数据处理流程', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图4_数据处理流程图.png')
    save_figure(fig, filepath)


# ========== 图5: 质量评估模块图 ==========
def draw_quality_assessment(topic, tech_field, output_dir):
    """生成质量评估模块图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('图5 质量评估模块图', fontsize=16, fontweight='bold', pad=20)

    # 中心评估模块
    center = FancyBboxPatch((5, 5), 4, 2, boxstyle="round,pad=0.2",
                             facecolor=COLORS['purple'], edgecolor='black', linewidth=3)
    ax.add_patch(center)
    ax.text(7, 6, '质量评估\n中心', ha='center', va='center',
            fontsize=14, color='white', fontweight='bold')

    # 三个评估维度
    dims = [
        (1.5, 7, '准确性\n评估', COLORS['primary']),
        (1.5, 4.5, '完整性\n评估', COLORS['secondary']),
        (7, 7.5, '一致性\n评估', COLORS['accent']),
        (7, 4, '时效性\n评估', COLORS['warning']),
        (10.5, 5.75, '综合评分', COLORS['dark']),
    ]

    for x, y, text, color in dims:
        rect = FancyBboxPatch((x-0.6, y-0.6), 1.4, 1.4, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.1, y, text, ha='center', va='center',
                fontsize=8, color='white', fontweight='bold')

    # 连接箭头
    ax.annotate('', xy=(4.4, 6), xytext=(2, 6.5), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(4.4, 6), xytext=(2, 5), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(5.6, 6), xytext=(7, 7), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(5.6, 6), xytext=(7, 5.5), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(9, 6), xytext=(10.5, 6), arrowprops=dict(arrowstyle='->', lw=2))

    ax.text(7, 1, f'图5 {topic}质量评估模块', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图5_质量评估模块图.png')
    save_figure(fig, filepath)


# ========== 图6: 优化流程图 ==========
def draw_optimization_flowchart(topic, tech_field, output_dir):
    """生成优化流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('图6 优化流程图', fontsize=16, fontweight='bold', pad=20)

    # 主循环流程
    steps = [
        (1.5, 5.5, '初始化\n参数', COLORS['primary']),
        (4, 5.5, '目标\n函数', COLORS['secondary']),
        (6.5, 5.5, '迭代\n优化', get_field_color(tech_field)),
        (9, 5.5, '收敛\n判断', COLORS['purple']),
        (11.5, 5.5, '输出\n结果', COLORS['accent']),
    ]

    for x, y, text, color in steps:
        rect = FancyBboxPatch((x-0.6, y-0.7), 1.4, 1.6, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.1, y, text, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')

    # 连接箭头
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1][0]-0.6, steps[i+1][1]),
                   xytext=(steps[i][0]+0.4, steps[i][1]),
                   arrowprops=dict(arrowstyle='->', lw=2))

    # 反馈回路
    ax.annotate('', xy=(8, 4), xytext=(9, 4),
               arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['red']))
    ax.text(8.5, 3.5, '未收敛', ha='center', va='center', fontsize=9, color=COLORS['red'])

    ax.text(7, 2, '优化迭代循环', ha='center', va='center',
            fontsize=14, fontweight='bold', color=COLORS['dark'])

    ax.text(7, 1, f'图6 {topic}优化流程', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图6_优化流程图.png')
    save_figure(fig, filepath)


# ========== 图7: 人机交互界面示意图 ==========
def draw_hmi_interface(topic, tech_field, output_dir):
    """生成人机交互界面示意图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('图7 人机交互界面示意图', fontsize=16, fontweight='bold', pad=20)

    # 主界面框
    main_box = FancyBboxPatch((1, 1.5), 12, 7, boxstyle="round,pad=0.1",
                               facecolor=COLORS['light'], edgecolor='black', linewidth=2)
    ax.add_patch(main_box)

    # 顶部标题栏
    title_bar = FancyBboxPatch((1, 7), 12, 1, boxstyle="round,pad=0",
                                facecolor=get_field_color(tech_field), edgecolor='black', linewidth=1)
    ax.add_patch(title_bar)
    ax.text(7, 7.5, f'{topic} - 监控系统', ha='center', va='center',
            fontsize=14, color='white', fontweight='bold')

    # 左侧菜单
    menu_items = ['数据监控', '分析报表', '系统配置', '用户管理']
    for i, item in enumerate(menu_items):
        menu = FancyBboxPatch((1.2, 5.5-i*1.2), 2.5, 0.9, boxstyle="round,pad=0.05",
                              facecolor=COLORS['dark'], edgecolor='black', linewidth=1)
        ax.add_patch(menu)
        ax.text(2.45, 5.95-i*1.2, item, ha='center', va='center',
                fontsize=9, color='white')

    # 右侧显示区域
    display = FancyBboxPatch((4, 2), 8.5, 4.5, boxstyle="round,pad=0.1",
                              facecolor='white', edgecolor=COLORS['gray'], linewidth=1)
    ax.add_patch(display)
    ax.text(8.25, 5.5, '[数据显示区域]', ha='center', va='center',
            fontsize=12, color=COLORS['gray'])

    # 底部状态栏
    status = FancyBboxPatch((1, 1.5), 12, 0.6, boxstyle="round,pad=0",
                             facecolor=COLORS['dark'], edgecolor='black', linewidth=1)
    ax.add_patch(status)
    ax.text(2, 1.8, '状态: 正常运行', ha='left', va='center',
            fontsize=9, color='white')
    ax.text(12, 1.8, '时间: 2026-01-01 12:00:00', ha='right', va='center',
            fontsize=9, color='white')

    ax.text(7, 0.8, f'图7 {topic}人机交互界面', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图7_人机交互界面示意图.png')
    save_figure(fig, filepath)


# ========== 图8: 应用场景示意图 ==========
def draw_application_scenarios(topic, tech_field, output_dir):
    """生成应用场景示意图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('图8 应用场景示意图', fontsize=16, fontweight='bold', pad=20)

    # 中心云
    center = Circle((7, 5), 1.2, facecolor=COLORS['primary'], edgecolor='black', linewidth=2)
    ax.add_patch(center)
    ax.text(7, 5.3, '云端\n平台', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

    # 四个场景
    scenarios = [
        (2, 7, '场景1\n智能监控', COLORS['primary']),
        (12, 7, '场景2\n远程控制', COLORS['secondary']),
        (2, 3, '场景3\n数据分析', COLORS['purple']),
        (12, 3, '场景4\n故障诊断', COLORS['accent']),
    ]

    for x, y, text, color in scenarios:
        rect = FancyBboxPatch((x-0.8, y-0.6), 2, 1.4, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.2, y, text, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')

    # 连接线
    for x, y, _, _ in scenarios:
        ax.annotate('', xy=(7, 5), xytext=(x+0.8, y),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color=COLORS['gray']))

    ax.text(7, 1, '多场景应用架构', ha='center', va='center',
            fontsize=14, fontweight='bold', color=COLORS['dark'])

    ax.text(7, 0.5, f'图8 {topic}应用场景', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图8_应用场景示意图.png')
    save_figure(fig, filepath)


# ========== 图9: 具体实施方式示意图 ==========
def draw_implementation(topic, tech_field, output_dir):
    """生成具体实施方式示意图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('图9 具体实施方式示意图', fontsize=16, fontweight='bold', pad=20)

    # 三个实施阶段
    stages = [
        (1.5, 6.5, '实施阶段1\n硬件部署', COLORS['primary']),
        (6, 6.5, '实施阶段2\n软件集成', COLORS['secondary']),
        (10.5, 6.5, '实施阶段3\n系统调试', COLORS['accent']),
    ]

    for x, y, text, color in stages:
        rect = FancyBboxPatch((x-1, y-1), 2.5, 2, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.25, y+0.2, text, ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')

    # 连接箭头
    ax.annotate('', xy=(5, 7.5), xytext=(4, 7.5), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(9, 7.5), xytext=(8, 7.5), arrowprops=dict(arrowstyle='->', lw=2))

    # 下方详细说明框
    detail_box = FancyBboxPatch((1.5, 2), 11, 3.5, boxstyle="round,pad=0.1",
                                  facecolor=COLORS['light'], edgecolor='black', linewidth=1)
    ax.add_patch(detail_box)

    details = [
        '1. 硬件部署: 传感器安装、网络配置',
        '2. 软件集成: 系统部署、功能对接',
        '3. 系统调试: 参数优化、性能测试',
        '4. 试运行: 功能验证、问题修复',
        '5. 正式运行: 全面上线、持续维护',
    ]

    for i, detail in enumerate(details):
        ax.text(2, 4.8-i*0.7, detail, ha='left', va='center',
                fontsize=10, color=COLORS['dark'])

    ax.text(7, 1, f'图9 {topic}具体实施方式', ha='center', va='center',
            fontsize=12, style='italic')

    filepath = os.path.join(output_dir, '图9_具体实施方式示意图.png')
    save_figure(fig, filepath)


# ========== 图10: 效果对比图 ==========
def draw_effect_comparison(topic, tech_field, output_dir):
    """生成效果对比图"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('图10 效果对比图', fontsize=16, fontweight='bold')

    categories = ['效率', '准确性', '稳定性', '成本']
    before = [0.65, 0.70, 0.60, 0.80]
    after = [0.92, 0.95, 0.90, 0.40]

    x = np.arange(len(categories))
    width = 0.35

    colors_before = [COLORS['gray']] * 4
    colors_after = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['purple']]

    for idx, ax in enumerate(axes.flat):
        ax.set_title(f'({chr(97+idx)}) {categories[idx]}对比', fontsize=12, fontweight='bold')

        bars1 = ax.bar(x[0], before[idx], width, label='现有技术', color=COLORS['gray'], alpha=0.7)
        bars2 = ax.bar(x[0]+width+0.1, after[idx], width, label='本发明', color=get_field_color(tech_field))

        ax.set_ylabel('评分')
        ax.set_ylim(0, 1.1)
        ax.legend()

        # 添加数值标签
        ax.text(x[0], before[idx]+0.02, f'{before[idx]:.0%}', ha='center', fontsize=9)
        ax.text(x[0]+width+0.1, after[idx]+0.02, f'{after[idx]:.0%}', ha='center', fontsize=9, fontweight='bold')

        # 计算提升
        improvement = (after[idx] - before[idx]) / before[idx] * 100
        if idx == 3:  # 成本是降低
            improvement = -improvement
        ax.text(0.5, 0.95, f'提升: {improvement:+.1f}%', transform=ax.transAxes,
                ha='center', fontsize=10, color=COLORS['secondary'], fontweight='bold')

    plt.tight_layout()

    filepath = os.path.join(output_dir, '图10_效果对比图.png')
    save_figure(fig, filepath)


def generate_all_figures(topic, tech_field, output_dir):
    """生成所有专利附图"""
    print(f"\n[FIGURES] 正在为专利生成图表...")
    print(f"  主题: {topic}")
    print(f"  技术领域: {tech_field}")
    print(f"  输出目录: {output_dir}")

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 生成10张图表
    draw_system_architecture(topic, tech_field, output_dir)
    draw_method_flowchart(topic, tech_field, output_dir)
    draw_core_module(topic, tech_field, output_dir)
    draw_data_processing(topic, tech_field, output_dir)
    draw_quality_assessment(topic, tech_field, output_dir)
    draw_optimization_flowchart(topic, tech_field, output_dir)
    draw_hmi_interface(topic, tech_field, output_dir)
    draw_application_scenarios(topic, tech_field, output_dir)
    draw_implementation(topic, tech_field, output_dir)
    draw_effect_comparison(topic, tech_field, output_dir)

    print(f"\n[OK] 所有图表生成完成！")

    # 返回生成的图表文件列表
    figures = []
    for i in range(1, 11):
        fig_name = f"图{i}_*.png"
        figures.append(f"图{i}_*.png")
    return figures


if __name__ == '__main__':
    # 测试生成
    output_dir = r'H:\专利\四万亿\高质量专利\专利8_一种基于生成式AI的电网场景模拟与应急演练方法'
    topic = "一种基于区块链的绿电溯源与认证系统"
    tech_field = "区块链"
    generate_all_figures(topic, tech_field, output_dir)
