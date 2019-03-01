import glob
import os
import re
import xlrd
import xlwt
import collections

file_list = glob.glob(os.path.join(os.getcwd(), "Sirovi podaci 1", "*.txt"))

videoizlaz = []
samoprovjera1 = []
samoprovjera2 = []
samoprovjere = []

# ucitavanje podataka iz excela
for file_path in file_list:
    with open(file_path) as f_input:
        if re.search("videoizlaz",file_path):
            videoizlaz.append(f_input.read().strip().split("\n"))
        if re.search("samoprovjeraizlaz1", file_path):
            samoprovjera1.append(f_input.read().strip().split("\n"))
        if re.search("samoprovjeraizlaz2", file_path):
            samoprovjera2.append(f_input.read().strip().split("\n"))


videoizlaz = [int(item) for sublist in videoizlaz for item in sublist]
samoprovjera1 = [int(item) for sublist in samoprovjera1 for item in sublist]
samoprovjera2 = [int(item) for sublist in samoprovjera2 for item in sublist]

# sve samoprovjere
for s in samoprovjera1:
    samoprovjere.append(s)
for s in samoprovjera2:
    samoprovjere.append(s)


#dict za videi
videi = {}
for i in videoizlaz:
    if i in videi:
        videi[i] += 1
    else:
        videi[i] = 1
videi = collections.OrderedDict(sorted(videi.items()))


# dict za samoprovjera1
sp1 = {}
for i in samoprovjera1:
    if i in sp1:
        sp1[i] += 1
    else:
        sp1[i] = 1
sp1 = collections.OrderedDict(sorted(sp1.items()))


# dict za samoprovjera2
sp2 = {}
for i in samoprovjera2:
    if i in sp2:
        sp2[i] += 1
    else:
        sp2[i] = 1
sp2 = collections.OrderedDict(sorted(sp2.items()))


# dict za sve samoprovjere
sp = {}
for i in samoprovjere:
    if i in sp:
        sp[i] += 1
    else:
        sp[i] = 1
sp = collections.OrderedDict(sorted(sp.items()))

# ucitavanje podataka iz datoteke
path = ("/home/sanja/PycharmProjects/ozupPodaci/Sirovi podaci 1/Skup podataka za dopuniti 1.xls")
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)

data = []
for col in range(sheet.ncols):
    data.append([])
    for row in range(sheet.nrows):
        data[col].append(sheet.cell_value(row, col))

# list id-jeva za usporedivanje
# usporeduje se da li se student nalazi u pojedinom rjecniku
ids = []
for d in data:
    for i in range(1, len(d)):
        if d[0] == "id":
            ids.append(d[i])

# unos izracunatih podataka u listu
for d in data:
    if d[0] == "videos":
        for k, v in videi.items():
            for id in ids:
                if k == id:
                    d[k] = v

    if d[0] == "selfassesm1":
        for k, v in sp1.items():
            for id in ids:
                if k == id:
                    d[k] = v

    if d[0] == "selfassesm2":
        for k, v in sp2.items():
            for id in ids:
                if k == id:
                    d[k] = v

    if d[0] == "selfassesm":
        for k, v in sp.items():
            for id in ids:
                if k == id:
                    d[k] = v


# sve praznine zamijeni sa 0
for d in data:
    if d[0] == "videos":
        for i in range(1, len(d)):
            if d[i] == '':
                d[i] = 0
    if d[0] == "selfassesm1":
        for i in range(1, len(d)):
            if d[i] == '':
                d[i] = 0
    if d[0] == "selfassesm2":
        for i in range(1, len(d)):
            if d[i] == '':
                d[i] = 0
    if d[0] == "selfassesm":
        for i in range(1, len(d)):
            if d[i] == '':
                d[i] = 0

# ostaviti samo bitne podatke (kod ucitavanja iz exclea ima praznih redova)
podaci = {'id', 'Lectures', 'quiz1', 'quiz2', 'quizzes', 'labs', 'videos', 'selfassesm1', 'selfassesm2',
          'selfassesm', 'grade'}
data = [d for d in data if d[0] in podaci]

# unos u excel
path2 = ("/home/sanja/PycharmProjects/ozupPodaci/Sirovi podaci 1/Skup podataka - dopunjen.xls")
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('podaci')
row = 0
col = 0

for d in data:
    for i in d:
        sheet1.write(row, col, i)
        row += 1
    col += 1
    row = 0

workbook.save(path2)




