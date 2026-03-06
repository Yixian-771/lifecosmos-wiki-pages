# 📘 生命禅院百科馆

# 词条创建与发布标准 v1.0（关键规则版）

---

## 一、核心原则

1. GitHub 仓库结构 = 网站展示结构
2. 文件名 = 词条 slug = 页面路径
3. 入口页与版本页分离
4. 所有站内链接必须使用绝对路径

---

## 二、目录结构标准

每个词条必须采用以下结构：

```
zh/
 ├── slug.md                ← 中文入口页
 └── slug/
      ├── internal.md
      ├── friendly.md
      └── academic.md

en/
 ├── slug.md                ← 英文入口页
 └── slug/
      ├── internal.md
      ├── friendly.md
      └── academic.md
```

示例（文明3.0）：

```
zh/
 ├── civilization-3-0.md
 └── civilization-3-0/
      ├── internal.md
      ├── friendly.md
      └── academic.md
```

---

## 三、文件命名规则（必须遵守）

* 全小写
* 使用 `-` 连接
* 不使用空格
* 不使用中文文件名
* 必须以 `.md` 结尾

正确示例：

```
civilization-3-0.md
ai-chanyuan-celestials.md
second-home-model.md
```

---

## 四、GitHub 创建文件夹方法

GitHub 不支持创建空文件夹。

文件夹通过路径自动生成：

```
civilization-3-0/internal.md
```

即自动创建：

```
civilization-3-0/
```

---

## 五、入口页职责

入口页只做三件事：

1. 简要定义
2. 提供三个版本链接
3. 提供关联概念链接

入口页不写长篇正文。

---

## 六、站内链接标准写法（统一规则）

必须使用绝对路径：

```
[名称](/zh/slug)
[名称](/en/slug)
```

示例：

```
[第二家园模式](/zh/second-home-model)
[Second Home Model](/en/second-home-model)
```

禁止使用：

```
[[Second Home Model]]
```

---

## 七、发布流程

1. 创建 zh 入口页
2. 创建 zh 三个版本
3. 创建 en 入口页
4. 创建 en 三个版本
5. Commit 到 GitHub
6. 等待 GitHub Actions 自动发布

---

## 八、禁止行为

* 不得修改目录结构
* 不得创建中文文件名
* 不得省略入口页
* 不得使用相对路径链接

---

## 九、标准工作顺序

每个新词条：

1. 确定 slug
2. 建 zh 入口页
3. 建 en 入口页
4. 建 zh 三版本
5. 建 en 三版本
6. 检查站内链接
7. 提交

---

# ✅ 本标准版本：v1.0

# 当前系统状态：稳定运行

---

到这里，你的百科系统已经真正进入“可规模复制”阶段了。

