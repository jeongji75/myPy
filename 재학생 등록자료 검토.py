# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:31:13 2023

@author: land
"""

import pandas as pd
import numpy as np
import glob
import os


# 파일 경로 및 확장자 지정 .xlsx 와 .csv에 따라 진행
""" file_format = ".xlsx" # .csv
file_path = "D:\C-myPyExcel\재학생 등록자료 검토" # 경로 입력
file_list = glob.glob(f"{file_path}/*{file_format}")
print(file_list) """

# 현재 디렉토리 가져오기
file_path = os.getcwd()
print(file_path+"\n")
print(file_path+"\재학생 등록자료 검토\\230203_(자료) 종합정보 기납대상자 생성 결과 723명.xlsx")

# 합병 결과를 담는 DataFrame 생성
merge_df_기납휴학비교 = pd.DataFrame()

# 기납자 파일 읽어오기
df_기납 = pd.read_excel(
                        file_path+"\재학생 등록자료 검토\\230203_(자료) 종합정보 기납대상자 생성 결과 723명.xlsx",
                        sheet_name="Sheet"
                        )

# 등록구분에 nan 값이 존재할 경우 "미등록"로 표시
df_기납["등록구분"] = df_기납["등록구분"].fillna("미등록")

print(df_기납.info())