from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#indata = open(from_file).read()
#indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready? Hit return to continue, Ctrl + C to abort."
#raw_input()

out_file = open(to_file, "w")
out_file.write(open(from_file).read())

print "All right. All done."

out_file.close()
#in_file.close()