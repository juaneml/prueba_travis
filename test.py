import pytest
import test2

def test_blog_landing_page_ok():
    r = requests.get('http://agus.tinproject.es')
    assert r.status_code == 200

def test_blog_landing_page_ok2():
    r = requests.get('http://agus.tinproject.es')
    assert r.status_code == 200

def prueba():
    r = conexion()
    assert r.status_code == 200