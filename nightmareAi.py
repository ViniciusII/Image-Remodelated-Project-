import replicate
from time import sleep
import os
import csv


def get_token():
    os.environ["REPLICATE_API_TOKEN"] = "r8_KIRrua8pL74NyeZZYtSqF8lf9IJMm8z4Ja0rK"
    print(f'Your Acess Token is: {(os.environ.get("REPLICATE_API_TOKEN"))}')


def choice_method():
    try:
        method = int(input(''''
        Choice your method to consume the image (Press the Number of your Option):
        [1] Archive
        [2] Link
        \n\n'''))

        if method != 1 and method != 2:
            print('This option does not exist\n')
            sleep(2)
            choice_method()
        return method

    except ValueError:
        print('Your character is not a number, please try again\n\n')
        sleep(2)
        choice_method()


def get_image_archive() -> str:
    image_archive_name = str(input('Please, send me the name of your image archive, exemple: image.jpg\n\n')).strip()
    return image_archive_name


def image_list() -> list:
    with open('input.csv', 'r', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_list = [item for item in csv_reader]
    return csv_list


def image_archive(archive_name: str) -> str:
    print('Your image is being reshaped.. Wait a Feel Seconds..\n')
    try:
        output_archive_image = replicate.run(
            "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
            scale = 2,
            face_enhance = True,
            input={"image": open(archive_name, 'rb')}
        )
    except FileNotFoundError:
        print('This archive does not exist, try again..')
    return [output_archive_image]


def image_link(list_image: list) -> str:
    print('Your image is being reshaped.. Wait a Feel Seconds..\n')
    output_list_img = replicate.run(
        "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
        scale = 2,
        face_enhance = True,
        input={"image": list_image}
    )
    return str(output_list_img)


def save_csv(image_resharped_list: list) -> str:
    with open('output_resharped.csv', 'w', encoding='utf8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in image_resharped_list:
            csv_writer.writerow([item])
        print('Wow, your image has been restored, and your CSV file has been created! Did you like the experience?')


def main():
    get_token()
    method = choice_method()
    if method == 1:
        img_file = get_image_archive()
        img_file_resharped = image_archive(img_file)
        save_csv(img_file_resharped)
    if method == 2:
        img_list_verify = list()
        img_links = image_list()
        for i in img_links:
            link_resharped = image_link(i[0])
            if link_resharped not in img_list_verify:
                img_list_verify.append(link_resharped)
            save_csv(img_list_verify)

if __name__ == '__main__':
    main()

'''

#>>>>teste direto na API<<<<

import replicate
import os
import csv

os.environ["REPLICATE_API_TOKEN"] = "r8_KIRrua8pL74NyeZZYtSqF8lf9IJMm8z4Ja0rK"

output = replicate.run(
    "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
    scale = 2,
    face_enhance = True,
    #input={"image": open('before_img_7896173100103.jpg', 'rb')}
    input = {"image": "https://www.unidasproducoes.com.br/wp-content/uploads/2014/12/erro-7.jpg"}
)

print(output)

'''