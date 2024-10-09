import os




search_root = "/home/yhzhang/workspace/biocas-conference.github.io"
year_path = "photos/2019"
search_path = os.path.join(search_root, year_path)





filelist = []

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(".JPG"):
            filepath = os.path.join(year_path, file)
            #print (filepath)
            filelist.append(filepath)


string = ""

for i, each in enumerate(filelist):
    if i % 4 == 0:
        string += """
<div class="flex flex-row pt-6 gap-4">\n
        """

    string += """
    <div class="basis-1/4">
        <img
            class="rounded-t-lg"
            src="{}"
            alt=""
            />
    </div>
    """.format(each)

    if i % 4 == 3:
        string += "\n</div>\n\n"
    
# 如果总计不是4的倍数，补齐
if len(filelist) % 4 != 0:
    string += "\n</div>"

with open("tmp.html", "w") as f:
    f.write(string)


            
