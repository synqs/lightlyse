from .BasicClasses import Run

def test_import_run():
    r = Run('run030.h5', no_write = True)
    label = 'absorption'
    orientation = 'horizontal'
    Iat = r.get_image(orientation, label, 'NaAtoms')
