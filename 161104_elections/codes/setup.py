import os

def class_home_dir():
    classhomedir = '.'
    if not os.path.exists(classhomedir):
        raise Exception('something is very wrong: %s does not exist'%classhomedir)
    return classhomedir

def code_home_dir():
    codehomedir = os.path.join(class_home_dir(), 'codes\\')
    return codehomedir

def data_home_dir():
    datahomedir = os.path.join(class_home_dir(), 'data\\')
    if not os.path.exists(datahomedir):
        os.makedirs(datahomedir)
    return datahomedir

    
if __name__ == '__main__':
    datahomedir = data_home_dir()

    print "data home directory:", datahomedir
    
    import py_compile
    py_compile.compile(os.path.join(code_home_dir(),'setup.py'))
