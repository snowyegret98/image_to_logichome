from PIL import Image
import sys
import json
import os


def pix2bin(data):
    try:
        if data[0] < r and data[1] < g and data[2] < b:
            return "1"
        else:
            return "0"
    except Exception as e:
        print("오류! R/G/B값이 잘못된 이미지입니다. 윈도우 캡처 도구를 이용해 다시 캡처해주세요.")
        print(e)
        input("종료하려면 엔터를 누르세요.")
        sys.exit(1)


try:
    confjson = str(sys.argv[0])[:-16] + "config.json"
    with open(confjson) as json_file:
        data = json.load(json_file)
        r = int(data["r"])
        g = int(data["g"])
        b = int(data["b"])
        print(f"r: {r}, g: {g}, b: {b}")
except:
    print("config.json 파일을 찾을 수 없거나, json 형식이 맞지 않습니다.")
    input("종료하려면 엔터를 누르세요.")
    sys.exit(1)

# 인풋 목록
try:
    img_name = sys.argv[1]
except Exception as e:
    print("드래그&드랍으로 열어주세요!")
    print(f"Error: {e}")
    input("종료하려면 엔터를 누르세요.")
    sys.exit(1)
input_width = int(input("가로 칸 갯수를 입력하세요: "))
input_height = int(input("세로 칸 갯수를 입력하세요: "))
try:
    image = Image.open(img_name)
    img_size = image.size
    img_width = img_size[0]
    img_height = img_size[1]

    pixel_width = img_width / input_width
    pixel_w_base = int(pixel_width / 2)
    pixel_height = img_height / input_height
    pixel_h_base = int(pixel_height / 2)

    width_list = [round(i * pixel_width + pixel_w_base) for i in range(input_width)]
    height_list = [round(i * pixel_height + pixel_h_base) for i in range(input_height)]

    output_list = []
    for hei in height_list:
        for wid in width_list:
            output_list.append(pix2bin(image.getpixel((wid, hei))))

    output_line = "".join(output_list)

    with open(img_name[:-3] + "txt", "w", encoding="ascii") as f:
        f.write("www.logichome.org\n")
        f.write(str(input_width) + "\n")
        f.write(str(input_height) + "\n")
        f.write(output_line)
    print("작업 완료!")
    input("엔터를 눌러 종료합니다.")
    sys.exit(1)
except Exception as e:
    print("오류!")
    print(e)
    input("엔터를 눌러 종료합니다.")
    sys.exit(1)
