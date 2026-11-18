print ('====Kantin Umsu====')
total = 0

while True:
    print('daftar menu :')
    print('1.mie goreng = 8000')
    print('2.nasi goreng = 10000')
    print('3.mie ACEH = 15000')
    print('4.teh manis = 6000')
    print('5.teh pucuk = 7000')
    print('0.selesai')

    pilihan =int(input('masukan pilihan :'))

    if pilihan == 0:
        break
    elif pilihan == 1:
        harga = 8000
        nama = 'mie goreng'
    elif pilihan == 2:
        harga = 10000    
        nama ='nasi goreng'
    elif pilihan == 3:
        harga = 15000
        nama = 'mie Aceh'
    elif pilihan == 4:
        harga = 6000
        nama = 'teh manis'
    elif pilihan == 5:
        harga = 7000
        nama ='teh pucuk'
    else:
        print('menu tidak tersedia')
        continue

    jumlah = int(input('mau pesan berapa bg/kk :'))
    subtotal = harga*jumlah
    total += subtotal

    print('===STRUK PEMBAYARAN===')
    print('total belanja: Rp.',total)

    if total >= 10000:
        diskon =(total*20)/100
    else:
        diskon = 0

    total_bayar = total-diskon

    print('diskon: Rp.',diskon)
    print('Total pembayaran : Rp.', total_bayar)
    print('terima kasih telah berbelanja di kantin kami')
    print('semoga harimu menyenangkan')
    

