# coding:utf-8
import requests
import csv
from bs4 import BeautifulSoup
from NovelContent import ANovel

#读取传入参数Uurl的网页源码
def readHtml(url):
		html = requests.get(url)
		html.encoding = 'gbk'
		return html.text

def getNovelsInfo(url):
	novels = []
	html = readHtml(url)
	soup = BeautifulSoup(html, 'html.parser')
	for item in soup.select("section ul li"):
		title = item.select("span a")[0]['title'].decode('utf-8')
		author = item.select("span a")[1].text
		coverImage = item.select("img")[0]['src']
		desc = item.select("em")[0].text
		novelUrl = item.select("span a")[2]["href"]
		#print(title, author, coverImage, desc, novelUrl)
		novel = [title,author,coverImage,desc,novelUrl]
		novels.append(novel)
	return novels

def get_Chapters_Url(novels):
	for novel in novels:
		html = readHtml(novel[-1])
		soup = 	BeautifulSoup(html,"html.parser")
		obj = soup.select(".reader")
		#print(obj)
		if not obj:
			novel.append('')
		else:
			novel.append(obj[0]["href"])
	return novels

def allChaptersUrl(novels):
	for novel in novels:
		aNovel = ANovel(novel[0], novel[1], novel[2], novel[3], novel[4], novel[5])
		aNovel.getChaptersUrl()                                                      # 获取该小说对象的所有章节的链接
		#print(a_novel.Chapters[:10])                                                 # 打印小说章节列表中的前10章
		for chapter in aNovel.Chapters[:10]:              # 遍历该小说的所有章节
			aNovel.getOneChapterContent(chapter)     # 获取某一章节的文本内容