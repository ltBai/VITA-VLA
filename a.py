import os
import subprocess

# 指定主目录（替换成你自己的路径）
root_dir = r"D:\xwechat_files\wxid_1vwo89ep95gz22_c572\msg\file\2025-10\calvin\videos_2025-09-30-07-21-42"

# 遍历所有子目录和文件
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith(".mp4"):
            # 原始路径
            input_path = os.path.join(subdir, file)
            
            # 替换文件名中的空格
            filename_no_space = file.replace(" ", "_")
            
            # 去掉扩展名，添加 "_trans"
            base_name = os.path.splitext(filename_no_space)[0]
            output_name = base_name + "_trans.mp4"
            
            # 输出路径（保持在同一个文件夹下）
            output_path = os.path.join(subdir, output_name)
            
            # ffmpeg 转码命令
            cmd = [
                "ffmpeg", "-i", input_path,
                "-c:v", "libx264", "-crf", "23", "-preset", "fast",
                "-c:a", "aac", "-y", output_path
            ]
            
            print(f"Converting: {input_path} → {output_path}")
            subprocess.run(cmd, check=True)

print("✅ All videos converted successfully!")
