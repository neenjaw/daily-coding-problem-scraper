import pdfkit

ns = range(1, 175)
problems = []

for n in ns:
  problems.append(f"problem_{n}.html")

# print(problems)

pdfkit.from_file(problems, "out.pdf")