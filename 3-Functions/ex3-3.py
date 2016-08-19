def print_row():
	print ('+ - - - - + - - - - + - - - - + - - - - +')
def print_column():
	print ('|         |         |         |         |')
def do_twice (f):
	f()
	f()
def do_four(f):
	do_twice(f)
	do_twice(f)
def do_block():
	print_row()
	do_four(print_column)
def do_grid():
	do_four(do_block)
	print_row()
do_grid()

