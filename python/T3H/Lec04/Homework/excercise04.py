def logo(slogan):
	data = {
    'xanh lá': '#3cba54',
    'vàng': '#f4c20d',
    'đỏ': '#db3236',
    'xanh da trời': '#4885ed',
	}
	letters = list('slogan')
	letters_cover= []
	for x in letters:
		if x.lower() == 'g':
			letters_cover.append((x, data['xanh da trời']))
		else x.lower() == 'l':
			letters_cover.append((x,data[]))
	with open('index.html','w') as f:
		string =  '<span style="color:'+ 4885ed +'">G</span>'

		f.write()

