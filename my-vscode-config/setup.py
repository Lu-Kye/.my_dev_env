import os
import shutil
import sys
import platform

def replace_file(src_file_path, dest_file_path):
    try:
        # 尝试替换文件，shutil.copy2用于复制权限和其他元数据
        shutil.copy2(src_file_path, dest_file_path)
        print(f"文件 '{src_file_path}' 已成功替换到 '{dest_file_path}'")
    except IOError as e:
        print(f"无法替换文件: {e}")
        sys.exit(1)

def get_vscode_user_config_path():
        # 根据不同的操作系统找到 VS Code 用户配置文件夹
    system_platform = platform.system()
    if system_platform == "Windows":
        config_path = os.path.join(os.getenv('APPDATA'), 'Code', 'User')
    elif system_platform == "Darwin":  # Mac OS X
        config_path = os.path.join(os.path.expanduser('~'), 'Library',
                                   'Application Support', 'Code', 'User')
    elif system_platform == "Linux":
        config_path = os.path.join(os.path.expanduser('~'), '.config', 'Code', 'User')
    else:
        print(f"不支持的操作系统: {system_platform}")
        sys.exit(1)

    if not os.path.isdir(config_path):
        print(f"VS Code 用户配置路径不存在: {config_path}")
        sys.exit(1)

    return config_path

def confirm_replacement(files_to_confirm):
    print("以下文件将被替换:")
    for file_name in files_to_confirm:
        print(file_name)
    
    # 让用户确认是否继续
    user_confirm = input("是否确定要替换这些文件? 输入 y 或 n: ")
    return user_confirm.lower() == 'y'

if __name__ == "__main__":
    # 确定 VS Code 用户配置路径
    vscode_user_config_path = get_vscode_user_config_path()
    
    # 要替换的文件：keybindings.json 和 settings.json
    # 如果文件不在脚本目录下，请使用正确的路径替换下面的字符串
    files_to_replace = ["keybindings.json", "settings.json"]

    # 确定将要替换的文件
    files_to_confirm = [os.path.join(vscode_user_config_path, file_name)
                        for file_name in files_to_replace]

    # 获取用户确认结果
    if confirm_replacement(files_to_confirm):
        for file_name in files_to_replace:
            src_file_path = os.path.join(os.getcwd(), file_name)
            dest_file_path = os.path.join(vscode_user_config_path, file_name)
            replace_file(src_file_path, dest_file_path)
    else:
        print("操作已取消。")
        sys.exit(0)