# coding:utf-8
import requests
from bs4 import BeautifulSoup
from vulDetil import aVuln
import time
import socket


socket.setdefaulttimeout(10) #设置超时，自动关闭连接。加了这个就不会一直报错ConnectionResetError：10054

def readHtml(url):
	respose = requests.get(url)
	html = respose.text
	return html

def getVulnInfo(url):
	vulns = []
	html = readHtml(url)
	soup = BeautifulSoup(html,'html.parser')
	
	for item  in soup.select('tbody tr'):
		vuln_url = 'https://www.anquanke.com' + item.select('.vul-title-item a')[0]['href']
		vuln_name = item.select('.vul-title-item a')[0].text.replace('\xa9','@@').replace('\u0130','@@').replace('\xae','@@') #哎，特殊符号一直报错，直接替换掉了
		try:
			cve = item.select('.vul-cve-item')[0].text
		except:
			cve = 'N/A'
		start_time = item.select('.vul-date-item')[0].text.strip()
		update_time = item.select('.vul-date-item')[1].text.strip()
		vuln = [vuln_url,vuln_name,cve,start_time,update_time]
		vulns.append(vuln)
	return vulns

def vulnSource(vulns):
	for vuln in vulns:
		html = readHtml(vuln[0])
		soup = BeautifulSoup(html,"html.parser")
		vuln_source = soup.select('.article-content a')[0].text
		vuln.append(vuln_source)
		print(vuln)
		time.sleep(0.5) #保险起见，加上延时
		a_vuln = aVuln(vuln[0],vuln[1],vuln[2],vuln[3],vuln[4],vuln[5])
		a_vuln.write2csv()

def getAllPages(url):
	html = readHtml(url)
	soup =BeautifulSoup(html,'html.parser')
	allpage = int(soup.select('.page-link')[-1]['href'][-4:])
	print(allpage)
	return allpage