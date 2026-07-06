
# Professional Shot Continuity Contract 专业镜头连续合约

## 目的

本规则用于更专业的分镜、广告、MV、系列短剧和多镜头项目。它把每个镜头当成一个“镜头合约”：镜头目的、动作、机位、参考图职责、连续性、风险、起点和终点必须清楚。

## 启动条件

出现以下任一情况时读取本规则：

```text
分镜、故事板、多镜头、广告片、产品片、MV、连续剧情、镜头清单、shot list、treatment、专业拍摄、客户提案、商业片、同一角色多镜头、多段视频、首尾帧衔接
```

## 镜头合约字段

复杂项目内部可建立以下字段。最终提示词不必表格化输出，除非用户要求。

```text
镜头编号：S01 / SH01 等。
时长：该镜头持续几秒。
镜头目的：建立、揭示、证明材质、情绪转折、动作落点、结尾钩子。
主体动作：谁做什么，动作终点是什么。
景别机位：远景 / 中景 / 近景 / 特写，平视 / 仰视 / 俯视等。
运镜焦点：推、拉、横移、环绕、跟拍、锁定、拉焦。
参考图职责：每张图控制什么，不控制什么。
连续锚点：人物、服装、道具、场景、光源、风向、屏幕方向、眼线。
起始状态：镜头开始时人物和环境状态。
结束状态：镜头结束时给下一个镜头的交接状态。
风险：脸漂、手崩、Logo、动作复杂、光影跳变、风向乱、首尾不接。
```

## 连续性账本

跨镜头必须追踪：

```text
角色：脸、发型、服装、妆容、情绪。
道具：谁拿着、在哪里、状态是否改变。
场景：门窗位置、亭子方向、空间左右关系。
屏幕方向：人物移动方向、视线方向、镜头轴线。
光线：主光方向、色温、是否有灯光阶段变化。
动力学：风向、雨线、水面、烟雾、粒子、道具状态、接触点、柔体响应是否持续。
动作状态：上一镜头动作是否完成，当前镜头从哪里接。
声音 / 音乐：节拍、歌词、环境声、对口型阶段。
```

## 镜头切分原则

1. 一个 Seedance 片段优先承担一个核心节拍。
2. 脸、产品、手、复杂动作、文字、Logo、首尾帧等脆弱锚点越多，镜头越要简化。
3. 如果同一镜头需要“走位 + 对口型 + 拿道具 + 镜头环绕 + 风动 + 光变”，应拆成两个镜头。
4. 三次重拍仍失败，应简化镜头合约或拆分动作，而不是继续堆词。
5. 当前镜头只写当前镜头，不写未来镜头结果。

## 首尾帧 / 下一段交接

当用户给首帧 / 尾帧，或要求下一段继续：

- 首帧锁定起始状态。
- 尾帧锁定结束状态。
- 中间过程必须解释从起点到终点的动作、光影、物理动力学和情绪变化。
- 下一段必须继承上一段已接受的结束状态，而不是只继承原计划。

## 与 V0.9.75 的关系

本规则是 `sequence-state-capsule.md` 的镜头级扩展：

- sequence-state-capsule 管项目 / 片段状态。
- 本规则管单个镜头 / 多镜头合约。
- reference-transfer-contract 管参考图职责。
- motion-performance-contract 管动作怎么写。
- lighting-intention-contract 管光影怎么写。

## 负面提示词建议

```text
连续性类：镜头轴线跳变、眼线不一致、人物位置跳变、道具状态冲突、屏幕方向翻转、首尾帧无法衔接、上一镜头动作重演、未来镜头事件提前出现
```


## V0.9.79 shot-language integration

Professional shot contracts must include content-fit checks: shot size, movement, focus, start frame, end frame, and risk. If the shot is meant to protect face, mouth, hands, text, product structure, or first/last-frame precision, reduce camera freedom. If the shot is meant to reveal geography or scale, do not ask for detailed face performance in the same shot.

Continuity checks must include screen direction, eyeline, entry/exit side, light direction, physical dynamics direction, prop position, and whether the previous end frame naturally becomes the next start frame.
