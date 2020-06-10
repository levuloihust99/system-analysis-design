format = (
    "{\n"
    "\t|M{.133\linewidth-2\\tabcolsep-.6pt}\n"
    "\t|L{.133\linewidth-2\\tabcolsep-.6pt}\n"
    "\t|L{.067\linewidth-2\\tabcolsep-.6pt}\n"
    "\t|L{.25\linewidth-2\\tabcolsep-.6pt}\n"
    "\t|L{.15\linewidth-2\\tabcolsep-.6pt}\n"
    "\t|L{.267\linewidth-2\\tabcolsep-.6pt}|\n"
    "}\n"
)

with open("input.txt", "r") as fr:
    raw = fr.read()

raw = raw.replace("{|c|l|l|l|l|l|}", format)
raw = raw.replace("\multicolumn{ ", "\multicolumn{")
# print(raw)
raw = raw.replace("\multicolumn{5}{c|}", "\multicolumn{5}{M{.867\linewidth-2\\tabcolsep-.6pt}|}")
raw = raw.replace("\multicolumn{2}{c|}", "\multicolumn{2}{L{.317\linewidth-2\\tabcolsep-.6pt}|}")
raw = raw.replace("\multicolumn{2}{L{.317\linewidth-2\\tabcolsep-.6pt}|}{\\textbf", "\multicolumn{2}{M{.317\linewidth-2\\tabcolsep-.6pt}|}{\\textbf")
raw = raw.replace("\multicolumn{1}{c|}{\\textbf{Tên", "\multicolumn{1}{M{.133\linewidth-2\\tabcolsep-.6pt}|}{\\textbf{Tên")
raw = raw.replace("\multicolumn{1}{c|}{\\textbf{Phạm", "\multicolumn{1}{M{.067\linewidth-2\\tabcolsep-.6pt}|}{\\textbf{Phạm")
raw = raw.replace("\multicolumn{1}{c|}{\\textbf{Kiểu dữ liệu", "\multicolumn{1}{M{.15\linewidth-2\\tabcolsep-.6pt}|}{\\textbf{Kiểu dữ liệu")
raw = raw.replace("\multicolumn{1}{c|}{\\textbf{Danh sách", "\multicolumn{1}{M{.25\linewidth-2\\tabcolsep-.6pt}|}{\\textbf{Dách sách")
raw = raw.replace("\multicolumn{1}{c|}{\\textbf{Mục đích", "\multicolumn{1}{M{.267\linewidth-2\\tabcolsep-.6pt}|}{\\textbf{Mục đích")
raw = raw.replace("tabular", "longtable")

with open("latex.txt", "w") as fp:
    fp.write(raw)