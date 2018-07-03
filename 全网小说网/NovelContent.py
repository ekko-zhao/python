# coding:utf-8
import requests
from bs4 import BeautifulSoup

#爬一篇小说内容的类
class ANovel(object):
	def __init__(self,title=None, author=None, cover=None, desc=None, novel_url=None, chapters_url=None):
		self.NovleTitle = title    #小说名
		self.Author = author       #小说作者
		self.CoverImageUrl = cover #封面图片链接
		self.Desc = desc           #小说简介
		self.NovleUrl = novel_url  #小说跳转链接
		self.ChaptersUrl = chapters_url #小说目录链接
		self.Chapters = []         #小说所有章节(chapterTitle, chapterUrl)列表

	#读取传入参数url的网页源码
	def readHtml(self,url):
		#print(url)
		html = requests.get(url)
		html.encoding = 'gbk'
		return html.text

	#获取所有章节列表
	def getChaptersUrl(self):
		html = self.readHtml(self.ChaptersUrl)
		soup = BeautifulSoup(html,"html.parser")
		for chapter in soup.select('.chapterNum ul li a'):
			self.Chapters.append((chapter.string, chapter['href'])) #获取章节名称和链接
		return self.Chapters

	#获取某章节内容
	def getOneChapterContent(self,chapter):
		#print(chapter)
		html = self.readHtml(chapter[1])
		soup = BeautifulSoup(html,"html.parser")
		content_drop = soup.select("#content")[0].text  #抓取id=content的内容
		content_drop = content_drop.replace("style5();", "").replace("style6();", "").replace('<br />', '\n').replace(u'\xa0', u' ').replace(u'\ufffd', u' ')
		self.Write2Txt(chapter[0],content_drop)

	def Write2Txt(self,chapter_name,content):
		with open('Novels/' + self.NovleTitle + '.txt', 'a',encoding="utf-8") as file:
			print(self.NovleTitle+"正在写入%s，"%chapter_name)
			file.writelines(chapter_name + "\n\n" + content + "\n\n")
