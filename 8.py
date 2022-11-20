def save_applicant_data(source, output):
    with open(output, "w") as fh:
        for stud in source:
            fh.write(stud["name"]+","+str(stud["specialty"])+"," +
                     str(stud["math"])+","+str(stud["lang"])+","+str(stud["eng"])+"\n")

        fh.close()
