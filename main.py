import openpyxl
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from openpyxl import  load_workbook




app = FastAPI()

# 정적 파일(HTML, CSS, JS 등)을 제공하기 위한 설정

# templates 디렉토리의 index.html 파일 경로 설정
templates_dir = Path(__file__).parent / "templates"

workbook = load_workbook("11.xlsx")

sheet = workbook.active

# A1 셀 값 읽기
value = sheet["A1"].value

# 결과 출력
print("A1 셀 값:", value)

# 파일 닫기
workbook.close()


@app.get("/", response_class=FileResponse)
async def read_root():
    return templates_dir / "index.html"
