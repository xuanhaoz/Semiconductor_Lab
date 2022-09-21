# python script used to read txt file data output
# use to either convert data to other format or analysis directly

# place this script in same directory as data file or specify the exact path to data file

# infile = "terminal_output.txt"
# infile = "TV-RFd.txt"
# infile = "TV-Rd.txt"
# infile = "TV.txt"
# infile = "TVlast.txt"
infile = "TVlast-Rd.txt"

with open(infile) as i:
    lines = [line.strip("[]. \n") for line in i]
    lines = [line for line in lines if line]


# V, Td, I: 1D lists of dimension = number of data points
# Can either directly use these for plotting or other analysis in python

# Use this for terminal_output
"""
V   = [float(line.split()[1]) for line in lines]
Td  = [float(line.split()[3]) for line in lines]
I   = [float(line.split()[5]) for line in lines]
"""

# Use this for TV-RFd, TV-Rd, TVlast-Rd
"""
V   = [float(line.split()[1]) for line in lines]
Td  = [float(line.split()[0]) for line in lines]
I   = [float(line.split()[2]) for line in lines]
"""

# Use this for TV, TVlast
V   = [float(line.split(", ")[2]) for line in lines]
Td  = [float(line.split(", ")[0]) for line in lines]
I   = [float(line.split(", ")[1]) for line in lines]

# In the future, try to use consistent output format.....

def write_file(outfile):
    with open(outfile,"w") as o:
        # header 
        o.write("V, Td, I\n")

        for v,t,i in zip(V,Td,I):
            # outline = (" ").join([str(v),str(t),str(i)])
            outline = "{}, {}, {}".format(v,t,i)
            o.write(outline+"\n")

# To write the variables to .csv file for excel or other formats
# write_file("terminal_output.csv")
# write_file("TV-RFd.csv")
# write_file("TV-Rd.csv")
# write_file("TV.csv")
# write_file("TVlast.csv")
write_file("TVlast-Rd.csv")
