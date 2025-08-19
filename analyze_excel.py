import pandas as pd

print('=== 新旧预定表格式对比分析 ===')

# 分析新的8月预定表
print('\n🆕 新格式分析 (8月预定.xls):')
df_new = pd.read_excel('8月预定.xls')
print(f'数据形状: {df_new.shape}')
print('表头信息:', df_new.iloc[0].tolist())

# 新格式的列结构
print('\n新格式列结构:')
print('列0: 包厢名称/桌台号 (如: 福禄, 喜乐, 大厅1等)')
print('列1: 时段 (午市/晚市)')
print('列2: 时间 (如: 12:00:00, 18:00:00)')
print('列3: 客户类型/姓名 (如: 贵宾, 林总等)')
print('列4: 人数')
print('列5: 联系电话')
print('列6: 预订人')
print('列7: 经手人')
print('列8: 备注')

# 显示有数据的示例行
print('\n新格式数据示例:')
for i in range(min(10, len(df_new))):
    row = df_new.iloc[i]
    if pd.notna(row.iloc[0]) and row.iloc[0] not in ['包厅', '晚市']:
        # 只显示非空字段
        non_empty = [f'{j}:{v}' for j, v in enumerate(row) if pd.notna(v)]
        if len(non_empty) > 3:  # 至少有包厢、时段、时间
            print(f'  行{i}: {non_empty}')

print('\n' + '='*60)
print('📋 格式变化总结:')
print('\n🔄 主要变化:')
print('1. 新格式使用固定的9列结构')
print('2. 第0行包含表头信息，但列名不规范（有Unnamed列）')
print('3. 数据从第1行开始')
print('4. 包厢名称更加详细（包含具体包厢名和大厅编号）')
print('5. 时间格式为time对象（如12:00:00）')
print('6. 增加了客户类型字段（贵宾等）')

print('\n⚠️  需要解决的问题:')
print('1. 列名不规范，需要重新定义标准列名')
print('2. 表头行混合了日期信息，需要特殊处理')
print('3. 数据行从第1行开始，而不是第0行')
print('4. 需要适配新的包厢命名规则')

print('\n🛠️  建议的软件调整:')
print('1. 修改Excel读取逻辑，跳过第0行表头')
print('2. 重新定义列名映射关系')
print('3. 更新数据清洗和验证逻辑')
print('4. 适配新的包厢名称匹配规则')
print('5. 处理时间格式的转换')

print('\n📊 新格式标准列名建议:')
suggested_columns = {
    0: '包厢名称',
    1: '时段',
    2: '预订时间',
    3: '客户姓名',
    4: '人数',
    5: '联系电话',
    6: '预订人',
    7: '经手人',
    8: '备注'
}

for col_idx, col_name in suggested_columns.items():
    print(f'  列{col_idx}: {col_name}')

print('\n✅ 处理后的数据预览:')
# 创建处理后的示例
processed_df = df_new.iloc[1:].copy()  # 跳过表头行
processed_df.columns = list(suggested_columns.values())

# 显示处理后的数据
valid_data = processed_df[processed_df['包厢名称'].notna()]
print(f'有效数据行数: {len(valid_data)}')
if not valid_data.empty:
    print('前5行处理后的数据:')
    for i, (idx, row) in enumerate(valid_data.head().iterrows()):
        print(f'  {i+1}. 包厢:{row["包厢名称"]} | 时段:{row["时段"]} | 时间:{row["预订时间"]} | 客户:{row["客户姓名"]} | 人数:{row["人数"]} | 预订人:{row["预订人"]}')