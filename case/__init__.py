import sys
base_dir=sys.path[0][0:-5]
for dir in ('lib','case'):
	try:
		sys.path.index(base_dir + '/' + dir)
	except Exception as e:
		sys.path.append(base_dir + '/' + dir)
