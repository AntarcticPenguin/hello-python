import json
import os

# 推荐：使用 os.path 动态构建文件的完整路径，更加健壮
# 这样即使你的脚本在其他地方运行，也能正确找到文件
file_path = os.path.join(os.path.dirname(__file__), 'data.json')

# ---------- 写入 JSON 文件 ----------
# 1. 准备要保存的 Python 数据（通常是字典或列表）
data_to_save = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "数据分析"]
}

# 2. 写入文件
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data_to_save, f, ensure_ascii=False, indent=2)
print(f"成功写入 JSON 文件: {file_path}")

# ---------- 读取 JSON 文件 ----------
# 3. 从文件读取数据
with open(file_path, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

# 4. 验证数据
print("成功读取 JSON 文件，内容如下：")
print(f"姓名: {loaded_data['name']}")
print(f"年龄: {loaded_data['age']}")
print(f"技能: {loaded_data['skills']}")

# ---------- （可选）异常处理：读取不存在的文件 ----------
try:
    with open('not_exist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("错误：文件未找到，请检查路径！")
except json.JSONDecodeError:
    print("错误：文件不是合法的 JSON 格式！")