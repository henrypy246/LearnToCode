import locale
locale.setlocale(locale.LC_ALL, "vi_VN.utf8")
provinces = [
  'Hà Giang',
  'Hà Nam',
  'Hà Nội',
  'Hà Tĩnh',
  'Hòa Bình',
  'Hưng Yên',
  'Hải Dương',
  'Hải Phòng',
  'Hậu Giang'
]
provinces.sort(key=locale.strxfrm)
print(provinces)