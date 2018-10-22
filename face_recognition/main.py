import face_recognition
import dataset
import os
import shutil

print("Выберите пункт:\n1-добавить лицо;\n2-удалить все лица;\n3-распознование.")
nomer = input()
if  nomer== '1':
    dataset.add_dataset()
elif nomer=='3':
    face_recognition.rec_face()
elif nomer=='2':
    shutil.rmtree('dataset')
    os.mkdir('dataset')









