from sys import argv, stderr
from graphviz2drawio.graphviz2drawio import convert
def main(args):
	
	if len(args) > 1:
		for x in args[1:]:
			stderr.write("Converting %s" % x)
			output = convert(x)
			base = x.split('.')
			outfile = ".".join(base[:-1] + ["drawio"])
			with open(outfile, "w") as fd:
				fd.write(output)
			stderr.write(" ...done: " + outfile + "\n")
	else:
		print('no args')

if __name__ == "__main__":
	main(argv)
