# 📘 生命禅院百科馆

# Slug 命名规则总表 v1.0

---

## 一、什么是 slug？

Slug 是：

* 文件名
* 页面路径
* URL 显示部分
* GitHub 目录名

例如：

```
civilization-3-0.md
```

网站路径即：

```
/zh/civilization-3-0
```

---

## 二、核心规则（必须遵守）

### 1️⃣ 全部小写

```
✔ civilization-3-0
✘ Civilization-3-0
✘ CIVILIZATION-3-0
```

---

### 2️⃣ 使用 `-` 连接单词

```
✔ second-home-model
✔ ai-chanyuan-celestials
✘ second_home_model
✘ second home model
```

---

### 3️⃣ 不使用中文文件名

```
✘ 文明3.0.md
✘ 第二家园.md
```

统一使用英文 slug。

---

### 4️⃣ 数字使用阿拉伯数字

```
✔ civilization-3-0
✔ human-800-concepts
✘ civilization-three
✘ eight-hundred-concepts
```

---

### 5️⃣ 不包含特殊符号

禁止使用：

```
.
,
&
?
!
:
;
()
```

---

### 6️⃣ 长度控制

建议不超过 40 个字符。

过长示例（不推荐）：

```
future-human-civilization-spiritual-evolution-system
```

---

## 三、标准命名结构

### 结构公式

```
核心概念 + 修饰词
```

例如：

| 中文        | slug                           |
| --------- | ------------------------------ |
| 文明3.0     | civilization-3-0               |
| 第二家园模式    | second-home-model              |
| 第二家园程序    | second-home-program            |
| 新时代人类八百理念 | new-era-human-800-concepts     |
| 浑沌管理      | hundun-management              |
| 心灵净化      | spiritual-purification         |
| AI禅院草     | ai-chanyuan-celestials         |
| AI禅院草联盟   | ai-chanyuan-celestial-alliance |

---

## 四、复数与单数规则

### 1️⃣ 概念类 → 单数

```
second-home-model
hundun-management
spiritual-purification
```

---

### 2️⃣ 群体类 → 复数

```
ai-chanyuan-celestials
ai-chanyuan-celestial-alliance
```

---

## 五、英文翻译来源规则

slug 必须基于：

* 官方英译标准
* 已确定的术语
* 固定英文译名

不得自行临时翻译。

---

## 六、中英文统一规则

zh 和 en 使用 **同一个 slug**

例如：

```
zh/civilization-3-0.md
en/civilization-3-0.md
```

不得出现：

```
zh/wenming-3-0.md
en/civilization-3-0.md
```

---

## 七、未来扩展预留规则

如需添加分类路径，可使用：

```
theory/
practice/
history/
people/
```

但当前版本 v1.0 不启用二级分类。

---

## 八、常见错误示例

| 错误               | 原因    |
| ---------------- | ----- |
| Civilization3.0  | 缺少连接符 |
| civilization_3_0 | 使用下划线 |
| secondHomeModel  | 驼峰式命名 |
| 文明3-0            | 中文文件名 |

---

## 九、slug 确定流程

创建新词条前必须：

1. 确认官方英文译名
2. 转换为小写
3. 用 `-` 连接
4. 检查是否已存在
5. 记录到词条总表

---

# ✅ 当前版本：v1.0

# 适用范围：生命禅院百科馆

---
