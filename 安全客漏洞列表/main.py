from vulList import *
import csv

if __name__ == '__main__':
	url = 'https://www.anquanke.com/vul/list?orderby=updated&page=1'
	pages = getAllPages(url)
	with open("test.csv","a",newline='') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow(['漏洞名称','漏洞CVE编号','公布时间','更新时间','漏洞来源'])
	for i in range(1,pages+1):
		url = 'https://www.anquanke.com/vul/list?orderby=updated&page=' + str(i)
		vulns = getVulnInfo(url)
		vulnSource(vulns)