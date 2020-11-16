from interfaceLogic import *
import os


def test_2():
    """ check 'read file' function - if correct list has been returned - first creates check2.txt"""
    with open("check2.txt", "w") as file:
        data = ('Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen''\n'
                '2020-09-01, 138, 139.5, 136, 136.25, 640779''\n'
                '2020-09-02, 136.45, 139.5, 136.05, 138.2, 638032')
        file.write(data)
    filename = os.path.abspath('check2.txt')
    assert read_file(filename) == [
        ['2020-09-01', 138.0, 139.5, 136.0, 136.25, 640779.0], ['2020-09-02', 136.45, 139.5, 136.05, 138.2, 638032.0]]


def test_3():
    """ check 'read file' function if suspected ERROR has been returned"""
    with open('check1.txt', 'w') as file:
        file.write('')
    filename = os.path.abspath('check1.txt')
    assert read_file(filename) == 'IndexError'


def test_4():
    """ check 'read file' function if suspected ERROR has been returned"""
    assert read_file('path unknown') == 'FileNotFoundError'


def test_5():
    """ check function data_analyst"""
    assert data_analyst([['2020-09-01', 138.0, 139.5, 136.0, 136.25, 640779.0],
                         ['2020-09-02', 136.45, 139.5, 136.05, 138.2, 638032.0]]) == (
               '2020-09-01 / 2020-09-02', 0.19999999999998863, 138.0, 138.2, 139.5, 136.0)


def test_6():
    """ check function data_analyst"""
    assert data_analyst('aaaaaaaaa') == 'IndexError'


def test_7():
    """ check function data_analyst"""
    assert data_analyst([['2020-09-01', '2020-09-01', 138.0, 139.5, 136.0, 136.25, 640779.0],
                         ['2020-09-02', 136.45, 139.5, 136.05, 138.2, 638032.0]]) == 'TypeError'


def test_8():
    """ check function open path if returned path is correct - first creates file with path"""
    filename = os.path.abspath('check1.txt')
    with open("chosen_file.txt", "w") as file:
        file.write(filename)
    assert open_path() == filename


def test_9():
    """ check function data_analyst - if error is returned - first clears the file"""
    with open('chosen_file.txt', 'w') as file:
        file.write('')
    assert open_path() == 'FileNotFoundError'


def test_10():
    """check if closing_price function returned Error - now file is empty"""
    assert closing_price() == 'FileNotFoundError'


def test_11():
    """check if closing_price function returned correct value - now file is empty, so overwrite 'chosen_file.txt'"""
    filename = os.path.abspath('check2.txt')
    with open('chosen_file.txt', 'w') as file:
        file.write(filename)
    assert closing_price() == 138.2


def test_12():
    """just deletes file chosen_file.txt after test's"""
    assert clean_after_test('./chosen_file.txt')== False
    assert clean_after_test('./check1.txt')== False
    assert clean_after_test('./check2.txt')== False


def clean_after_test(file_name) -> bool:
    file_delete = os.path.isfile(file_name)
    if file_delete:
        file_path = os.path.abspath(file_name)
        os.remove(file_path)

    file_delete_check = os.path.isfile(file_name)
    return file_delete_check