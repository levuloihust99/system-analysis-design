
import numpy as np
from string import Template

# fixed, do not adjust
portion = [0.19, 0.09, 0.114, 0.038, 0.057, 0.095, 0.043, 0.128, 0.256]
portion = np.array(portion)

# input
ID = "UC013"
name = "Tạo Server"
actor = "Admin"
important_level = "Trung bình"
description = "Mô tả chức năng quản lý shop cho admin"
trigger = "Admin chọn chức năng \\textit{quản lý shop} từ giao diện trang quản lý"
association = "Admin"
include = None
extend = "Các use case mô tả phía dưới"
generalization = None

children = [] # list of sub-usecase

# first sub-usecase
name_child = "Thêm vật phẩm"
normal_flow = [
    ("Admin", "Từ giao diện quản lý Server, chọn \\textit{thêm server}"),
    ("Hệ thống", "Hiển thị form yêu cầu nhập tên của server mới"),
    ("Admin", "Nhập tên cho server mới"),
    ("Hệ thống", "Hiển thị form yêu cầu nhập thông báo đến người dùng"),
    ("Admin", "Nhập thông báo vào form"),
    ("Hệ thống", "Hiển thị yêu cầu lựa chọn thời điểm tạo mới server trên hệ thống game"),
    ("Admin", "Lựa chọn thời điểm tạo server"),
    ("Hệ thống", "Hiển thị yêu cầu xác nhận tạo server mới"),
    ("Admin", "Xác nhận tạo server mới"),
    ("Hệ thống", "Thông báo tạo mới hoàn tất"),
    ("Hệ thống", "Thêm thông báo về server mới lên website của hệ thống"),
    ("Hệ thống", "Hiển thị thông báo của về server mới trong giao diện chơi game của toàn bộ người dùng"),
]
sub_flow = None
alter_flow = None
children.append((name_child, normal_flow, sub_flow, alter_flow))

# second sub-usecase
# name_child = "Xem danh sách vật phẩm"
# normal_flow = None
# sub_flow = None
# alter_flow = None
# children.append((name_child, normal_flow, sub_flow, alter_flow))

# third sub-usecase
# name_child = "Xóa vật phẩm"
# normal_flow = None
# sub_flow = None
# alter_flow = None
# children.append((name_child, normal_flow, sub_flow, alter_flow))

# fourth child
# name_child = "Cập nhật giá vật phẩm"
# normal_flow = (
#     ("Admin", "Chọn vật phẩm từ danh sách vật phẩm"),
#     ("Hệ thống", "Hiển thị thông tin vật phẩm"),
#     ("Admin", "Chọn cập nhật giá vật phẩm"),
#     ("Hệ thống", "Hiển thị cửa sổ cập nhật giá vật phẩm"),
#     ("Admin", "Nhập giá mới cho vật phẩm"),
#     ("Admin", "Xác nhận thực hiện cập nhật"),
#     ("Hệ thống", "Thông báo cập nhật giá thành công cho vật phẩm"),
# )
# sub_flow = None
# alter_flow = [
#     ("6a", "Admin", "Hủy bỏ thao tác cập nhật giá vật phẩm"),
# ]
# children.append((name_child, normal_flow, sub_flow, alter_flow))

# fifth child 
# name_child = "Xem thống kê lịch sử giao dịch"
# normal_flow = (
#     ("Admin", "Từ giao diện \\textit{quản lý shop}, chọn chức năng \\textit{xem thống kê lịch sử giao dịch}"),
#     ("Hệ thống", "Hiển thị thống kê lịch sử giao dịch"),
# )
# sub_flow = None
# alter_flow = None
# children.append((name_child, normal_flow, sub_flow, alter_flow))

# output file name
out_file = "output.txt"

#
# Input2LaTeX
#

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
    "\\multicolumn{{3}}{{M{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}} &\n"
    "\\multicolumn{{3}}{{M{{{3:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Mức độ quan trọng}}}} &\n"
    "{4}\\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:5].sum(), actor, portion[5:8].sum(), important_level)
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
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\textbf{{Sự kiện kích hoạt}}}} &\n"
    "\\multicolumn{{7}}{{L{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{2}}}\\\\\\hline\n"
).format(portion[0:2].sum(), portion[2:].sum(), trigger)
result = "{0}{1}".format(result, storage)
# print(result)

# Row relationship
storage = (
    "%Row relationship\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}}} &\n"
    "\\multicolumn{{3}}{{M{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\textbf{{Association}}}} &\n"
    "\\multicolumn{{4}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} \\\\ \\cline{{3-9}}\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}}} &\n"
    "\\multicolumn{{3}}{{M{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\textbf{{Include}}}} &\n"
    "\\multicolumn{{4}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{4}}} \\\\ \\cline{{3-9}}\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}}} &\n"
    "\\multicolumn{{3}}{{M{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\textbf{{Extend}}}} &\n"
    "\\multicolumn{{4}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\cline{{3-9}}\n"
    "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\multirow{{-4}}{{*}}{{\\textbf{{Các mỗi quan hệ}}}}}} &\n"
    "\\multicolumn{{3}}{{M{{{1:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\textbf{{Generalization}}}} &\n"
    "\\multicolumn{{4}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{6}}} \\\\ \\hline\n"
).format(portion[0:2].sum(), portion[2:5].sum(), portion[5:].sum(), value(association), value(include), value(extend), value(generalization))
result = "{0}{1}".format(result, storage)
# print(result)

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
    if normal_flow is not None:
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
            "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\multirow{{-{6}}}{{*}}[1em]{{\\parbox{{{0:.3f}\\textwidth-2\\tabcolsep-.6pt}}{{\\centering\\textbf{{Luồng sự kiện con}}}}}}}} &\n"
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
            "\\multicolumn{{2}}{{|M{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\\cellcolor{{blue!20}}\\multirow{{-{6}}}{{*}}[1em]{{\\parbox{{{0:.3f}\\textwidth-2\\tabcolsep-.6pt}}{{\\centering\\textbf{{Luồng sự kiện thay thế/ngoại lệ}}}}}}}} &\n"
            "{1} &\n"
            "\\multicolumn{{3}}{{M{{{2:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{3}}} &\n"
            "\\multicolumn{{3}}{{L{{{4:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{{5}}} \\\\ \\hline\n%\n"
        ).format(portion[0:2].sum(), alter_last[0], portion[3:6].sum(), alter_last[1], portion[6:].sum(), alter_last[2], len(alter_flow) + 1)

        alter_string = "{0}{1}".format(alter_string, last_line)

    return "%Normal flow\n{0}%Subflow\n{1}%Alter flow\n{2}".format(normal_string if normal_flow is not None else "", subflow_string if sub_flow is not None else "", alter_string if alter_flow is not None else "")

if len(children) == 1:
    result = "{0}{1}".format(result, child_flow(children[0]))
else:
    count = 0
    for child in children:
        count += 1
        title = (
            "%Child title\n"
            "\\multicolumn{{9}}{{|L{{{0:.3f}\\linewidth-2\\tabcolsep-.6pt}}|}}{{\cellcolor{{yellow!35}}\\textbf{{\\#{2}: {1}}}}} \\\\ \\hline\n"
        ).format(portion.sum(), child[0], count)

        result = "{0}{1}{2}".format(result, title, child_flow(child))

result = "{0}\\end{{longtable}}\n".format(result)
with open(out_file, "w") as fw:
    fw.write(result)
