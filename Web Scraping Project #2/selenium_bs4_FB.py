import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd

def send_graphql_request(url, headers, payload):
    response = requests.post(url, headers=headers, data=payload)
    obj = response.json()
    return obj

def initialize_webdriver():
    opt = webdriver.ChromeOptions()
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])
    opt.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=opt)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def login_facebook(driver, username, password):
    driver.get('https://www.facebook.com/groups/PC.Enthusiast.Malaysia')
    username_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/form/div/div[3]/div/label/div/div/input')
    username_input.click()
    username_input.send_keys(username)
    password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/form/div/div[4]/div/label/div/div/input')
    password_input.click()
    password_input.send_keys(password)
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/form/div/div[5]/div/div')
    login_button.click()

def scrape_group_members(driver, obj):
    people = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/a[2]/div/span')
    people.click()
    time.sleep(3)

    name = []
    join_date = []
    bio_text = []
    url = []
    pfp = []

    for i in range(1, 10):
        join_date.append(obj.get('data').get('node').get('new_members').get('edges')[i].get('join_status_text').get('text'))
        url.append(obj.get('data').get('node').get('new_members').get('edges')[i].get('node').get('url'))
        name.append(obj.get('data').get('node').get('new_members').get('edges')[i].get('node').get('name'))
        pfp.append(obj.get('data').get('node').get('new_members').get('edges')[i].get('node').get('profile_picture').get('uri'))
        bio_text.append(obj.get('data').get('node').get('new_members').get('edges')[i].get('node').get('bio_text').get('text'))

    df = pd.DataFrame({
        'Name': name,
        'Join Date': join_date,
        'Bio Text' : bio_text,
        'Profile URL' : url,
        'Profile Picture URL' : pfp
    })

    return df

def save_data_to_excel(df, filename):
    df.to_excel(filename, index=True)

def main():
    url = "https://www.facebook.com/api/graphql/"
    payload = 'av=100002206178562&__user=100002206178562&__a=1&__req=e&__hs=19556.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1007858379&__s=xidep3%3A9pk0qr%3Awpnij5&__hsi=7257238461416158731&__dyn=7AzHK4HzEmwIxt0mUyEqxenFwLBwopU98nwgUao4u5QdwSxucyUco5S3O2Saw8i2S1DwUx60DUG0Z82_CxS320om78bbwto88422y11xmfz81s8hwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2Sq2-azo7u3C223908O321LwTwNxe6Uak1xwJwxyo6J0qo&__csr=gmR6mD7OYTbNlR5QlWdbbaxeyOh9adGAyiindlEIOcIAAgx2GSQSyd2939eBjRiT9GBqTN19qpirGIHV8OWAGZjQh4yADwFyklbAAjAGp6xaHgCeCGqjDx97xequmeAzbJ7hHhqGp28CqEyil1OHGm48iK2-5eiu48jASi3y2iawxyUeE8lzpopx-9gqxS8J162211CgKm5ppEjwwzF8pzHwOxm1mxe3q2q58-UKfwFzU8ob8W1eAwZG3e68hxW1zxy3i4U5m5Ee8uyawnE0raDw0en-03IK0Fo1FE0odwSgO1wBw4pw4Mw8Dw2nE6Km06iX9wq404JFU0gIx64-04Coai04hg0P91e5o760hKU1bo4S4h4C18g0qZDwJam7U0ZyhwDws80R-7FU6G0kR06ywmUC0xo1d80OO1sg1W9o&__comet_req=15&fb_dtsg=NAcOoZBfO7MpDXIm-C1AaOk2sVCvKOO_NOEb1h7D1uhDvieqrIY_Oig%3A12%3A1689704716&jazoest=25401&lsd=2NEbo4UUSYTvkcuB_oMW8A&__spin_r=1007858379&__spin_b=trunk&__spin_t=1689707502&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22AQHRSYhYJ5h-yrxvDljZTb_sgI8WcPEYUz3KQTLdBsLKRbRma1zOZCneMnD_uHTBDGu_NGf8UJADa2uax37sRYAspA%22%2C%22groupID%22%3A%22376997419553016%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22376997419553016%22%7D&server_timestamps=true&doc_id=7396994073660826'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Friendly-Name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
    'X-FB-LSD': '2NEbo4UUSYTvkcuB_oMW8A',
    'X-ASBD-ID': '129477',
    'Origin': 'https://www.facebook.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.facebook.com/groups/PC.Enthusiast.Malaysia/members',
    'Cookie': 'wd=870x947; datr=R8q2ZM9z3S_UlFQsReu1f40W; sb=bcq2ZHN2mQwWQ_37hjMz_8PZ; fr=0W7AV9Dd5ZDNK7vQV.AWVq4TUSr2CZc_1SzrXcelDVhD8.Bktspt.J8.AAA.0.0.BkttkM.AWXn2OIX-ek; usida=eyJ2ZXIiOjEsImlkIjoiQXJ5MDhnYzFtdWx5Z3UiLCJ0aW1lIjoxNjg5NzA1MjY0fQ%3D%3D; c_user=100002206178562; xs=12%3AvAvy6_wg27kFHg%3A2%3A1689704716%3A-1%3A5841; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1689707497450%2C%22v%22%3A1%7D; c_user=100002206178562; fr=0hzjHKvh6F8HTtpcb.AWX-Y_XkbqlQO6cSenE_39Ohx0g.BktuQk.J8.AAA.0.0.BktuQk.AWWBwRU9Fc8; xs=12%3AvAvy6_wg27kFHg%3A2%3A1689704716%3A-1%3A5841%3A%3AAcXS7BwsZDasHorRgdQHGz8CjKVAUFQNNXpFu_fv9A',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
    }

    obj = send_graphql_request(url, headers, payload)
    driver = initialize_webdriver()

    username = 'fazeel332@gmail.com'
    with open('pass.txt', 'r') as file:
        password = file.read().rstrip()
        
    login_facebook(driver, username, password)
    
    df = scrape_group_members(driver, obj)
    save_data_to_excel(df, 'fb_data.xlsx')

if __name__ == "__main__":
    main()