import os 
os.environ['KIVY_NO_C0NSOLELOG']='1'

from kivymd.app import MDApp		
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivymd.uix.list import OneLineListItem
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image 
from kivymd.toast import toast
from kivymd.uix.picker import MDThemePicker
from kivy.uix.recycleview import RecycleView
import time
from kivy.storage.jsonstore import JsonStore 
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty,ListProperty
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
import random
from kivmob import KivMob, TestIds

from kivy.clock import Clock
#from kivy.uix.screenmanager.SwapTransition import SwapTransition
from meann import *
#Window.size=(400,600)

Builder.load_string("""

<cus>:
	on_release:app.change(self)




<about_tin>:

	
	
	RstDocument:
		pos_hint:{"center_x":.5,"center_y":.45}
		size_hint_y:None
		height:"160dp"
		size_hint_x:None
		width:"260dp"
		background_color:(244/255.0,244/255.0,244/255.0,1)


		text:"In this Application is a collection of Ghananian words and phrase which is mostly derived from English language and some indigenous African languages.It also provide the etymology and the pronountiation of the words"


NavigationLayout:



<First_Screen>:

	
	

	
	MDToolbar:
		title:"GH pidgin"
		pos_hint:{"top":1}
		elevation:10
		left_action_items:[["menu",lambda x:nav_draw.set_state("open")]]


	MDBoxLayout:
		pos_hint:{"center_y":.83}
		adaptive_height:True
		MDIconButton:
			icon:"magnify"
			
		MDTextField:
			id:search
			hint_text:"Enter the word to search for"
			on_text:root.searching()
		


		
	MDFloatLayout:

		pos_hint:{"center_x":.0,"center_y":.0}
		size_hint_y:.8
		RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'


	MDNavigationDrawer:
		id:nav_draw
		MDFloatLayout:
			MDRectangleFlatIconButton:
				text:"History"
				icon:"history"
				pos_hint:{"center_x":.5,"center_y":.7}
				size_hint_x:None
				width:250
				on_release:root.manager.current='hist'


			MDRectangleFlatIconButton:
				text:"Settings"
				icon:"settings-outline"
				pos_hint:{"center_x":.5,"center_y":.6}
				size_hint_x:None
				width:250
				on_release:
					app.set()

			MDRectangleFlatIconButton:
				text:"Random word"
				icon:"alpha-t"
				pos_hint:{"center_x":.5,"center_y":.5}
				size_hint_x:None
				width:250
				on_release:app.rand()

			MDRectangleFlatIconButton:
				text:"About"
				icon:"svg"
				pos_hint:{"center_x":.5,"center_y":.4}
				size_hint_x:None
				width:250
				on_release:app.about()

			

		

		

<Second_Screen>:

	MDToolbar:
		title:"GH pidgin"
		pos_hint:{"top":1}
		elevation:10
		left_action_items:[["keyboard-backspace",lambda x:root.move()]]
		right_action_items:[["volume-high",lambda x:root.talk_two()],["content-copy",lambda x:app.copy()]]


	MDFloatLayout:
		


		




		MDLabel:
			text:app.lab
			halign:"center"
			pos_hint:{"center_y":.85}
			theme_text_color:"Custom"
			text_color:0,0,1,1

		BoxLayout:
			padding:dp(10)
			spacing:dp(8)
			pos_hint:{"x":0,"y":0}
			size_hint:1,.8

			orientation:"vertical"

			RstDocument:
				id:ety
				size_hint_y:.3
				
				text:app.text1
				background_color:(244/255.0,244/255.0,244/255.0,1)


			RstDocument:
				id:men
				
				text:app.text2
<cus2>:
	on_release:app.change(self)
	
<Third_Screen>:

	MDToolbar:
		title:"History"
		pos_hint:{"top":1}
		elevation:10	
		left_action_items:[["keyboard-backspace",lambda x:root.back()]]
		right_action_items:[["delete",lambda x:app.delete()]]

	
	BoxLayout:
		size_hint_y:.87
		
		RecycleView:
            data: app.datas
            viewclass: 'cus2'
        	RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                spacing: dp(10)
                padding:dp(10)

""")


class cus(OneLineListItem):pass
	
class cus2(MDRectangleFlatButton):
	pass


