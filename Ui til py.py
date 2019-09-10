from PyQt5 import uic
fin = open("", 'r')
fout = open("", 'w')
uic.compileUi(fin, fout, execute=False)
fin.close()
fout.close()
