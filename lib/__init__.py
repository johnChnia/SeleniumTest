import sys
base_dir=sys.path[0][0:-4]
for dir in ('lib','case'):
	try:
		sys.path.index(base_dir + '/' + dir)
	except Exception as e:
		sys.path.append(base_dir + '/' + dir)


# import sys
# for dir in ('lib','case'):
# 	try:
# 		sys.path.index(sys.path[0] + '/' + dir)
# 	except Exception,e:
# 		sys.path.append(sys.path[0] + '/' + dir)
