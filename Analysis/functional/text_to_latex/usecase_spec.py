
import numpy as np
import yaml
from string import Template

# fixed, do not adjust
portion = [0.19, 0.09, 0.114, 0.038, 0.057, 0.095, 0.043, 0.128, 0.256]
portion = np.array(portion)




with open("table.yml", 'r') as stream:
    table = yaml.safe_load(stream)


header = table['header']
ID = header['ID']
name = header['name']
actor = header['actor']
# important_level = header['important_level']
description = header['description']
trigger = header['trigger']
precondition = header['precondition']
extensions = header['extensions']


children = []

for key in table.keys():
    if key == 'header':
        continue
    sub_uc = (table[key]['uc_name'],
              table[key]['normal_flow'],
              table[key]['child_flow'],
              table[key]['alter_flow']
    )
    children.append(sub_uc)


def value(x):
    if x is None:
        return ""
    return x

# begin
template = Template("M{$portion\\linewidth-2\\tabcolsep-.6pt}|\n\t")
column_format = "|\n\t" + "".join([template.substitute(portion=p) for p in portion])
begin_tabular = "\\begin{{longtable}}{{{0}}}\n".format(column_format)

# Row 1
storage = (
    "%Row 1\n"
    "\\hline\n"
    "\\cellcolor{{blue!20}}\\textbf{{Mã Use case}} &\n"
    "\\multicolumn{{3}}{{M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{1}}} &\n"
    "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Tên Use case}}}} &\n"
    "\\multicolumn{{2}}{{M{{{3:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{4}}}\\\\\\hline\n"
).format(portion[1:4].sum(), ID, portion[4:7].sum(), portion[7:9].sum(), name)
result = "{0}{1}".format(begin_tabular, storage)
# print(result)

