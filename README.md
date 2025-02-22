# -
icloud 文稿桌面同步出错时可用！本脚本主要用于将多个文件夹（各自作为一个根目录）中相同相对路径下的文件合并到一个目标文件夹中。

文件合并脚本使用说明
适用范围
本脚本主要用于将多个文件夹（各自作为一个根目录）中相同相对路径下的文件合并到一个目标文件夹中。适用场景包括：

iCloud 备份异常：文件因上传中断而被拆分到不同文件夹中时，可借助该脚本恢复原始目录结构和文件完整性。
文件整合：多个来源文件夹存在重复或分散存储的文件时，可快速合并整理，防止文件覆盖。
数据备份与恢复：在进行数据迁移、备份或恢复过程中，将分散的文件合并成统一目录。
该脚本可在 macOS 与 Windows 系统中运行（注意：Windows 用户需要将路径格式调整为 Windows 形式，如 C:\Users\用户名\Downloads\A 等）。

# 文件合并脚本使用说明

本说明文档提供了最简化的操作步骤，帮助您快速使用脚本完成文件合并任务。即使您没有 Python 使用经验，也能按照以下步骤操作。

---

## 操作步骤

### 1. 下载文件

- 下载并保存脚本文件 **“整理文件.py”** 到一个文件夹中（例如：Downloads 文件夹）。

### 2. 将“整理文件.py”和要合并的文件夹放在同一目录下


### 3. 安装 Python3

- **macOS 用户：**
1. 打开 **终端**。
2. 如果未安装 Python3，可输入以下命令（需要安装 Homebrew，若已安装可跳过）：
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python3
   ```
3. 验证安装：
   ```bash
   python3 --version
   ```

- **Windows 用户：**
1. 打开 **命令提示符** 或 **Windows Terminal**。
2. 如果未安装 Python3，可输入以下命令（需要使用 Windows Package Manager Winget）：
   ```cmd
   winget install Python.Python.3
   ```
   或者访问 [Python 官网](https://www.python.org/downloads/windows/)下载安装，并确保勾选 “Add Python 3.x to PATH” 选项。
3. 验证安装：
   ```cmd
   python --version
   ```

### 4. 运行脚本

1. 打开终端（macOS）或命令提示符（Windows）。
2. 切换到脚本所在目录（例如 Downloads 文件夹）：
 - **macOS：**
   ```bash
   cd ~/Downloads
   ```
 - **Windows：**
   ```cmd
   cd C:\Users\YourName\Downloads
   ```
3. 运行脚本：
 - **macOS：**
   ```bash
   python3 整理文件.py
   ```
 - **Windows：**
   ```cmd
   python 整理文件.py
   ```
   或者：
   ```cmd
   py 整理文件.py
   ```

### 5. 按照提示操作

- 脚本运行后，会提示您输入待合并的源文件夹路径和目标文件夹路径（请使用绝对路径）。
- 按照提示输入后，脚本将自动完成文件合并工作。

---

## 注意事项

- 请确保所有路径均为**绝对路径**,可以尝试将文件夹拖到终端或 cmd 中完成路径的输入；
- 如果遇到问题，请先检查 Python3 是否正确安装并配置到 PATH 中；
- 脚本将合并相同相对路径下的文件，重复文件会存入目标目录下的 `duplication` 文件夹中；

按照以上步骤操作，您就可以轻松完成文件合并任务！
  
