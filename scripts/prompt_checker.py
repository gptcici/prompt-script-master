#!/usr/bin/env python3
"""Lightweight checker for current Prompt Script Master video prompts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SECTION_HINTS = {
    "正文提示词": ["【正文提示词】"],
    "负面提示词": ["【负面提示词】"],
    "光源锚点": ["光源", "主光源", "夕阳", "侧逆光", "补光"],
    "物理动力学锚点": ["物理动力学", "风向", "山风", "柔体", "发丝", "披帛", "纱幔", "雨线", "烟雾", "水面", "粒子", "接触", "碰撞", "惯性", "重力", "消散", "重量", "回弹"],
    "镜头时间轴": ["镜头一", "0-", "秒"],
}

NEGATIVE_CATEGORIES = [["人物类"], ["动作类"], ["动力学类", "风力类"], ["场景类"], ["风格类"]]
SHOT_RE = re.compile(r"\d+\s*[-—]\s*\d+\s*秒[^\n。]*")
DEPRECATED_MARKERS = ["【全程" + "总定调】", "【时间轴" + "分段】", "【全局" + "收尾】"]

CAMERA_HINTS = ["镜头", "机位", "运镜", "推", "拉", "横移", "环绕", "跟拍", "俯视", "特写", "远景", "中景", "近景"]
ACTION_HINTS = ["动作", "走", "坐", "弹", "拨", "抬", "转", "看", "凝视", "回头", "停步", "伸手", "表情", "头部", "手", "身体", "肩", "衣", "发"]
ENV_HINTS = ["光", "阴影", "风", "云", "景深", "虚化", "背景", "纱幔", "环境", "透光"]
PERSON_HINTS = ["人物", "她", "他", "女孩", "少女", "女性", "男性", "歌手", "演员", "角色", "主角", "女主", "男主"]
EXPRESSION_HINTS = ["眼神", "眉", "嘴", "唇", "表情", "面部", "肩", "手", "身体", "重心", "情绪"]
MOUTH_TRIGGER_HINTS = ["唱", "演唱", "说话", "念白", "对口型", "口型", "台词", "喊", "哼唱"]
MOUTH_DETAIL_HINTS = ["下颌", "嘴唇", "唇部", "开合", "呼吸", "口型", "气息"]
CLOSEUP_HINTS = ["中近景", "近景", "特写", "面部特写", "情绪近景", "半身近景"]
FACE_LIGHT_HINTS = ["鼻梁", "眼窝", "颧骨", "下颌", "眼神光", "瞳孔", "皮肤", "面部光影", "面光", "骨骼"]
WIND_OBJECT_HINTS = ["发丝", "头发", "碎发", "披帛", "袖口", "裙摆", "衣摆", "丝带", "珠链", "流苏", "纱幔", "竹叶", "云雾", "云海", "水面", "烟", "雨", "雪", "火焰", "灰尘", "花瓣", "粒子", "纸张", "门", "杯", "琴弦", "武器", "液体", "涟漪"]
WIND_PHYSICS_HINTS = ["风向", "吹向", "重量", "惯性", "延迟", "回弹", "下坠", "鼓起", "拉伸", "翻卷", "速度差", "动力来源", "运动路径", "接触点", "碰撞", "反作用", "支点", "转轴", "摩擦", "涟漪", "扩散", "消散", "受光", "落点", "停止位置", "最终状态"]
FAILURE_WORDS_IN_MAIN = ["不要", "避免", "不能", "不得", "不允许", "无卡顿", "不会"]
SEQUENCE_TRIGGER_HINTS = ["继续上一段", "接着上一条", "下一段", "第二段", "第三段", "系列", "连续剧情", "首帧", "尾帧"]
SEQUENCE_STATE_HINTS = ["already_happened", "current_clip_only", "reserved_for_later", "planned_start_state", "planned_end_state", "连续片段状态胶囊", "已发生", "当前片段", "保留给未来"]
MULTI_REF_HINTS = ["图1", "图2", "参考图1", "参考图2", "Mixed 1", "Mixed 2", "锁脸", "换装", "多图"]
REFERENCE_CONTRACT_HINTS = ["参考图职责", "主职责", "继承内容", "忽略内容", "只用于", "不继承", "不控制"]
RETAKE_HINTS = ["重拍", "retake", "修复", "复盘", "失败归因", "这版不对", "脸不像", "风向乱", "动作怪"]
RETAKE_DIAG_HINTS = ["失败归因", "修复策略", "identity drift", "costume drift", "mouth failure", "wind conflict", "连续性", "参考图污染"]

DIRECTOR_TRIGGER_HINTS = ["电影感", "氛围感", "导演感", "剧情", "分镜", "AIMV", "MV", "情绪", "转折", "揭示"]
DIRECTOR_INTENT_HINTS = ["镜头意图", "目的是", "让观众", "情绪从", "转为", "服务", "潜台词"]
MOTION_CONTRACT_HINTS = ["终点", "落点", "物理结果", "力量", "节拍", "起始状态", "结束状态", "造成", "停在"]
MULTI_CHARACTER_HINTS = ["两人", "多人", "群像", "群演", "伴舞", "对话", "众人", "背景人物", "前景人物"]
BLOCKING_HINTS = ["微动作", "单一反应", "动作层级", "主角", "背景", "站位", "眼线", "队形"]
LIGHTING_CONTRACT_HINTS = ["主光源", "色温", "光质", "阴影", "反射", "眼神光", "轮廓光", "月光", "烛光", "灯笼", "窗光", "舞台灯"]
PRO_SHOT_HINTS = ["镜头清单", "shot list", "广告片", "专业分镜", "镜头合约", "客户", "商业片", "treatment"]
PRO_SHOT_CONTRACT_HINTS = ["镜头目的", "连续锚点", "起始状态", "结束状态", "风险", "参考图职责", "屏幕方向"]
ITERATION_HINTS = ["再来一版", "只改", "保留", "换种子", "重抽", "局部编辑", "后期修", "变量"]
ITERATION_CONTROL_HINTS = ["单变量", "只改一个", "判定", "保留", "局部编辑", "换种子", "改写提示词"]

SLOP_HINTS = ["电影感", "高级感", "氛围感", "质感", "震撼", "唯美", "梦幻", "真实感", "大片感", "动感", "8K", "masterpiece", "best quality", "超高清", "不要AI", "不要 AI", "不要塑料"]
CONCRETE_REWRITE_HINTS = ["主光", "机位", "景别", "运镜", "色温", "阴影", "反射", "材质", "动作", "路径", "终点", "接触", "声音", "节奏", "构图", "镜头"]
BUDGET_TRIGGER_HINTS = ["复杂", "多参考", "多人物", "多镜头", "锁脸", "大动作", "提示词太长", "很多元素", "同时"]
BUDGET_HINTS = ["主预算", "次预算", "primary", "secondary", "压缩", "拆分", "优先", "预算", "economized"]
DENSITY_TRIGGER_HINTS = ["走进", "坐下", "弹", "落泪", "起身", "离开", "转场", "多个地点", "多轮对白", "很多动作", "同时发生", "然后", "再", "最后"]
DENSITY_HINTS = ["当前片段", "一个核心事件", "一个可见", "终点", "拆成", "下一段", "reserved_for_later", "this_clip_only"]
MODEL_MECHANICS_HINTS = ["注意力", "预算", "否定", "参考图压过文字", "细节面积", "错误累积", "漂移", "不听话", "模型机制"]

SHOT_CONTRACT_TRIGGER_HINTS = ["镜头语言", "镜头感", "景别", "机位", "运镜", "焦点", "转场", "分镜", "shot list", "storyboard", "电影感"]
SHOT_CONTRACT_HINTS = ["镜头意图", "主体优先级", "起始画面", "结束画面", "起点", "终点", "焦点", "风险", "镜头目的"]
SHOT_SCALE_HINTS = ["大远景", "远景", "全身", "中景", "半身", "中近景", "近景", "特写", "微距"]
CAMERA_MOVEMENT_TRIGGER_HINTS = ["推近", "拉远", "横移", "跟拍", "环绕", "摇臂", "航拍", "手持", "焦点转移", "rack focus"]
CAMERA_MOVEMENT_FIT_HINTS = ["稳定", "慢速", "起点", "终点", "锁脸", "口型", "手部", "产品", "文字", "不抢动作", "减少"]
MULTISHOT_TRIGGER_HINTS = ["多镜头", "镜头一", "镜头二", "切点", "15秒", "10秒", "8秒", "分镜"]
MULTISHOT_FIT_HINTS = ["2-4", "2-3", "镜头数量", "切点", "一个核心", "一个主运镜", "信息量", "建立", "推进", "落点"]
AXIS_TRIGGER_HINTS = ["连续镜头", "首帧", "尾帧", "下一段", "对话", "打斗", "舞台走位", "方向", "轴线"]
AXIS_HINTS = ["屏幕方向", "视线", "眼线", "入画", "出画", "轴线", "光源方向", "物理方向", "道具位置", "起止状态"]
ANIMATION_CAMERA_TRIGGER_HINTS = ["2D", "动漫", "二次元", "手绘", "漫画", "分镜图", "storyboard", "动画"]
ANIMATION_CAMERA_HINTS = ["多平面", "前景层", "背景层", "cel", "停帧", "冲击帧", "拖影", "速度线", "动画"]

MODE_TRIGGER_HINTS = ["图生视频", "首帧", "尾帧", "续写", "动起来", "视频续写", "图片生成", "海报", "角色图", "三视图", "压缩版", "简短版", "一句话"]
MODE_STANDARD_HINTS = ["T2V", "I2V", "R2V", "FLF2V", "IMAGE", "模式", "长度档位", "只写图片看不出来", "压缩版", "快速视频", "标准视频", "高控制"]
REFERENCE_VISIBILITY_TRIGGER_HINTS = ["上传图片", "参考图", "图1", "图2", "首帧", "尾帧", "图生视频", "动起来", "锁脸", "换装", "重绘", "三视图", "人物图", "服装图", "场景图", "构图图", "产品图"]
REFERENCE_VISIBILITY_HINTS = ["可识别", "清晰", "不清晰", "模糊", "遮挡", "过曝", "过暗", "补写", "重建", "参考图可识别性", "清晰部分", "不清晰部分", "上传后自检", "重新生成参考图", "主职责", "弱参考", "降级"]
FACE_INTEGRITY_TRIGGER_HINTS = ["脸", "人脸", "面部", "五官", "皮肤", "锁脸", "近景", "特写", "修脸", "脸畸形", "黑斑", "色块", "阴影怪", "大面积黑色", "塑料皮肤", "蜡像", "肤色断层"]
FACE_INTEGRITY_HINTS = ["生理", "五官比例", "结构自然", "肤色连续", "皮肤色调", "自然面部", "主光源", "阴影逻辑", "眼神光", "暗部保留", "黑斑", "异常阴影", "色块", "死黑", "塑料", "蜡像"]
REFERENCE_REGEN_TRIGGER_HINTS = ["不清晰位置较多", "多处不清晰", "五官不可辨", "主职责不可辨", "服装不可辨", "背景死黑", "大面积模糊", "低清", "压缩噪点", "首尾帧无法连接"]
REFERENCE_REGEN_HINTS = ["重新生成参考图", "重新上传", "更清晰", "弱参考", "降低职责", "补写", "重建", "不承担强职责", "建议用户"]


def contains_any(text: str, hints: list[str]) -> bool:
    return any(h in text for h in hints)


def check_prompt(text: str) -> tuple[list[str], list[str]]:
    missing: list[str] = []
    warnings: list[str] = []

    for marker in DEPRECATED_MARKERS:
        if marker in text:
            warnings.append(f"检测到已废弃输出模板：{marker}")

    for label, hints in SECTION_HINTS.items():
        if not contains_any(text, hints):
            missing.append(label)

    if "【负面提示词】" in text:
        neg = text.split("【负面提示词】", 1)[1]
        for cats in NEGATIVE_CATEGORIES:
            if not any(cat in neg for cat in cats):
                warnings.append(f"负面提示词缺少分类：{'/'.join(cats)}")
        if ("动力学类" in neg or "风力类" in neg) and not contains_any(neg, ["风向", "发丝", "布料", "纱幔", "云层", "同速", "重量", "接触", "碰撞", "消散", "落点", "漂浮"]):
            warnings.append("动力学类负面提示词较弱，建议加入风向混乱、发丝不动、布料无重量、同速漂浮、道具漂浮、粒子无落点、烟雾无消散等故障词。")

    main = text.split("【负面提示词】", 1)[0]
    if sum(main.count(w) for w in FAILURE_WORDS_IN_MAIN) > 2:
        warnings.append("正文提示词含较多负面/故障措辞，建议移入负面提示词。")

    has_person = contains_any(main, PERSON_HINTS)
    if has_person:
        if not contains_any(main, ACTION_HINTS):
            warnings.append("检测到人物主体，但缺少人物核心动作。")
        if not contains_any(main, EXPRESSION_HINTS):
            warnings.append("检测到人物主体，但缺少表情与肢体联动。")
        if contains_any(main, MOUTH_TRIGGER_HINTS) and not contains_any(main, MOUTH_DETAIL_HINTS):
            warnings.append("检测到说话/唱歌/对口型，但缺少下颌稳定、嘴唇开合、呼吸节奏等口型细节。")
        if contains_any(main, CLOSEUP_HINTS) and not contains_any(main, FACE_LIGHT_HINTS):
            warnings.append("检测到人物中近景/近景/特写，但缺少鼻梁、眼窝、颧骨、下颌、眼神光等人物面部光影。")

    if contains_any(text, SEQUENCE_TRIGGER_HINTS) and not contains_any(text, SEQUENCE_STATE_HINTS):
        warnings.append("检测到连续片段/首尾帧/下一段任务，但缺少连续片段状态胶囊或当前段状态约束。")

    if contains_any(text, MULTI_REF_HINTS) and not contains_any(text, REFERENCE_CONTRACT_HINTS):
        warnings.append("检测到多参考图/锁脸换装任务，但缺少参考图职责转移契约。")

    if contains_any(text, RETAKE_HINTS) and not contains_any(text, RETAKE_DIAG_HINTS):
        warnings.append("检测到修复/重拍/复盘任务，但缺少失败归因或修复策略。")


    if contains_any(text, DIRECTOR_TRIGGER_HINTS) and not contains_any(text, DIRECTOR_INTENT_HINTS):
        warnings.append("检测到电影感/剧情/情绪/分镜需求，但缺少单一镜头意图或导演一致性锚点。")

    if contains_any(main, ACTION_HINTS) and not contains_any(main, MOTION_CONTRACT_HINTS):
        warnings.append("检测到关键动作，但缺少动作落点、物理结果、力量/节奏或结束状态。")

    if contains_any(text, MULTI_CHARACTER_HINTS) and not contains_any(text, BLOCKING_HINTS):
        warnings.append("检测到多人/群像/舞台/对话任务，但缺少多人动作层级、站位或主次调度。")

    if contains_any(text, LIGHTING_CONTRACT_HINTS) and not contains_any(text, ["方向", "来自", "色温", "阴影", "反射", "光质"]):
        warnings.append("检测到光影需求，但缺少有动机的光源方向、色温、阴影或材质反射。")

    if contains_any(text, PRO_SHOT_HINTS) and not contains_any(text, PRO_SHOT_CONTRACT_HINTS):
        warnings.append("检测到专业分镜/广告/MV镜头需求，但缺少镜头合约、连续锚点或起止状态。")

    if contains_any(text, ITERATION_HINTS) and not contains_any(text, ITERATION_CONTROL_HINTS):
        warnings.append("检测到重拍迭代需求，但缺少保留/后期修/局部编辑/换种子/改写提示词等单变量策略。")


    if contains_any(text, SLOP_HINTS) and not contains_any(text, CONCRETE_REWRITE_HINTS):
        warnings.append("检测到空泛词/图像模型词，但缺少可见的镜头、光影、动作、材质、动力学或声音替换。")

    if contains_any(text, BUDGET_TRIGGER_HINTS) and not contains_any(text, BUDGET_HINTS):
        warnings.append("检测到复杂任务/多元素/锁脸与大动作冲突风险，但缺少提示词预算分配或拆分策略。")

    action_count = sum(main.count(w) for w in ["然后", "接着", "再", "随后", "最后", "同时"])
    if action_count >= 3 and not contains_any(text, DENSITY_HINTS):
        warnings.append("检测到多个连续动作/事件，建议使用事件密度控制：当前clip只保留一个核心事件和一个改变后的终点。")

    if contains_any(text, MODEL_MECHANICS_HINTS) and not contains_any(text, ["注意力", "否定", "参考图", "细节面积", "预算", "正向替代"]):
        warnings.append("检测到模型机制/失败原因讨论，但缺少注意力预算、否定召唤、参考图冲突或细节容量等诊断维度。")

    if contains_any(text, MODE_TRIGGER_HINTS) and not contains_any(text, MODE_STANDARD_HINTS):
        warnings.append("检测到图生视频/首尾帧/图片/压缩等模式需求，但缺少模式优先判断、长度档位或 I2V 极简原则。")

    if contains_any(text, REFERENCE_VISIBILITY_TRIGGER_HINTS) and not contains_any(text, REFERENCE_VISIBILITY_HINTS):
        warnings.append("检测到参考图/图生视频/首尾帧/锁脸任务，但缺少参考图可识别性检查：需判断人脸、服装、发型、背景、构图是否清晰；不清晰部分必须补写。")

    if "只写图片看不出来" in text and not contains_any(text, ["清晰", "可识别", "不清晰", "补写", "重建"]):
        warnings.append("检测到 I2V 极简原则，但缺少前置条件：只有参考图关键视觉信息清晰时才能省略；不清晰或异常部分必须补写/重建。")

    if contains_any(text, REFERENCE_REGEN_TRIGGER_HINTS) and not contains_any(text, REFERENCE_REGEN_HINTS):
        warnings.append("检测到参考图多处不清晰/主职责不可辨风险，但缺少重新生成参考图、降低参考职责或补写重建策略。")

    if contains_any(text, FACE_INTEGRITY_TRIGGER_HINTS) and not contains_any(text, FACE_INTEGRITY_HINTS):
        warnings.append("检测到人脸/皮肤/锁脸/近景任务，但缺少人脸完整性检查：需约束生理结构、五官比例、肤色连续、面部阴影逻辑，并排除黑斑、异常色块、大面积死黑、塑料/蜡像皮肤。")

    if contains_any(main, WIND_OBJECT_HINTS):
        if not contains_any(main, WIND_PHYSICS_HINTS):
            warnings.append("检测到动态材质/流体/粒子/道具运动，但缺少动力来源、运动路径、重量/惯性/接触反应/回弹/速度差/消散等物理动力学锚点。")
        if "风向" in main and "统一" not in main:
            warnings.append("检测到风向描述，但未明确风向全程统一。")

    shots = SHOT_RE.findall(text)
    if shots:
        for shot in shots:
            idx = text.find(shot)
            window = text[idx: idx + 380]
            if not contains_any(window, CAMERA_HINTS):
                warnings.append(f"{shot} 附近缺少机位/运镜信息。")
            if contains_any(window, PERSON_HINTS):
                if not contains_any(window, ACTION_HINTS):
                    warnings.append(f"{shot} 附近有人物但缺少人物动作。")
                if not contains_any(window, EXPRESSION_HINTS):
                    warnings.append(f"{shot} 附近有人物但缺少表情/肢体联动。")
            elif not contains_any(window, ACTION_HINTS):
                warnings.append(f"{shot} 附近缺少主体动作/肢体信息。")
            if not contains_any(window, ENV_HINTS):
                warnings.append(f"{shot} 附近缺少光影/风/环境信息。")
    elif "镜头" in text:
        warnings.append("检测到镜头描述，但没有识别到明确秒数段落。")

    main_len = len(main.strip())
    if main_len < 500:
        warnings.append("正文偏短，复杂视频可能缺少控制锚点。")
    if main_len > 2600:
        warnings.append("正文偏长，建议压缩重复说明，保留强锚点和镜头化时间轴。")

    return missing, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a Prompt Script Master video prompt text file.")
    parser.add_argument("file", help="Path to prompt text file")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    missing, warnings = check_prompt(text)

    print("提示词检查结果")
    print("=" * 20)
    if not missing and not warnings:
        print("通过：符合当前中等精简 + 强锚点 + 镜头化时间轴 + 人物镜头强制覆盖 + 物理动力学 + V0.9.82 参考图上传后自检 + V0.9.80 模式优先 + 长度档位 + I2V极简 + 镜头语言 + 景别运镜适配 + 模型机制 + 预算分配 + 事件密度 + 反空泛词融合标准。")
        return
    print("需要优化")
    if missing:
        print("\n缺少关键模块：")
        for item in missing:
            print(f"- {item}")
    if warnings:
        print("\n提醒：")
        for item in warnings:
            print(f"- {item}")


if __name__ == "__main__":
    main()
