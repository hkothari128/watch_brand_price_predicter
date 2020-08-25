import csv
import requests
with open('watches.csv','r') as f:
    reader = csv.reader(f)
    idx = 0
    for row in reader:
        Name, brand, img, price = row
        # print(Name, brand, img, price)
        response = requests.get(img)

        img_file = open("images/{idx}-{brand}-{price}.png".format(brand=brand, idx=idx,price=price), "wb")
        img_file.write(response.content)
        img_file.close()
        idx += 1
        # break
    
