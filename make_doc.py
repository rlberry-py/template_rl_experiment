import sys
import os
import re
import glob
import subprocess

text = open(sys.argv[1], "r")

tag = "%%% @python-src@"
new_text = []

for x in text:
  if x[:len(tag)] == tag:
    new_text.append("```python\n")
    python_file = re.search(r'(?<='+tag+').*',x)
    if python_file is not None:
          python_file = python_file.group(0)
    else:
      raise ValueError(x + "was not recognized as a valid doc line.")

    with open(python_file, "r") as pf:
      for y in pf:
        new_text.append(y)
    new_text.append("```\n")
  else:
    new_text.append(x)

with open("generated_doc.md", "w") as f:
    f.write("".join(new_text))
    f.close()
print("Wrote generated_doc.md")
