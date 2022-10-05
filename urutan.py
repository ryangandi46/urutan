def mengurutkan():
    kalimat = str(input("Tulis sebuah kalimat : "))
    #memecahkan kalimat menjadi kata-kata
    kata = kalimat.split()
    #mengurutukann kata-kata
    kata.sort()
    #menampilkan kata-kata yang telah diurutkan
    print("berikut urutan kata-kata : " )
    for urut in kata:
        print(urut)
    print(' ')
    teks = kalimat
    huruf_vokal={
        'a':0,
        'i':0,
        'u':0,
        'e':0,
        'o':0
    }
    total_huruf_vokal = 0
    for karakter in teks :
        if karakter in['a','i','u','e','o']:
            huruf_vokal[karakter] += 1
            total_huruf_vokal += 1
    print(f'Total karakter: {len(teks)}')
    print(f'Total huruf vokal: {total_huruf_vokal}')
    print(f"""\
    a -> {huruf_vokal['a']}
    i -> {huruf_vokal['i']}
    u -> {huruf_vokal['u']}
    e -> {huruf_vokal['e']}
    o -> {huruf_vokal['o']}\
    """)
mengurutkan()

