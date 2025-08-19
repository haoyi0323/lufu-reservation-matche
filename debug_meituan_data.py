import pandas as pd
import streamlit as st
from datetime import datetime

def debug_meituan_data():
    """调试美团数据的日期范围"""
    print("=== 美团数据调试工具 ===")
    
    # 检查session state中是否有美团数据
    if 'meituan_file' in st.session_state:
        meituan_df = st.session_state['meituan_file']
        print(f"找到美团数据，共 {len(meituan_df)} 行")
        
        # 显示列名
        print("\n列名:")
        for i, col in enumerate(meituan_df.columns):
            print(f"{i+1}. {col}")
        
        # 检查下单时间列
        if '下单时间' in meituan_df.columns:
            print("\n=== 下单时间分析 ===")
            
            # 显示原始数据样本
            print("\n原始下单时间样本（前10行）:")
            for i, time_val in enumerate(meituan_df['下单时间'].head(10)):
                print(f"{i+1}. {time_val} (类型: {type(time_val)})")
            
            # 转换为datetime并分析
            try:
                meituan_dates = pd.to_datetime(meituan_df['下单时间'], errors='coerce')
                valid_dates = meituan_dates.dropna()
                
                if len(valid_dates) > 0:
                    print(f"\n有效日期数量: {len(valid_dates)}")
                    print(f"最早日期: {valid_dates.min()}")
                    print(f"最晚日期: {valid_dates.max()}")
                    
                    # 按日期统计
                    date_counts = valid_dates.dt.date.value_counts().sort_index()
                    print("\n按日期统计订单数量:")
                    for date, count in date_counts.items():
                        print(f"{date}: {count} 个订单")
                else:
                    print("没有找到有效的日期数据")
                    
            except Exception as e:
                print(f"日期转换错误: {e}")
        else:
            print("未找到'下单时间'列")
        
        # 检查订单状态过滤
        if '订单状态' in meituan_df.columns:
            print("\n=== 订单状态分析 ===")
            status_counts = meituan_df['订单状态'].value_counts()
            print("订单状态统计:")
            for status, count in status_counts.items():
                print(f"{status}: {count} 个")
            
            # 过滤后的数据
            filtered_df = meituan_df[meituan_df['订单状态'] == '已结账']
            print(f"\n过滤后（已结账）: {len(filtered_df)} 行")
            
            if len(filtered_df) > 0 and '下单时间' in filtered_df.columns:
                try:
                    filtered_dates = pd.to_datetime(filtered_df['下单时间'], errors='coerce')
                    valid_filtered_dates = filtered_dates.dropna()
                    
                    if len(valid_filtered_dates) > 0:
                        date_counts = valid_filtered_dates.dt.date.value_counts().sort_index()
                        print("\n过滤后按日期统计:")
                        for date, count in date_counts.items():
                            print(f"{date}: {count} 个订单")
                except Exception as e:
                    print(f"过滤后日期分析错误: {e}")
        
        # 检查营业日期过滤
        if '营业日期' in meituan_df.columns:
            print("\n=== 营业日期分析 ===")
            business_date_counts = meituan_df['营业日期'].value_counts()
            print("营业日期统计（前10个）:")
            for date, count in business_date_counts.head(10).items():
                print(f"{date}: {count} 个")
            
            # 检查'--'值
            dash_count = (meituan_df['营业日期'] == '--').sum()
            print(f"\n营业日期为'--'的记录数: {dash_count}")
            
    else:
        print("未找到美团数据，请先上传文件")

if __name__ == "__main__":
    debug_meituan_data()