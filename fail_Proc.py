import tkinter as tk
import time
from CaChannel import  CaChannel, CaChannelException
import threading
import shutil
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Application(tk.Frame):

	global procFlag
	procFlag=[0,0,0,0,0,0,0,0]
	global llrf_warnings
	llrf_warnings =[0,0,0,0,0,0,0,0]
	global llrf_warnings_text
	llrf_warnings_text =['腔压超限','栅极超限','前级超限','给定超限','腔体调谐故障','栅极调谐故障','腔体偏流源通讯故障','栅极偏流源通讯故障','中断信号故障']
	global trigFlag
	trigFlag = [0,0,0,0,0,0,0,0]
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()
	
	def create_widgets(self):
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "1#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 1)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "1#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 1)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "2#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 2)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "2#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 2)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "3#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 3)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "3#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 3)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "4#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 4)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "4#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 4)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "5#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 5)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "5#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 5)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "6#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 6)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "6#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 6)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "7#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 7)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "7#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 7)
		self.failProcOff.pack(side="top")
        
		self.failProcOn = tk.Button(self)
		self.failProcOn["text"] = "8#开启自动故障处理！"
		self.failProcOn["bg"] = "green"
		self.failProcOn["command"] = lambda : self.failProcStart(num = 8)
		self.failProcOn.pack(side="top")
		
		self.failProcOff = tk.Button(self)
		self.failProcOff["text"] = "8#关闭自动故障处理"
		self.failProcOff["bg"] = "red"
		self.failProcOff["command"] = lambda : self.failProcStop(num = 8)
		self.failProcOff.pack(side="top")

		self.quit = tk.Button(self, text="退出", fg="black", command=root.destroy)
		self.quit.pack(side="bottom")

	def failProcStart(self,num):
		global 	llrf_warnings
		global llrf_warnings_text
		global trigFlag
		def readWavesFunc(self, num):
			try:
				trigFlag[num -1] = 1
				file_str1 = ''
				file_str2 = ''
				file_str3 = ''
				file_str4 = ''
				file_str5 = ''
				file_str6 = ''
				file_str7 = ''
				file_str8 = ''
				file_str9 = ''
				file_str10 = ''
				time_record = time.strftime("%Y_%m_%d_%H_%M_%S")
				rf_warning_value = 0
                
				chan = CaChannel('rcsRf'+str(num)+':alarm0_get')
				chan.searchw()
				llrf_warnings[0] = chan.getw()
				if (llrf_warnings[0] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[0] +','
                
				chan = CaChannel('rcsRf'+str(num)+':alarm1_get')
				chan.searchw()
				llrf_warnings[1] = chan.getw()
				if (llrf_warnings[0] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[1] +','
                    
				chan = CaChannel('rcsRf'+str(num)+':alarm2_get')
				chan.searchw()
				llrf_warnings[2] = chan.getw()
				if (llrf_warnings[2] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[2] +','
                    
				chan = CaChannel('rcsRf'+str(num)+':alarm3_get')
				chan.searchw()
				llrf_warnings[3] = chan.getw()
				if (llrf_warnings[3] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[3] +','
                                    
				chan = CaChannel('rcsRf'+str(num)+':alarm4_get')
				chan.searchw()
				llrf_warnings[4] = chan.getw()
				if (llrf_warnings[4] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[4] +','
                    
				chan = CaChannel('rcsRf'+str(num)+':alarm5_get')
				chan.searchw()
				llrf_warnings[5] = chan.getw()
				if (llrf_warnings[5] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[5] +','
                                    
				chan = CaChannel('rcsRf'+str(num)+':alarm6_get')
				chan.searchw()
				llrf_warnings[6] = chan.getw()
				if (llrf_warnings[6] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[6] +','
                                    
				chan = CaChannel('rcsRf'+str(num)+':alarm7_get')
				chan.searchw()
				llrf_warnings[7] = chan.getw()
				if (llrf_warnings[7] == 1) :
					file_str1 = file_str1 + llrf_warnings_text[7] +'\n'
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT19:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '阳极水压欠压' +','

				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT20:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '阳极水压过压' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT21:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '阳极水流量' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT22:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '隔直电容水流量' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT23:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '方仓风水交换水流量' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT24:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '功放柜急停开关' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT25:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '监控柜急停开关' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT26:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '主风压节点' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT27:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '副风压节点' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT28:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '方舱冷却前侧风压节点' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT29:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str2 = file_str2 + '断路器闭锁' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT30:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '放电棒状态' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT31:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '接地开关' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT32:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '灯丝欠流' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT33:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '方舱冷却后侧风压节点' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT34:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '门开关' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT35:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '帘栅电源' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT36:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '加载腔漏水' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT39:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str3 = file_str3 + '大偏流源' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT40:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '人身联锁' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT41:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '加载腔总入水过压' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT42:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '末级功放帘栅过流' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT43:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '反馈放大器帘栅电流' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT44:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '加载腔总进水过温' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT45:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '左加载腔出水过温' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT46:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '右加载腔出水过温' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT47:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '反馈放大器V1管栅极过压' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT48:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '反馈放大器V3管栅极过压' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT49:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str4 = file_str4 + '反馈放大器电源' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT50:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '栅极电压' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT51:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '高压光过流' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT52:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '反馈放大器阳极电流' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT53:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '末级功放阳极过流' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT54:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '左加载腔出水流量' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT55:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '右加载腔出水流量' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT56:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '高压电流模块仓温度' +','
                                    
				chan = CaChannel('ACC_RCS_RRF:RFPS'+str(num)+'::INT57:ai')
				chan.searchw()
				rf_warning_value = chan.getw()
				if (rf_warning_value == 3) :
					file_str5 = file_str5 + '反馈放大器V2管栅极过压' +','


				chan = CaChannel('rcsRf'+str(num)+':wf_amp_skew.VALA')
				chan.searchw()
				wf_1 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_phaseError.VALA')
				chan.searchw()
				wf_2 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_cavTunningError.VALA')
				chan.searchw()
				wf_3 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_gridTunningError.VALA')
				chan.searchw()
				wf_4 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_gridBias.VALA')
				chan.searchw()
				wf_5 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_cavBias.VALA')
				chan.searchw()
				wf_6 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_frontAmp.VALA')
				chan.searchw()
				wf_7 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_gridAmp.VALA')
				chan.searchw()
				wf_8 = chan.getw()
                
				chan = CaChannel('rcsRf'+str(num)+':wf_cavAmp.VALA')
				chan.searchw()
				wf_9 = chan.getw()
                
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\llrf_warnings'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n%s\n%s\n%s\n%s\n'%(file_str1,file_str2,file_str3,file_str4,file_str5))
				parmFile.close()
                
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\ampSkew'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_1))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\phaseError'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_2))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\cavTunningError'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_3))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\gridTunningError'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_4))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\gridBias'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_5))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\cavBias'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_6))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\frontAmp'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_7))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\gridAmp'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_8))
				parmFile.close()
				
				parmFile = open(r'D:\eLog_Local\Software\Fail_Record\cavAmp'+str(num)+time_record+'.txt', 'w', encoding='utf-8')
				parmFile.write('%s\n'%(wf_9))
				parmFile.close()
				
				#延时1s
				time.sleep(1)
				print("Fail Wave Record finished!")
				
				#写ELOG

				driver = webdriver.Chrome()
				driver.get("http://elog.csns.ihep.ac.cn/Ring+RF/?cmd=Login")
                
				
                
				driver.find_element_by_name("uname").send_keys("longw")
				driver.find_element_by_name("upassword").send_keys("csnsrcsrf")
                
				driver.find_element_by_class_name("login_submit").click()
                
				WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "title2")))
				print(driver.title)
                
				driver.find_element_by_link_text("New").click()
				WebDriverWait(driver, 10)
				Select(driver.find_element_by_name("Category")).select_by_value("Fault")
				driver.find_element_by_id("Beam commissioning").click()
				str_text = '自动故障记录:'+time_record
				time.sleep(2)
				driver.find_element_by_name("Subject").send_keys(str_text)
				time.sleep(2)
				driver.find_element_by_name("attfile").send_keys('D:\eLog_Local\Software\Fail_Record\llrf_warnings'+str(num)+time_record+'.txt')
				time.sleep(2)
				driver.find_element_by_xpath("//input[@value='Upload']").click()
				time.sleep(1)
				driver.find_element_by_xpath("//input[@value='Submit']").click()
				time.sleep(1)
				driver.quit()
                
			except CaChannelException as e:
				print(e)
			
		global procFlag
		global trigFlag
		
		def failProcThread(self,num):
			failFlag = 0
			while procFlag[num-1]:
				time.sleep(5)
				chan = CaChannel('ACC_RCS_RRF:RRF'+str(num)+':LLRF:Alarm')
				chan.searchw()	
				failFlag = chan.getw()
                
				#print("procFlag:%d"%(procFlag[num-1]))
				#print("trigFlag:%d"%(trigFlag[num-1]))
				if failFlag == 0:
					trigFlag[num-1] = 0
				if ((failFlag == 1)and(trigFlag[num-1] == 0)):
					readWavesFunc(self,num)
                    
		
		if procFlag[num-1] == 0:
			print("start")
			procFlag[num-1] = 1
			pr = threading.Thread(target=failProcThread,name ='failProcThread',args=(self,num))
			pr.start()
		else:
			print("failProc already running!")

	def failProcStop(self,num):
		global procFlag
		print("stop")
		procFlag[num-1] = 0

root = tk.Tk()
app = Application(master = root)
app.mainloop()
