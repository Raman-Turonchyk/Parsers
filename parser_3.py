import requests
import img2pdf


def get_data():
    headers = {
        'Accept': 'image/avif,image/webp,*/*',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 103.0) Gecko / 20100101 Firefox / 103.0'
    }

    for i in range(1,49):
        url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f'Media/{i}.jpg', 'wb') as file:
            file.write(response)
            print(f'Downloaded {i} of 48')


def write_to_pdf():
    img_list = [f'Media/{i}.jpg' for i in range(1, 49)]

    with open('Ctalog.pdf', 'wb') as file:
        file.write(img2pdf.convert(img_list))

    print('PDF file created successfully!')


def main():
    get_data()
    write_to_pdf()

if __name__ == '__main__':
    main()