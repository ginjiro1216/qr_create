import os, csv, qrcode
qr1_names = []
qr2_names = []
qr3_names = []


def qr_create():

    def qr1_create():
        count1 = 1
        with open('qrtest.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for line1 in reader:
                qr_url = line1[10]
                qr1_names.append(str(1) + '-' + str(count1) + '.png')
                with open('qr1_name', 'w') as w:
                    writer = csv.writer(w)
                    for qr1_name in qr1_names:
                        writer.writerow([qr1_name])
                img = qrcode.make(qr_url)
                img.save(str(1) + '-' + str(count1) + '.png')
                count1 += 1

    def qr2_create():
        count2 = 1
        with open('qrtest.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for line2 in reader:
                qr_url = line2[14]
                qr2_names.append(str(2) + '-' + str(count2) + '.png')
                with open('qr2_name', 'w') as w:
                    writer = csv.writer(w)
                    for qr2_name in qr2_names:
                        writer.writerow([qr2_name])
                img = qrcode.make(qr_url)
                img.save(str(2) + '-' + str(count2) + '.png')
                count2 += 1

    def qr3_create():
        count3 = 1
        with open('qrtest.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for line3 in reader:
                qr_url = line3[18]
                qr3_names.append(str(3) + '-' + str(count3) + '.png')
                with open('qr3_name', 'w') as w:
                    writer = csv.writer(w)
                    for qr3_name in qr3_names:
                        writer.writerow([qr3_name])
                img = qrcode.make(qr_url)
                img.save(str(3) + '-' + str(count3) + '.png')
                count3 += 1

    qr1_create()
    qr2_create()
    qr3_create()


if __name__ == '__main__':
    qr_create()

