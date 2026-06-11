# Obsidian MCP 集成备忘

## 需求
在项目中添加 Obsidian MCP 集成，让 Claude、Codex、Cursor 等 AI 工具能通过 REST API 读写 Obsidian 笔记。

## 前置条件
- Obsidian 已安装 **Local REST API** 插件（社区插件）
- 插件已启用，API Key 已复制
- Obsidian 正在运行

## 配置文件

### 项目级 `.mcp.json`
放在任意 Claude Code 项目的根目录，仅该项目生效：

```json
{
  "mcpServers": {
    "obsidian": {
      "type": "http",
      "url": "https://127.0.0.1:27124/mcp/",
      "headers": {
        "Authorization": "Bearer 8dbd6223be12d9d32817297dec8b7152705f0f061cb77b69ab843f9897b4f3f1"
      }
    }
  }
}
```

### 用户级配置
放在 `~/.claude/.mcp.json`（全局生效，所有项目可用）。

## 生效方式
保存 `.mcp.json` 后，Claude Code 会自动检测到并提示你批准 MCP 服务器连接。批准后即可使用。

## 验证是否成功
重启 Claude Code 后，在对话中问：

> "搜索我的 Obsidian 中关于 SaaS 定价的笔记"

如果 Claude 能返回结果，说明 MCP 连接成功。

## 相关链接
- [Local REST API 插件文档](https://github.com/coddingtonbear/obsidian-local-rest-api)
- [Claude Code MCP 文档](https://docs.anthropic.com/en/docs/claude-code/mcp)
