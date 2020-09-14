from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells

from openpyxl.drawing.image import Image
from openpyxl.cell import cell
img = Image('sample_image.jpg')
img.width = 535
img.height = 366
ws.add_image(img, 'c5')
ws.column_dimensions['c'].width = 66.25
ws.column_dimensions['d'].width = 66.25
ws.column_dimensions['b'].width = 1.63
ws.column_dimensions['e'].width = 1.63
ws.column_dimensions['h'].width = 1.63
ws.column_dimensions['g'].width = 22.38
ws.column_dimensions['f'].width = 22.38
ws.row_dimensions[3].height = 13.5
ws.row_dimensions[4].height = 91.5
ws.row_dimensions[5].height = 91.5
ws.row_dimensions[6].height = 91.5
ws.row_dimensions[7].height = 91.5
ws.row_dimensions[8].height = 91.5
ws.row_dimensions[9].height = 91.5
ws.row_dimensions[10].height = 91.5
ws.row_dimensions[11].height = 91.5
ws.row_dimensions[12].height = 91.5
ws.row_dimensions[13].height = 91.5

ws.merge_cells('c4:d4')
ws.merge_cells('f4:g4')

top_left_cell = ws['c4']
top_left_cell.value = '사진'
top_left_cell2 = ws['f4']
top_left_cell2.value = '거래조건'

# ws.row_dimensions

from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
font = Font(name='경기천년제목 Bold', size=24, color='205c98')
alignment=Alignment(horizontal= 'center', vertical='center')

fill = PatternFill(fill_type=None, start_color='205c98', end_color='205c98')
ws['b3:h3'].fill = fill #여기부터 다시시작

ws['c4'].font = Font(name='경기천년제목 Bold', size=36, color='ffffff')
ws['c4'].alignment = alignment

ws['f4'].font = Font(name='경기천년제목 Bold', size=36, color='ffffff')
ws['f4'].alignment = alignment


# Rows can also be appended
ws['f5'] = '층수'
ws['f5'].font = font
ws['f5'].alignment = alignment

ws['f6'] = '룸형태'
ws['f6'].font = font
ws['f6'].alignment = alignment

ws['f7'] = '크기'
ws['f7'].font = font
ws['f7'].alignment = alignment

ws['f8'] = '주방구조'
ws['f8'].font = font
ws['f8'].alignment = alignment

ws['f9'] = '보증금'
ws['f9'].font = font
ws['f9'].alignment = alignment

ws['f10'] = '월세'
ws['f10'].font = font
ws['f10'].alignment = alignment

ws['f11'] = '관리비'
ws['f11'].font = font
ws['f11'].alignment = alignment

ws['f12'] = '보증금조정'
ws['f12'].font = font
ws['f12'].alignment = alignment

ws['f13'] = '입주시기'
ws['f13'].font = font
ws['f13'].alignment = alignment


# Python types will automatically be converted
import datetime
# ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")
