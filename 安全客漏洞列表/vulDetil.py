# coding:utf-8
import requests
import csv


class aVuln(object):
	
	def __init__(self,vuln_url,vuln_name,cve,start_time,update_time,vuln_source):
		self.Vuln_url = vuln_url
		self.Vuln_name = vuln_name
		self.CVE = cve
		self.Start_time = start_time
		self.Update_time = update_time
		self.Vuln_source = vuln_source
	def readHtml(self,url):
		respose = requests.get(url)
		html = respose.text
		return html


	def write2csv(self):
		
		with open("test.csv","a",newline='') as csvfile:  #加newline=''，不然每行都会加一行空行
			writer = csv.writer(csvfile)
			#writer.writerow(['漏洞名称','漏洞CVE编号','公布时间','更新时间','漏洞来源'])
			#print(self.Vuln_name,self.CVE,self.Start_time,self.Update_time,self.Vuln_source)
			writer.writerow([self.Vuln_name,self.CVE,self.Start_time,self.Update_time,self.Vuln_source])