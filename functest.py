from func import get_commission

def get_commision_test_0_15():
    date_str = "2022-07-30"
    assert get_commission(date_str) == 0.15
    
def get_commision_test_0_1():
    date_str = "2022-02-30"
    assert get_commission(date_str) == 0.1

def get_commision_test_none():
    date_str = "None"
    assert get_commission(date_str) == None
    
def get_commision_test_noth():
    date_str = ""
    assert get_commission(date_str) == None
    
def get_commision_test_year():
    date_str = "20123-02-30"
    assert get_commission(date_str) == None

def get_commision_test_month():
    date_str = "2012-18-30"
    assert get_commission(date_str) == None
    
def get_commision_test_day():
    date_str = "2012-12-50"
    assert get_commission(date_str) == None
    


if __name__ == "__main__":
    get_commision_test_0_15()
    get_commision_test_0_1()
    get_commision_test_none()
    get_commision_test_noth()
    get_commision_test_year()
    get_commision_test_month()
    get_commision_test_day()