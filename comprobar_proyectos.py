import importlib.util, pathlib, subprocess, sys, json, tempfile, shutil, math
from decimal import Decimal
from datetime import datetime, timedelta
root=pathlib.Path(__file__).resolve().parent
files=sorted(root.glob('*/solucion.py'))
assert len(files)==20
mods={}
for f in files:
 spec=importlib.util.spec_from_file_location(f.parent.name,f)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 mods[int(f.parent.name[:2])]=mod
 r=subprocess.run([sys.executable,str(f)],input=('1234\n0\n' if f.parent.name.startswith('03_') else '100\n0\n0\n0\n0\n0\nn\n' if f.parent.name.startswith('08_') else '1\n1\n1\n1\n1\nn\n' if f.parent.name.startswith('11_') else 'hola\n\n' if f.parent.name.startswith('13_') else 'fin\n' if f.parent.name.startswith('16_') else 'Ana\nn\nBob\nn\n0\n' if f.parent.name.startswith('14_') else '0\n'),capture_output=True,text=True,timeout=3)
 assert r.returncode==0,(f,r.stderr)
 for fn in ('README.md','enunciado.md','explicacion.md'):
  assert (f.parent/fn).is_file()
# Unit tests main algorithms
m=mods
assert m[1].calcular('1',2,3)==5
assert m[1].calcular('7',200,15)==30
try: m[1].calcular('5',-2,0.5); assert False
except ValueError: pass
assert m[2].media([6,7,8])==7
assert m[4].cargar()=={} # no data yet
assert m[5].convertir('longitud',1,'km','m')==1000
assert m[5].convertir('temperatura',32,'f','c')==0
assert m[6].telefono_usado({'Ana':{'telefono':'123'}},'123')
assert m[7].precio_valido('9,95')==Decimal('9.95')
assert m[8].nomina(Decimal(1000),Decimal(100),Decimal(2),Decimal(10),Decimal(10),Decimal(5))[-1]==Decimal('952')
assert m[9].precio(0)==9 and m[9].precio(4)==7
pw=m[10].generar(20,[m[10].GRUPOS[x] for x in 'lns'])
assert len(pw)==20 and any(c.isdigit() for c in pw) and any(c.isalpha() for c in pw)
assert len(m[11].PREGUNTAS)>=5
start=datetime(2026,1,1,10)
assert m[12].coste(start,start+timedelta(hours=1,minutes=1))==4
assert m[13].analizar('Hola, hola mundo.')['frecuencias']['hola']==2
assert m[15].cuenta({'1':2,'4':1})==2080
assert m[16].calcular([1,2,2,3])['modas']==[2]
assert m[17].porcentaje({'a':'presente','b':'ausente'})==50
assert m[18].total({'1':1})[-1]>350
assert m[19].encontrar({'tareas':[{'id':1}]},1)['id']==1
assert m[20].disponible({'citas':[{'medico':'1','fecha':'2027-01-01','hora':'09:00'}]},'1','2027-01-01','09:00') is False
# Interactive smoke workflows in clean temporary directory, no persistent user data pollution
cases={
1:'1\n2\n3\n8\n0\n', 2:'1\nAna López\n5\n6\n7\n2\n6\n0\n',
3:'1234\n2\n10\n3\n20\n4\n0\n',4:'1\nB001\nDune\nHerbert\n3\nB001\nAna\n5\n4\nB001\n0\n',
5:'1\nkm\nm\n2\n0\n',6:'1\nAna\n612345678\na@b.com\n5\n0\n',
7:'1\nP1\nLápiz\n1.50\n10\n3\nP1\n2\n4\n0\n',
8:'1000\n100\n2\n10\n10\n5\nn\n',9:'2\n1\n1\n4\n3\n1\n1\n0\n',
10:'1\n16\nlns\n0\n',11:'1\n1\n1\n1\n1\nn\n',
12:'1\n1234ABC\n4\n2\n1234ABC\n0\n',13:'Hola hola mundo.\nhola\n\n',
14:'Ana\nn\nBob\nn\n1\nv1\n1\n2\n0\n',
15:'2\n1\n1\n2\n4\n1\n2\n5\n1\n0\n',
16:'1\n2\n2\n3\nfin\n',17:'1\nAna\n2\n2026-10-01\np\n3\n2026-10-01\n0\n',
18:'2\n1\n2\n4\nAHORRA10\n5\nn\n0\n',
19:'1\nEstudiar\nalta\n2\n4\n1\n0\n',20:'1\nP1\nAna\n3\n0\n'
}
for n,inp in cases.items():
 with tempfile.TemporaryDirectory() as d:
  s=pathlib.Path(d)/'solucion.py'
  shutil.copy2(files[n-1],s)
  r=subprocess.run([sys.executable,str(s)],input=inp,capture_output=True,text=True,timeout=5)
  assert r.returncode==0,(n,r.stderr,r.stdout[-500:])
  assert not r.stderr,(n,r.stderr)
print('OK: 20 proyectos, pruebas de arranque, casos interactivos y funciones principales.')
