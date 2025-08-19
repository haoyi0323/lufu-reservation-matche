import pandas as pd
import numpy as np

print('=== 7月预定表格（老格式）详细分析 ===')
df_old = pd.read_excel('7月预定_20250802_0801.xlsx', sheet_name=None)
print(f'工作表数量: {len(df_old)}')
print(f'工作表名称: {list(df_old.keys())}')

# 分析第一个工作表的结构
first_sheet_name = list(df_old.keys())[0]
first_sheet = df_old[first_sheet_name]
print(f'\n--- 第一个工作表: {first_sheet_name} ---')
print(f'行数: {len(first_sheet)}, 列数: {len(first_sheet.columns)}')
print(f'列名: {list(first_sheet.columns)}')

print('\n前5行数据:')
for i in range(min(5, len(first_sheet))):
    print(f'  行{i}: {first_sheet.iloc[i].tolist()}')

print('\n最后5行数据:')
for i in range(max(0, len(first_sheet)-5), len(first_sheet)):
    print(f'  行{i}: {first_sheet.iloc[i].tolist()}')

print('\n=== 8月预定表格（新格式）详细分析 ===')
df_new = pd.read_excel('8月预定.xls')
print(f'行数: {len(df_new)}, 列数: {len(df_new.columns)}')
print(f'列名: {list(df_new.columns)}')

print('\n表头行（第0行）:')
print(df_new.iloc[0].tolist())

print('\n前5行数据:')
for i in range(min(5, len(df_new))):
    print(f'  行{i}: {df_new.iloc[i].tolist()}')

print('\n最后5行数据:')
for i in range(max(0, len(df_new)-5), len(df_new)):
    print(f'  行{i}: {df_new.iloc[i].tolist()}')

print('\n=== 关键差异对比分析 ===')
print('\n1. 日期信息处理:')
print('   老格式: 日期信息通过工作表名称体现（如01、02、03代表不同日期）')
print('   新格式: 日期信息在表头第二列（8月1号 星期五）')

print('\n2. 总结信息:')
print('   老格式: 无明显总结行')
print('   新格式: 最后一行包含合计信息')
last_row = df_new.iloc[-1].tolist()
print(f'   新格式总结行: {last_row}')

print('\n3. 数据结构:')
print('   老格式: 多工作表，每个工作表代表一天')
print('   新格式: 单工作表，包含多天数据，通过表头区分日期')

print('\n4. 列结构对比:')
print(f'   老格式列名: {list(first_sheet.columns)}')
print(f'   新格式实际列名: {df_new.iloc[0].tolist()}')

print('\n5. 时间格式:')
print('   老格式: 可能使用字符串格式')
print('   新格式: 使用datetime.time对象格式')

# 检查新格式是否有多个日期
print('\n6. 新格式多日期检查:')
date_columns = []
for i, col_val in enumerate(df_new.iloc[0].tolist()):
    if pd.notna(col_val) and ('月' in str(col_val) and '号' in str(col_val)):
        date_columns.append((i, col_val))
print(f'   发现的日期列: {date_columns}')

if len(date_columns) > 1:
    print('   新格式包含多个日期，需要按日期分组处理数据')
else:
    print('   新格式只包含单个日期')