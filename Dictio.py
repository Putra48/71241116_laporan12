# Latihan soal 1
# data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# print("key value item")

# for key, value in data.items():
#     print(key, value, key)

# Latihan soal 2
# lista = ['red', 'green', 'blue']
# listb = ['#FF0000', '#008000', '#0000FF']

# hasil = dict(zip(lista, listb))

# print(hasil)

# Latihan soal 3
# nama_file = input("Masukkan nama file : ")

# try:
#     file = open(nama_file, 'r')

#     email_count = {}

#     for line in file:
#         if line.startswith("From "):
#             parts = line.split()
#             email = parts[1]
#             if email in email_count:
#                 email_count[email] += 1
#             else:
#                 email_count[email] = 1

#     file.close()

#     email_count_urut = dict(sorted(email_count.items()))

#     print(email_count_urut)

# except FileNotFoundError:
#     print("File tidak ditemukan. Pastikan nama file benar.")
# except Exception as e:
#     print("Terjadi kesalahan:", e)

# Latihan soal 4
nama_file = input("Masukkan nama file: ")

try:
    file = open(nama_file, 'r')

    domain_count = {}

    for line in file:
        if line.startswith("From "):
            parts = line.split()
            email = parts[1] 
            domain = email.split('@')[1] 

            if domain in domain_count:
                domain_count[domain] += 1
            else:
                domain_count[domain] = 1

    file.close()

    print(domain_count)

except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file benar.")
except Exception as e:
    print("Terjadi kesalahan:", e)

