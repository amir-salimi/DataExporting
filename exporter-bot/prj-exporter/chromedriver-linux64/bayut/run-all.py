import os 

bayut = [
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_abudhabi_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_ajman_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_alain_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_dubai_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_fujeirah_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_rasalkhaimah_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_sharjah_city_detials.py",
"/home/amir/Documents/export_data/exporter-bot/prj-exporter/chromedriver-linux64/bayut/bayut_ummalqawain_city_detials.py",
]

from subprocess import call

for i in bayut:
    os.system(f"python {i} &")