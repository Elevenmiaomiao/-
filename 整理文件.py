import os
import shutil
import logging

# 配置日志，输出到控制台，日志级别设为 INFO
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # 交互式输入源文件夹路径（多个路径以空格分隔）和目标文件夹路径
    sources_input = input("请输入待合并的源文件夹的绝对路径，多个路径以空格分隔:\n").strip()
    if not sources_input:
        logging.error("未输入任何源文件夹路径，程序退出。")
        return
    sources = sources_input.split()
    
    dest = input("请输入合并后目标文件夹的绝对路径:\n").strip()
    if not dest:
        logging.error("未输入目标文件夹路径，程序退出。")
        return

    # 创建目标目录（如果不存在）
    os.makedirs(dest, exist_ok=True)
    logging.info(f"已创建目标目录: {dest}")

    # 构建一个字典，记录每个相对目录下各文件在各源中的信息
    # 格式：merged_dict[rel_path][filename] = [(source_index, full_path, source_dir), ...]
    merged_dict = {}

    for idx, src in enumerate(sources):
        if not os.path.isdir(src):
            logging.error(f"目录 {src} 不存在，跳过。")
            continue
        logging.info(f"扫描源目录 {src} ...")
        for root, dirs, files in os.walk(src):
            rel_path = os.path.relpath(root, src)
            if rel_path == ".":
                rel_path = ""
            if rel_path not in merged_dict:
                merged_dict[rel_path] = {}
            for file in files:
                full_path = os.path.join(root, file)
                merged_dict[rel_path].setdefault(file, []).append((idx, full_path, src))
        logging.info(f"扫描目录 {src} 完毕。")
    
    logging.info(f"待处理相对目录总数：{len(merged_dict)}")

    # 遍历所有相对目录进行文件复制
    for rel_path, file_dict in merged_dict.items():
        dest_dir = os.path.join(dest, rel_path)
        os.makedirs(dest_dir, exist_ok=True)
        logging.info(f"处理目录: {dest_dir}")

        for file, entries in file_dict.items():
            # 若只有一个来源，则直接复制
            if len(entries) == 1:
                src_file = entries[0][1]
                dst_file = os.path.join(dest_dir, file)
                try:
                    shutil.copy2(src_file, dst_file)
                    logging.info(f"复制文件: {src_file} -> {dst_file}")
                except Exception as e:
                    logging.error(f"复制文件 {src_file} 时出错: {e}")
            else:
                # 多个来源：按照输入顺序，后面的源优先
                sorted_entries = sorted(entries, key=lambda x: x[0])
                # 取优先级最高的文件（即来源序号最大的）
                primary = sorted_entries[-1]
                src_file_primary = primary[1]
                dst_file = os.path.join(dest_dir, file)
                try:
                    shutil.copy2(src_file_primary, dst_file)
                    logging.info(f"覆盖复制（优先）文件: {src_file_primary} -> {dst_file}")
                except Exception as e:
                    logging.error(f"复制文件 {src_file_primary} 时出错: {e}")
                # 其他来源的文件复制到 duplication 子目录中
                dup_dir = os.path.join(dest_dir, "duplication")
                os.makedirs(dup_dir, exist_ok=True)
                for entry in sorted_entries[:-1]:
                    src_file_dup = entry[1]
                    dst_dup_file = os.path.join(dup_dir, file)
                    try:
                        shutil.copy2(src_file_dup, dst_dup_file)
                        logging.info(f"将重复文件复制到 duplication: {src_file_dup} -> {dst_dup_file}")
                    except Exception as e:
                        logging.error(f"复制重复文件 {src_file_dup} 时出错: {e}")

    logging.info("所有文件合并操作已完成！")

if __name__ == "__main__":
    main()