# Row 2
storage = (
    "%Row 2\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Tác nhân chính}}}} &\n"
    "\\multicolumn{{7}}{{L{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}} \\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:].sum(), actor)
result = "{0}{1}".format(result, storage)
# print(result)

# Row 3
storage = (
    "%Row 3\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Mô tả ngắn gọn}}}} &\n"
    "\\multicolumn{{7}}{{L{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}}\\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:].sum(), description)
result = "{0}{1}".format(result, storage)
# print(result)

# Row 4
storage = (
    "%Row 4\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Điều kiện tiên quyết}}}} &\n"
    "\\multicolumn{{7}}{{L{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}}\\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:].sum(), precondition)
result = "{0}{1}".format(result, storage)

# Row 5
storage = (
    "%Row 5\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Sự kiện kích hoạt}}}} &\n"
    "\\multicolumn{{7}}{{L{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}}\\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:].sum(), trigger)
result = "{0}{1}".format(result, storage)

# Row 6
storage = (
    "%Row 6\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Điểm mở rộng}}}} &\n"
    "\\multicolumn{{7}}{{L{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}}\\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:].sum(), extensions)
result = "{0}{1}".format(result, storage)

# loop row
def child_flow(child):
    name = child[0]
    normal_flow = child[1]
    sub_flow = child[2]
    alter_flow = child[3]

    #normal flow
    first_line = (
        "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\cellcolor{{blue!20}}}} &\n"
        "\\cellcolor{{orange!40}}\\textbf{{STT}} &\n"
        "\\multicolumn{{3}}{{M{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{orange!40}}\\textbf{{Thực hiện bởi}}}} &\n"
        "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{orange!40}}\\textbf{{Hành động}}}} \\\\ \\cline{{3-9}}\n"
    ).format(portion[0:2].sum(), portion[3:6].sum(), portion[6:].sum())

    normal_string = "{0}{1}".format(first_line, "")
    line_number = 1
    while line_number <= len(normal_flow) - 1:
        idx = line_number - 1
        line = (
            "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\cellcolor{{blue!20}}}} &\n"
            "{1} &\n"
            "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
            "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\cline{{3-9}}\n%\n"
        ).format(portion[0:2].sum(), line_number, portion[3:6].sum(), normal_flow[idx][0], portion[6:].sum(), normal_flow[idx][1])

        normal_string = "{0}{1}".format(normal_string, line)
        line_number += 1
    
    idx = len(normal_flow) - 1
    last_line = (
        "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\cellcolor{{blue!20}}\\multirow{{-{6}}}{{*}}[1em]{{\\parbox{{{0:.3f}\\textwidth-2\\tabcolsep-.6pt}}{{\\centering\\textbf{{Luồng sự kiện chính}}}}}}}} &\n"
        "{1} &\n"
        "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
        "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\hline\n%\n"
    ).format(portion[0:2].sum(), line_number, portion[3:6].sum(), normal_flow[idx][0], portion[6:].sum(), normal_flow[idx][1], len(normal_flow) + 1)

    normal_string = "{0}{1}".format(normal_string, last_line)

    # sub_flow
    if sub_flow is not None:
        subflow_string = "{0}{1}".format(first_line, "")
        for subflow_item in sub_flow[:-1]:
            line = (
                "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}}} &\n"
                "{1} &\n"
                "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
                "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\cline{{3-9}}\n%\n"
            ).format(portion[0:2].sum(), subflow_item[0], portion[3:6].sum(), subflow_item[1], portion[6:].sum(), subflow_item[2])
            subflow_string = "{0}{1}".format(subflow_string, line)

        item = sub_flow[len(sub_flow) - 1]
        last_line = (
            "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\multirow{{-{6}}}{{*}}[1em]{{\\parbox{{{0:.3f}\\textwidth-2\\tabcolsep-.6pt}}{{\\centering\\textbf{{Luồng sự kiện rẽ nhánh}}}}}}}} &\n"
            "{1} &\n"
            "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
            "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\hline\n%\n"
        ).format(portion[0:2].sum(), item[0], portion[3:6].sum(), item[1], portion[6:].sum(), item[2], len(sub_flow) + 1)

        subflow_string = "{0}{1}".format(subflow_string, last_line)
    
    # alter flow
    if alter_flow is not None:
        alter_string = "{0}{1}".format(first_line, "")
        for alter_item in alter_flow[:-1]:
            line = (
                "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\cellcolor{{blue!20}}}} &\n"
                "{1} &\n"
                "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
                "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\cline{{3-9}}"
            ).format(portion[0:2].sum(), alter_item[0], portion[3:6].sum(), alter_item[1], portion[6:].sum(), alter_item[2])

            alter_string = "{0}{1}".format(alter_string, line)

        alter_last = alter_flow[len(alter_flow) - 1]
        last_line = (
            "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\multirow{{-{6}}}{{*}}[1em]{{\\parbox{{{0:.3f}\\textwidth-2\\tabcolsep-.6pt}}{{\\centering\\textbf{{Luồng sự kiện ngoại lệ}}}}}}}} &\n"
            "{1} &\n"
            "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
            "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\hline\n%\n"
        ).format(portion[0:2].sum(), alter_last[0], portion[3:6].sum(), alter_last[1], portion[6:].sum(), alter_last[2], len(alter_flow) + 1)

        alter_string = "{0}{1}".format(alter_string, last_line)

    return "%Normal flow\n{0}%Subflow\n{1}%Alter flow\n{2}".format(normal_string, subflow_string if sub_flow is not None else "", alter_string if alter_flow is not None else "")

if len(children) == 1:
    result = "{0}{1}".format(result, child_flow(children[0]))
else:
    count = 0
    for child in children:
        count += 1
        title = (
            "%Child title\n"
            "\\multicolumn{{9}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\cellcolor{{yellow!35}}\\textbf{{Use case con \\#{2}: {1}}}}} \\\\ \\hline\n"
        ).format(portion.sum(), child[0], count)

        result = "{0}{1}{2}".format(result, title, child_flow(child))

result = "{0}\\end{{longtable}}\n".format(result)
with open('latex_code.txt', "w") as fw:
    fw.write(result)
