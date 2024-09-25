#cramos una nueva manera de importar
import F_repaso as fun
notas=[]
while True:
    fun.menu()
    fun.add_nota(notas)
    fun.add_nota(notas)
    fun.add_nota(notas)
    fun.del_notas(notas)
    fun.mod_nota(notas)
    fun.m_notas(notas)
    fun.cal_promedio(notas)
    fun.max_min_notas(notas)
    break
print("===\n", notas)
#Whispers, transcribit, reconocimiento de palabras