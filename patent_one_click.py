# -*- coding: utf-8 -*-
"""
一键智能专利生成系统 - 全局版
可以在任意目录运行，自动创建工作目录

使用方法：
    python patent_one_click.py "专利题目" [--output 输出目录]
"""

import os
import sys
import shutil
from datetime import datetime

# Skill目录（代码所在目录）
SKILL_DIR = os.path.dirname(os.path.abspath(__file__))


class PatentOneClick:
    """一键智能专利生成系统"""

    def __init__(self, output_dir: str = None):
        """初始化"""
        if output_dir is None:
            # 默认在当前目录创建patent_output子目录
            output_dir = os.path.join(os.getcwd(), 'patent_output')

        self.output_dir = output_dir
        self.topic = ""
        self.tech_field = ""
        self.generator = None
        self.improver = None

    def _setup_environment(self):
        """设置环境 - 将依赖文件复制到输出目录"""
        # 确保输出目录存在
        os.makedirs(self.output_dir, exist_ok=True)

        # 需要复制的依赖文件
        deps = [
            'patent_templates.py',
            'patent_skills_config.py',
            'smart_patent_generator.py',
            'dynamic_patent_figures.py',
            'patent_self_improver.py',
        ]

        # 复制依赖文件到输出目录
        for dep in deps:
            src = os.path.join(SKILL_DIR, dep)
            dst = os.path.join(self.output_dir, dep)
            if os.path.exists(src) and not os.path.exists(dst):
                shutil.copy2(src, dst)

        # 切换到输出目录
        os.chdir(self.output_dir)

    def generate(self, topic: str) -> bool:
        """一键生成完整专利"""
        self.topic = topic

        print("\n" + "="*70)
        print("           One-Click Patent Generation System v1.0")
        print("="*70)
        print(f"[START] Patent Topic: {topic}")
        print(f"[TIME] Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[OUTPUT] Directory: {self.output_dir}")
        print("="*70)

        # 设置环境
        self._setup_environment()

        # 导入依赖（现在在正确的目录下）
        from patent_templates import detect_tech_field, TECH_FIELDS
        from patent_skills_config import check_skills_available
        from smart_patent_generator import SmartPatentGenerator
        from patent_self_improver import create_self_improving_patent_system

        # 步骤1: 检测技术领域
        print("\n[STEP 1] Detecting Technical Field...")
        self.tech_field = detect_tech_field(topic)
        field_info = TECH_FIELDS.get(self.tech_field, TECH_FIELDS["人工智能"])
        print(f"  Technical Field: {self.tech_field} - {field_info['name']}")
        print(f"  Core Keywords: {', '.join(field_info['keywords'][:5])}")

        # 步骤2: 创建自我改进系统
        print("\n[STEP 2] Initializing Smart Audit System...")
        self.improver = create_self_improving_patent_system()
        print(f"  Search System: Loaded")
        print(f"  Audit System: Loaded")
        print(f"  Improvement System: Loaded")

        # 步骤3: 生成初始专利内容
        print("\n[STEP 3] Generating Initial Patent Content...")
        self.generator = SmartPatentGenerator(self.output_dir)
        self.generator.topic = topic
        self.generator.tech_field = self.tech_field
        self.generator.template = {}

        from patent_templates import get_template
        self.generator.template = get_template(topic, self.tech_field)

        patent_content = {
            "title": topic,
            "tech_field": field_info['name'],
            "abstract": self.generator.template.get("abstract", ""),
            "background": self.generator.template.get("background", ""),
            "invention": self.generator.template.get("invention", ""),
            "implementation": self.generator.template.get("implementation", ""),
            "claims": self.generator.template.get("claims", []),
            "effect_comparison": self.generator._generate_effect_comparison(),
        }

        print(f"  Initial content generated")

        # 步骤4: 审核 + 自我改进
        print("\n[STEP 4] Smart Audit & Self-Improvement...")
        print("  Starting Search-Audit-Modify Loop...")

        improved_content, success = self.improver.improve_patent(
            patent_content, topic, self.tech_field
        )

        print(f"\n  Iteration: {self.improver.iteration} rounds")
        print(f"  Final Score: {self.improver.history[-1]['audit']['score']}/100")

        self.generator.template.update(improved_content)

        # 步骤5: 生成高清图表
        print("\n[STEP 5] Generating HD Patent Figures (1200 DPI)...")
        self.generator._generate_figures()
        self.generator.figures_generated = True
        print(f"  Figures generated")

        # 步骤6: 生成Word文档
        print("\n[STEP 6] Generating Word Patent Document...")
        self.generator._generate_word_doc()
        self.generator.doc_generated = True
        print(f"  Document generated")

        self._print_summary()
        return success

    def _print_summary(self):
        """打印总结"""
        print("\n" + "="*70)
        print("                    PATENT GENERATED!")
        print("="*70)

        doc_files = [f for f in os.listdir(self.output_dir)
                    if f.startswith('Patent_') and f.endswith('.docx')]
        if not doc_files:
            doc_files = [f for f in os.listdir(self.output_dir)
                        if f.startswith('专利_') and f.endswith('.docx')]

        if doc_files:
            latest_doc = max(doc_files, key=lambda x: os.path.getmtime(os.path.join(self.output_dir, x)))
            size = os.path.getsize(os.path.join(self.output_dir, latest_doc)) / 1024 / 1024
            print(f"\n[DOC] Word Document: {latest_doc} ({size:.2f} MB)")

        png_count = len([f for f in os.listdir(self.output_dir) if f.endswith('.png')])
        print(f"[FIG] Patent Figures: {png_count} (1200 DPI)")

        if self.improver:
            print(f"\n[ITERATION] Audit Iterations: {self.improver.iteration} rounds")
            if self.improver.history:
                final_audit = self.improver.history[-1]['audit']
                print(f"[SCORE] Final Score: {final_audit['score']}/100")
                print(f"[PASSED] Status: {'Passed' if final_audit['passed'] else 'Not Passed'}")

        print("\n" + "="*70)
        print("[OK] Patent generation completed!")
        print("="*70)


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description='One-Click Patent Generation System')
    parser.add_argument('topic', nargs='?', help='Patent topic')
    parser.add_argument('--output', '-o', help='Output directory (default: ./patent_output)')

    args = parser.parse_args()

    if not args.topic:
        print("\n[START] One-Click Patent Generation System v1.0")
        print("="*60)
        print("\nUsage:")
        print("  python patent_one_click.py \"patent topic\"")
        print("  python patent_one_click.py \"patent topic\" -o /path/to/output")
        print()
        args.topic = input("Enter patent topic: ").strip()
        if not args.topic:
            print("[ERROR] No topic provided")
            return

    generator = PatentOneClick(args.output)
    success = generator.generate(args.topic)

    if success:
        print("\n[SUCCESS] Patent generated successfully!")
    else:
        print("\n[WARN] Patent generated, but audit not fully passed.")


if __name__ == "__main__":
    main()
