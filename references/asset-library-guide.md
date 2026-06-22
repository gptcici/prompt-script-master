# 素材库与本地上传指南

本文件用于管理之后用户手动放入项目的图片、视频、截图和辅助资料。所有素材只作为内部参考，不得在最终生成内容中泄露来源。

## 推荐目录

```text
assets/
  reference-images/
    concert-case-a/
      README.md
      image-001.webp
      image-002.webp
  reference-videos/
    concert-case-a/
      README.md
      video-proxy.mp4
      keyframes/
  source-breakdowns/
    README.md
```

## 图片资料建议

图片可用于：

- 人物造型连续性参考。
- 舞台构图参考。
- 镜头景别与机位参考。
- 灯光氛围参考。
- 服装材质和妆造参考。

处理建议：

- 使用 `.webp` 或压缩 `.jpg`。
- 单张图建议控制在 300KB 以内。
- 命名使用中性名称，例如 `image-001.webp`，不要把艺人名、视频名、品牌名写入文件名。
- 每组图片配一个 `README.md`，只写抽象用途，不写可识别来源。

## 视频资料建议

完整视频通常不适合直接塞进 Skill 包，除非已经压缩到很小。

优先方案：

1. 保留低码率 proxy 视频，用于本地查看。
2. 抽取关键帧放入 `keyframes/`。
3. 写一份 `video-index.md`，记录抽象的段落用途，例如开场、主歌、高潮、收尾。
4. 不要在最终脚本中输出原视频名、时间戳、人物名或可识别桥段。

## 大小限制

Skill ZIP 最好小于 25MB。若视频或图片导致超过限制：

- 优先保留文字索引和关键帧。
- 压缩图片最长边到 1280-1600px。
- 将视频替换为关键帧 + shot index。
- 必要时把大型原视频放在 GitHub 外部，仅在 README 记录“本地素材未打包”。

## 本地同步步骤

用户在本地仓库放入素材后：

```powershell
git add .
git commit -m "feat: add script reference media assets"
git push origin main
```

推送前检查：

```powershell
(Get-ChildItem .\assets\reference-images -Recurse -File).Count
(Get-ChildItem .\assets\reference-videos -Recurse -File).Count
git status
```