class First_Screen(Screen):
	
	def searching(self):
		
		self.ids.rv.data = []
		def excit(wo):

			self.ids.rv.data.append( {"viewclass": "cus",
						"text":words,
						
						}

					)

		
		item=meanings()			
		items=item.explian("keywords")
		
		for words in items:
			
			if self.ids.search.text !="":
				len_text=len(self.ids.search.text)
				len_word=len(words)
				
				if len_text <= len_word:

					getting_word=words[0:len_text]
					if self.ids.search.text == getting_word:
	
						excit(words)

	
	

	
				
	
class about_tin(MDFloatLayout):
	pass


class Second_Screen(Screen):


	def talk_two(self):
		
	
		pass
		

	

	@staticmethod
	def show_toast(message):
		toast(message)

	

	def move(self):
		self.manager.current="first"

	
	
		
class Third_Screen(Screen):
	def back(self):
		self.manager.current="first"
		





class pidginApp(MDApp):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		#Clock.schedule_once(self.onstart, 1)

	

	text1=StringProperty()
	text2=StringProperty()
	lab=StringProperty()
	m=None
	datas=ListProperty()
	
	dialog=None
	dialo=None
	
	def build(self):
		self.ads=KivMob('ca-app-pub-2321607705785649~3660456216')
		self.ads.new_banner("ca-app-pub-2321607705785649/6850313064",top_pos=False)
		self.ads.request_banner()
		self.ads.show_banner()
		self.onstart()
		self.m=ScreenManager(transition=FadeTransition())

		self.m.add_widget(First_Screen(name='first'))
		self.m.add_widget(Second_Screen(name='second'))
		self.m.add_widget(Third_Screen(name='hist'))
		self.m.current="first"


	
		self.theme_cls.primary_palette="Amber"



		
		return self.m

	


	def change(self,tex):
				
		self.m.current="second"
		happy=meanings()

		self.text2=happy.explian(tex.text)
		self.text1=happy.etymology(tex.text)
		self.lab=str(tex.text +":")
		self.datas=[]
		self.adding_search(tex.text)
		self.onstart()
		
	def exc(self,wo):

		
		self.datas.append( {
					"text":wo	
						})
	
		

	def onstart(self):
		it=[]
		store=JsonStore("main.json")
		for items in store.keys():
			making=store.get(str(items))["word"]
			it.append(making)
		n=0
		for j in it:
			n-=1
			self.exc(it[n])


	def set(self):
		pas=MDThemePicker()
		pas.open()

	def about(self):

		btns=MDFlatButton(text="Ok",
			on_release=self.miss
			)

		
		if not self.dialog:
			self.dialog=MDDialog(
				title="About this App",
				width=15,
				type="custom",
				size_hint=[.7,.7],
				auto_dismiss=False,
				content_cls=about_tin(),
				buttons=[btns]
			)

		self.dialog.open()



	def miss(self,obj):
		self.dialog.dismiss()

	class inner(Screen):pass

		
	def rand(self):

		moo=[]
		
		happy=meanings()
		lis=happy.explian("keywords")
		for i in lis:
			moo.append(i)
		my=random.choice(moo)
		self.m.current="second"

		self.text2=happy.explian(my)
		self.text1=happy.etymology(my)
		self.lab=str(my +":")
		self.adding_search(my)
		self.datas=[]
		self.onstart()

	def adding_search(self,searchs):
		store=JsonStore("main.json")
		seach=str(searchs)
		if store.exists(seach):
			store.delete(seach)
			store.put(seach,
				word=seach)
		else:
			store.put(seach,
				word=seach)

		
	def delete_all_search(self,obj):
		
		store=JsonStore("main.json")
		for items in store.keys():
			store.delete(items)
		self.dialo.dismiss()
		
		self.show_toast("Restart the Application to clear all history")
		#self.datas=list()

		

		

		
	

	def copy(self):
		new=self.text2
		if "**" in new:
			new=new.replace("**","")
			Clipboard.copy(str(self.lab+new))

		else:

			Clipboard.copy(str(self.lab+new))

		time.sleep(0.15)
		
		self.show_toast("Text Copied")

	def delete(self):
		if not self.dialo:
			self.dialo=MDDialog(
				title="Clear History",
				text="Are you sure you want to clear all history?",
				width=15,
				size_hint=[.7,.7],
				auto_dismiss=False,
				buttons=[
				MDFlatButton(text="Cancel",
					on_release=self.dis,
					text_color=(0.1,.2,1,1)

					),	

				MDRaisedButton(text="Okay",
					on_release=self.delete_all_search
					)
				]
			)
		self.dialo.open()


	@staticmethod
	def show_toast(message):
		toast(message)

	def dis(self,obj):
		self.dialo.dismiss()
	

if __name__ == '__main__':
	
	pidginApp().run()













