import os
import platform
import time
import datetime
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 1000)

def user():
    usr = pd.read_csv('https://docs.google.com/spreadsheets/d/1PXxDnH2q5MGsWNard0lxnvmre7dI5JGIaYtoTWAAg48/export?format=csv', dtype=str)
    user_list = usr.values.tolist()
    user_list = [item for sublist in user_list for item in sublist]
    return user_list

def akun():
    nim = open("nim.txt",'rt')
    pw = open("pw.txt",'rt')
    nim = nim.read().rstrip()
    pw = pw.read().rstrip()

    matkul = open('matkul.txt','r')
    kelas = open('kelas.txt','r')
    matkul = matkul.read().rstrip()
    kelas = kelas.read().rstrip()
    matkul = matkul.split(',')
    kelas = kelas.split(',')
    
    return nim, pw, matkul, kelas

def login(nim, pw):
    driver.get('https://mahasiswa.unair.ac.id')
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/form/div[2]/input").send_keys(nim) #nim
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/form/div[3]/input").send_keys(pw) #password
    driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
    wait.until(EC.alert_is_present()) # alert
    driver.switch_to.alert.accept()
    wait.until(EC.alert_is_present()) # alert
    driver.switch_to.alert.accept()
    if driver.find_elements(By.XPATH, '/html/body/div[1]/div/span'): # alert cyberv2
        driver.find_element(By.XPATH, '/html/body/div[1]/div/span').click()
        wait.until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[1]/div')))

def mode_manual(jam, menit, detik, matkul, kelas):
    sekarang = datetime.datetime.now().replace(microsecond=0)
    aa = datetime.datetime(year=sekarang.year, month=sekarang.month, day=sekarang.day, hour=jam, minute=menit, second=detik)
    selisih = aa-sekarang
        
    time.sleep(selisih.total_seconds())
    time.sleep(3)

    timer = datetime.datetime.now().replace(microsecond=0)
    
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/a[4]').click() # klik menu krs
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="center_main_content"]'), "NAMA MATA KULIAH")) # tunggu muncul tabel krs

    for (a, b) in zip(matkul, kelas):
        try:
            driver.find_element(By.XPATH, f"//tbody[1]/tr[td[normalize-space()='{a}'] and td[normalize-space()='{b}']]/td[8]/input").click()
            wait.until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            wait.until(EC.invisibility_of_element_located((By.XPATH, f"//tbody[1]/tr[td[normalize-space()='{a}'] and td[contains(text(),'{b}')]]")))
            print(f"[#] Matkul {a} Kelas {b} Berhasil Diamankan")
        except: 
            print(f"[!] Matkul {a} Kelas {b} Gagal Diamankan")

    timer1 = datetime.datetime.now().replace(microsecond=0)
    selisih = timer1-timer

    # print("\n")
    # print(f"Waktu: {selisih.total_seconds()} detik")
    
def mode_auto(delay, matkul, kelas):
    n = 1
    matkul_terambil = []
    kelas_terambil = []
    sek = WebDriverWait(driver, 5)
    while True:
        driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/a[4]').click() #klik menu krs
        try:
            sek.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="center_main_content"]'), "NAMA MATA KULIAH")) # tunggu muncul tabel krs
            print(f"Pengecekan ke-{n}")
            print('\n')
            for (a, b) in zip(matkul, kelas):
                try:
                    driver.find_element(By.XPATH, f"//tbody[1]/tr[td[normalize-space()='{a}'] and td[normalize-space()='{b}']]/td[8]/input").click()
                    wait.until(EC.alert_is_present())
                    driver.switch_to.alert.accept()
                    wait.until(EC.invisibility_of_element_located((By.XPATH, f"//tbody[1]/tr[td[normalize-space()='{a}'] and td[contains(text(),'{b}')]]")))
                    matkul_terambil.append(f"{a}")
                    kelas_terambil.append(f"{b}")
                except: 
                    z = 1
            n = n + 1
            print('Matkul Berhasil Diamankan: ')
            for (j, k) in zip(matkul_terambil, kelas_terambil):
                print(f'[#] {j} Kelas {k}')
            print('\n')
            if set(matkul_terambil) == set(matkul):
                break
        except:
            time.sleep(5)  
        driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/a[17]').click() #klik menu minat prodi
        time.sleep(delay) # delay waktu e

def os_clear():
    sys_name = platform.system()
    if sys_name == 'Linux':
        os.system('clear')
    elif sys_name == 'Windows':
        os.system('cls')

def header(name):
    os_clear()
    print(r"""

		         ___====-_  _-====___
		   _--^^^#####//      \\#####^^^--_
		_-^##########// (    ) \\##########^-_
	       -############//  |\^^/|  \\############-
	     _/############//   (@::@)   \\############\_
	    /#############((     \\//     ))#############\
	   -###############\\    (oo)    //###############-
	  -#################\\  / VV \  //#################-
	 -###################\\/      \//###################-
	_#/|##########/\######(   /\   )######/\##########|\#_
	|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
	`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
	   `   `  `      `   / | |  | | \   '      '  '   '
		            (  | |  | |  )
		           __\ | |  | | /__
		          (vvv(VVV)(VVV)vvv)

	     █░█ █▀▀█ █▀▀ █▀▀█ █▀▀ █▀▀ ░░ █▀▀▄ █▀▀█ ▀▀█▀▀ 
	     █▀▄ █▄▄█ █▀▀ █▄▄▀ █▀▀ ▀▀█ ▀▀ █▀▀▄ █░░█ ░░█░░ 
	     ▀░▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ░░ ▀▀▀░ ▀▀▀▀ ░░▀░░
                                                by v1r
          """)
    print(f'Login sukses!')
    print(f'Akun: {nama}')
    print('')
    print('[1] Mode Manual')
    print('[2] Mode Otomatis')
    print('')
    pilihan_menu = int(input('Inputkan Pilihan: '))
    print('')
    return pilihan_menu

if __name__ == '__main__':
    nim, pw, matkul, kelas = akun()
    if nim not in user():
        print('[!] Pengguna tidak dikenali')
        exit(1)
    login(nim, pw)
    raw = driver.find_element(By.XPATH, "//div[@class='border_box']").text
    nama = raw.splitlines()[0].strip()

    pilihan_menu = header(nama)

    if pilihan_menu == 1:
        jam = int(input("Jam: "))
        menit = int(input("Menit: "))
        detik = int(input("Detik: "))
        print("")
        print("Sedang Menunggu ...")
        print("")
        mode_manual(jam, menit, detik, matkul, kelas)
        print("")
        print("Program Selesai")
        print("\n")

    elif pilihan_menu == 2:
        delay = int(input('Jeda (detik): '))
        print("\n")
        mode_auto(delay, matkul, kelas)
        print("\n")
        print("Program Selesai")
        print("\n")

    else:
        print('Inputan tidak valid')

