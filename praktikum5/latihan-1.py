

b={'ari':'085267888','dina':'087677776'}
print('Kontak awal')
print('==============================')
print('    nama    |   nomor teleon')
print('==============================')
print('1.    ari   |   085267888','\n2.    dina    |   087677776')

# tamprintilkan kontak ari
print('\nTampilkan Kontak Ari')
print('1.    ari      |   ',b['ari'])
print('\nMenambah Kontak Riko')
b['riko']='087654544'
print('1.   ari      |   ',b['ari'])
print('2.   dina     |   ',b['dina'])
print('3.   riko     |   ',b['riko'])
print('\nMengubah nomor Dina ke')
b['dina']='088999776'
print('1.   ari      |   ',b['ari'])
print('2.   dina     |   ',b['dina'])
print('3.   riko     |   ',b['riko'])
print('\nMenampilkan semua nama')
print(b.keys())
print('\nMenampilkan semua nomor')
print(b.values())
print('\nMenampilkan semua nama dan nomor')
print(b)
print('\nMenghapus kontak dina')
del b['dina']
print(b,'\n')