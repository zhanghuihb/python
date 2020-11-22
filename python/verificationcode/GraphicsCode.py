import pytesseract
from PIL import Image

image = Image.open('graphics_code.jpg')
# 如果有线条干扰，可能识别不准确
# 可以采用转灰度或者二值化处理,L:转灰度 1:二值化处理
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
image.show()

result = pytesseract.image_to_string(image)
print(result)