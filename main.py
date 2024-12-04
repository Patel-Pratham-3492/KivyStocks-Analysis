import sqlite3
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup

screen_helper = """

ScreenManager:
    LoginScreen:
    ForgotScreen:
    CreateScreen:
	MainScreen:


<LoginScreen>:
    name: 'login'
	MDLabel:
		text: 'Welcome'
		font_style : 'H3'
		pos_hint : {'x':0.1,'y':0.4}
		size_hint_x:  None
		width : 200
		
	MDLabel:
		text:'to'
		font_style : 'H4'
		pos_hint : {'x':0.4,'y':0.3}
		size_hint_x: None
		width : 200
		
	MDLabel:
		text: 'Stock'
		font_style : 'H2'
		pos_hint : {'x':0.5,'y':0.2}
		color : 1,0,0,1
		bold : True
		size_hint_x:  None
		width : 200
		
	MDLabel:
		text: 'Advicer'
		font_style : 'H2'
		pos_hint : {'x':0.7,'y':0.2}
		color : 0,100/255.0,100/255.0,1
		bold : True
		size_hint_x:None
		width : 200
				
	MDTextField:
		id : user1
		name : 'username'
		hint_text: "Enter Email"
		color_mode: 'custom'
		line_color_focus: 1, 0, 0, 1
		helper_text: "or click on forgot button"
		helper_text_mode: "on_focus"
		icon_right: "account-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.45}
		size_hint_x:None
		width:300
	
	MDTextField:
		id : pass1
		name : 'password'
		password : True
		hint_text: "Enter Password"
		color_mode: 'custom'
		line_color_focus: 0,100/255.0,100/255.0,1
		helper_text: "or click on forgot button"
		helper_text_mode: "on_focus"
		icon_right: "eye-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.35}
		size_hint_x:None
		width:300
		
	MDRectangleFlatButton:
        text: 'Create'
        pos_hint: {'x':0.34,'y':0.25}
		theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
        on_press: root.manager.current = 'create'
        
    MDRectangleFlatButton:
        text: 'Login'
		theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
        pos_hint: {'x':0.44,'y':0.25}
		on_release: app.checkin(user1.text,pass1.text)
        
        
	MDRectangleFlatButton:
		text: 'Forgot'
		theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
		pos_hint: {'x':0.535,'y':0.25}
		on_press: root.manager.current = 'forgot'
		
	MDIconButton:
		icon: 'exit-to-app'
		on_release : app.exit()
		pos_hint : {'x':0.9,'y':0.05}
		
		
    
    
    
<ForgotScreen>:
    name: 'forgot'
    
	MDLabel:
		text: 'Enter'
		font_style : 'H3'
		pos_hint : {'x':0.1,'y':0.4}
		size_hint_x:  None
		width : 200
	
	MDLabel:
		text:'Your'
		font_style : 'H4'
		pos_hint : {'x':0.25,'y':0.3}
		color : 1,0,0,1
		bold : True
		size_hint_x: None
		width : 200
		
	MDLabel:
		text: 'Email'
		font_style : 'H2'
		pos_hint : {'x':0.35,'y':0.2}
		color : 0,100/255.0,100/255.0,1
		bold : True
		size_hint_x:  None
		width : 200
		
	MDTextField:
		id : userforgot
		name : 'username1'
		hint_text: "Enter Email"
		color_mode: 'custom'
		line_color_focus: 1, 0, 0, 1
		helper_text: "Enter your exist Email"
		helper_text_mode: "on_focus"
		icon_right: "account-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.45}
		size_hint_x:None
		width:300
		
	MDTextField:
		id : passforgot
		name : 'password1'
		password : True
		hint_text: "Enter Password"
		color_mode: 'custom'
		min_text_length: 6
		max_text_length: 20
		line_color_focus: 0,100/255.0,100/255.0,1
		helper_text: "Enter New Password"
		helper_text_mode: "on_focus"
		icon_right: "eye-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.35}
		size_hint_x:None
		width:300
		
	MDTextField:
		id : passforgot2
		name : 'password2'
		password : True
		hint_text: "Re-Enter Password"
		color_mode: 'custom'
		min_text_length: 6
		max_text_length: 20
		line_color_focus: 75/255.0 , 0/255.0 , 130/255.0,1
		helper_text: "please conform your Password"
		helper_text_mode: "on_focus"
		icon_right: "eye-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.25}
		size_hint_x:None
		width:300
		
	MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'x':0.39,'y':0.15}
		theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
        on_release: app.submit(userforgot.text,passforgot.text,passforgot2.text)
        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.53,'center_y':0.18}
        theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
        on_press: root.manager.current = 'login'
        
        
        
        
        
        
<CreateScreen>:
    name: 'create'
    
    MDLabel:
		text: 'Create'
		font_style : 'H3'
		pos_hint : {'x':0.1,'y':0.4}
		size_hint_x:  None
		width : 200
	
	MDLabel:
		text:'Your'
		font_style : 'H4'
		pos_hint : {'x':0.29,'y':0.3}
		color : 1,0,0,1
		bold : True
		size_hint_x: None
		width : 200
		
	MDLabel:
		text: 'Account'
		font_style : 'H2'
		pos_hint : {'x':0.39,'y':0.2}
		color : 0,100/255.0,100/255.0,1
		bold : True
		size_hint_x:  None
		width : 300
	
	MDTextField:
		id : usercreate
		name : 'usercreate1'
		hint_text: "Enter Email"
		color_mode: 'custom'
		line_color_focus: 1, 0, 0, 1
		helper_text: "Enter your exist Email"
		helper_text_mode: "on_focus"
		icon_right: "account-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.45}
		size_hint_x:None
		width:300
		
	MDTextField:
		id : passcreate1
		name : 'passcreate1'
		password : True
		hint_text: "Create New Password"
		color_mode: 'custom'
		min_text_length: 6
		max_text_length: 20
		line_color_focus: 0,100/255.0,100/255.0,1
		helper_text: "Enter New Password"
		helper_text_mode: "on_focus"
		icon_right: "eye-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.35}
		size_hint_x:None
		width:300
		
	MDTextField:
		id : passcreate2
		name : 'passcreate2'
		password : True
		hint_text: "Re-Enter Password"
		color_mode: 'custom'
		min_text_length: 6
		max_text_length: 20
		line_color_focus: 75/255.0 , 0/255.0 , 130/255.0,1
		helper_text: "please conform your Password"
		helper_text_mode: "on_focus"
		icon_right: "eye-lock"
		icon_right_color: app.theme_cls.primary_color
		pos_hint:{'x': 0.3, 'y': 0.25}
		size_hint_x:None
		width:300
        
    MDRectangleFlatButton:
        text: 'Create'
        pos_hint: {'x':0.39,'y':0.15}
		theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
        on_release: app.create(usercreate.text,passcreate1.text,passcreate2.text)
        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.53,'center_y':0.18}
        theme_text_color: "Custom"
		line_color: "black"
		text_color: "black"
        on_press: root.manager.current = 'login'
        
        
        
        
<MainScreen>:
	name : 'main'
		
	GridLayout:
		cols: 3  # Only one column
		rows: 2  # Only one row
		spacing : dp(10)
		size_hint: None, None  # Disable automatic size hint
		size: dp(750), dp(550)  # Set specific size
    
		pos_hint : {'x':0.03,'y':0.04}
    
		canvas.before:
			Color:
				rgba: 0.7, 0.7, 0.7, 1  # Grey color in RGBA format
			Rectangle:
				pos: self.pos
				size: self.size
            
			Color:
				rgba: 1, 1, 1, 1  # White color in RGBA format
        		# Draw borders between cells and between columns and rows
			Line:
				points: [self.x, self.y, self.x + self.width, self.y, self.x + self.width, self.y + self.height, self.x, self.y + self.height, self.x, self.y]
				width: 3  # Border width
			Line:
				points: [self.x + self.width / 3, self.y, self.x + self.width / 3, self.y + self.height]
				width: 3  # Border width
			Line:
				points: [self.x + 2 * self.width / 3, self.y, self.x + 2 * self.width / 3, self.y + self.height]
            	width: 3  # Border width
        	Line:
            	points: [self.x, self.y + self.height / 2, self.x + self.width, self.y + self.height / 2]
            	width: 3  # Border width

		MDFloatLayout:
        	orientation: 'horizontal'
        	padding: dp(10)
        	AsyncImage:
            	source: 'https://companiesmarketcap.com/img/company-logos/256/TSLA.webp'  # Replace with the actual path to your image
            	size_hint: None, None
            	size: self.parent.width, self.parent.height * 0.4  # Image takes 75% of the cell height
            	pos_hint : {'x': 0.0,'y': 0.55}
        
        	MDLabel:
            	text: 'Country : USA'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.37}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
            	text: 'World Rank : #9'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.29}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
				id: label_id0
            	text: 'Share Price : $242.65'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.21}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height   
             
			MDLabel:
            	text: 'Market Cap : $769.07B'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.13}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDRaisedButton:
				text: 'view'
            	size_hint: None, None
            	size: self.parent.width * 0.8, self.parent.height * 0.2  # Button takes 20% of the cell height
            	pos_hint: {'x': 0.38,'y': 0.03}
            	md_bg_color: '000000'  # Set button color to black
            	text_color: (1, 1, 1, 1)  # Set text color to white  
            
		MDFloatLayout:
        	orientation: 'vertical'
        	padding: dp(10)
        	AsyncImage:
            	source: 'https://companiesmarketcap.com/img/company-logos/256/HPQ.webp'  # Replace with the actual path to your image
            	size_hint: None, None
            	size: self.parent.width, self.parent.height * 0.4  # Image takes 75% of the cell height
            	pos_hint : {'x': 0.0,'y': 0.55}
        
        	MDLabel:
            	text: 'Country : USA'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.37}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
            	text: 'World Rank : #568'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.29}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
				id: label_id1
            	text: 'Share Price : $32.77'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.21}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height   
             
			MDLabel:
            	text: 'Market Cap : $32.30B'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.13}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDRaisedButton:
				text: 'view'
            	size_hint: None, None
            	size: self.parent.width * 0.8, self.parent.height * 0.2  # Button takes 20% of the cell height
            	pos_hint: {'x': 0.38,'y': 0.03}
            	md_bg_color: '000000'  # Set button color to black
            	text_color: (1, 1, 1, 1)  # Set text color to white   
            
            
		MDFloatLayout:
        	orientation: 'vertical'
        	padding: dp(10)
        	AsyncImage:
            	source: 'https://companiesmarketcap.com/img/company-logos/256/IBM.webp'  # Replace with the actual path to your image
            	size_hint: None, None
            	size: self.parent.width, self.parent.height * 0.4 # Image takes 75% of the cell height
            	pos_hint : {'x': 0.0,'y': 0.55}
        
        	MDLabel:
            	text: 'Country : USA'
            	halign: 'center'
            	valign: 'middle'
				size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.37}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
            	text: 'World Rank : #96'
            	halign: 'center'
            	valign: 'middle'
				size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.29}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
				id: label_id2
            	text: 'Share Price : $143.12'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.21}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height   
             
			MDLabel:
            	text: 'Market Cap : $130.38B'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.13}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDRaisedButton:
				text: 'view'
            	size_hint: None, None
            	size: self.parent.width * 0.8, self.parent.height * 0.2  # Button takes 20% of the cell height
            	pos_hint: {'x': 0.38,'y': 0.03}
            	md_bg_color: '000000'  # Set button color to black
            	text_color: (1, 1, 1, 1)  # Set text color to white 

		MDFloatLayout:
        	orientation: 'vertical'
        	padding: dp(10)
        	AsyncImage:
				source: 'https://companiesmarketcap.com/img/company-logos/256/AMZN.webp'  # Replace with the actual path to your image
            	size_hint: None, None
            	size: self.parent.width, self.parent.height * 0.4  # Image takes 75% of the cell height
            	pos_hint : {'x': 0.0,'y': 0.55}
        
        	MDLabel:
            	text: 'Country : USA'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.37}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
            	text: 'World Rank : #5'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.29}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
				id: label_id3
            	text: 'Share Price : $138.41'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.21}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height   
             
			MDLabel:
            	text: 'Market Cap : $1.420T'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.13}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDRaisedButton:
				text: 'view'
            	size_hint: None, None
            	size: self.parent.width * 0.8, self.parent.height * 0.2  # Button takes 20% of the cell height
            	pos_hint: {'x': 0.38,'y': 0.03}
            	md_bg_color: '000000'  # Set button color to black
            	text_color: (1, 1, 1, 1)  # Set text color to white 
	
		MDFloatLayout:
        	orientation: 'vertical'
        	padding: dp(10)
        	AsyncImage:
        		source: 'https://companiesmarketcap.com/img/company-logos/256/INTC.webp'  # Replace with the actual path to your image
            	size_hint: None, None
            	size: self.parent.width, self.parent.height * 0.4  # Image takes 75% of the cell height
            	pos_hint : {'x': 0.0,'y': 0.55}
        
        	MDLabel:
            	text: 'Country : USA'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.37}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
            	text: 'World Rank : #80'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.29}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
				id: label_id4
            	text: 'Share Price : $34.89'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.21}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height   
             
			MDLabel:
            	text: 'Market Cap : $146.07B'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.13}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDRaisedButton:
				text: 'view'
            	size_hint: None, None
            	size: self.parent.width * 0.8, self.parent.height * 0.2  # Button takes 20% of the cell height
            	pos_hint: {'x': 0.38,'y': 0.03}
            	md_bg_color: '000000'  # Set button color to black
            	text_color: (1, 1, 1, 1)  # Set text color to white 
            
		MDFloatLayout:
        	orientation: 'vertical'
        	padding: dp(10)
        	AsyncImage:
            	source: 'https://companiesmarketcap.com/img/company-logos/256/AAPL.webp'  # Replace with the actual path to your image
            	size_hint: None, None
            	size: self.parent.width, self.parent.height * 0.4  # Image takes 75% of the cell height
            	pos_hint : {'x': 0.0,'y': 0.55}
        
        	MDLabel:
            	text: 'Country : USA'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.37}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
            	text: 'World Rank : #1'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.29}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDLabel:
				id: label_id5
            	text: 'Share Price : $177.79'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.21}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height   
             
			MDLabel:
            	text: 'Market Cap : $2.796T'
            	halign: 'center'
            	valign: 'middle'
            	size_hint: None, None
            	pos_hint : {'x': 0.0,'y': 0.13}
            	size: self.parent.width, self.parent.height * 0.2  # Label takes 25% of the cell height
            
			MDRaisedButton:
				text: 'view'
            	size_hint: None, None
            	size: self.parent.width * 0.8, self.parent.height * 0.2  # Button takes 20% of the cell height
            	pos_hint: {'x': 0.38,'y': 0.03}
            	md_bg_color: '000000'  # Set button color to black
            	text_color: (1, 1, 1, 1)  # Set text color to white

	MDIconButton:
		icon: 'arrow-left'
		on_press: root.manager.current = 'login'
		pos_hint : {'x': -0.01,'y':0.93}
		
	MDIconButton:
		icon: 'reload'
		on_release: app.reload()
		pos_hint : {'x': 0.9,'y':0.93}
	
        
"""


class LoginScreen(Screen):
	pass
			
class ForgotScreen(Screen):
    pass

class CreateScreen(Screen):
    pass

class MainScreen(Screen):
	pass

class DemoApp(MDApp):
	def build(self):
		conn = sqlite3.connect('your_database.db')
		cursor = conn.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='my_data'")
		table_exists = cursor.fetchone()
		
		if not table_exists:
			cursor.execute("CREATE TABLE my_data (email TEXT,password TEXT)")
			conn.commit()
		else:
			conn.commit()
			conn.close()
					
		urlli = ['https://companiesmarketcap.com/tesla/revenue/','https://companiesmarketcap.com/hp/revenue/','https://companiesmarketcap.com/ibm/revenue/','https://companiesmarketcap.com/amazon/revenue/','https://companiesmarketcap.com/intel/revenue/','https://companiesmarketcap.com/apple/revenue/']
		
		
		self.screen = Builder.load_string(screen_helper)
		self.sm = ScreenManager()
		self.sm.add_widget(LoginScreen(name = 'login'))
		self.sm.add_widget(ForgotScreen(name = 'forgot'))
		self.sm.add_widget(CreateScreen(name = 'create'))
		self.sm.add_widget(MainScreen(name = 'main'))
		return self.screen
		
	def reload(self):
		main_screen = self.root.get_screen('main')
		urlli = ['https://companiesmarketcap.com/tesla/revenue/','https://companiesmarketcap.com/hp/revenue/','https://companiesmarketcap.com/ibm/revenue/','https://companiesmarketcap.com/amazon/revenue/','https://companiesmarketcap.com/intel/revenue/','https://companiesmarketcap.com/apple/revenue/']
		for i in range(0,6):
			url = urlli[i]
			html_data = requests.get(url).text
			soup = BeautifulSoup(html_data,"html5lib")
			div_elements = soup.find_all("div", class_="line1")
			h = div_elements[3].text
			label = main_screen.ids[f"label_id{i}"]
			label.text = 'Share Price : ' + h
				
	def create(self,A,B,C):       #This is for CREATE Page 
		create_btn = MDFlatButton(text = 'OK', md_bg_color=(0, 1, 0, 1) ,on_release = self.close)
		conn = sqlite3.connect('your_database.db')
		cursor = conn.cursor()
		if(A =="" or B =="" or C ==""):
			self.dialog_create = MDDialog(text = 'please insert the data', buttons = [create_btn], title = "Your New Account:", 
											size_hint = (0.5,0.7))
			self.dialog_create.open()
		else:
			if(B == C):
				insert_query = "INSERT INTO my_data (email,password) VALUES (?, ?)"
				cursor.execute(insert_query, (A,B))
				conn.commit()
				conn.close()
				self.dialog_create = MDDialog(text = 'your Account is created successfully', buttons = [create_btn], title = "Your New Account:", 
												size_hint = (0.5,0.7))
				self.dialog_create.open()
			else:
				self.dialog_create = MDDialog(text = 'your created password is not equal to conform password, please try again ', buttons = [create_btn], 
												title = "Your New Account:",size_hint = (0.5,0.7))
				self.dialog_create.open()
			
	def close(self,instance):    #This is for CREATE page
		self.dialog_create.dismiss()

			
	def submit(self, A1, B1, C1):  # This is for the FORGOT page
		btn2 = MDFlatButton(text='OK', on_release=self.close_dialog1, md_bg_color=(0, 1, 0, 1))
		conn = sqlite3.connect('your_database.db')
		cursor = conn.cursor()

		self.A = "SELECT email FROM my_data"
		cursor.execute(self.A)
		self.user = cursor.fetchall()

		conn.commit()

		if A1 == "" or B1 == "" or C1 == "":
			self.dialog1 = MDDialog(text='please insert the data',buttons=[btn2],title="Your new password:",size_hint=(0.5, 0.7))
			self.dialog1.open()
			conn.close()
		else:
			email_found = False
			for i in self.user:
				if A1 in i:
					print("user is present")
					email_found = True
					if B1 == C1:
						self.update_query = "UPDATE my_data SET password = ? where email = ?"
						cursor.execute(self.update_query, (B1, A1))
						conn.commit()
						conn.close()
						self.dialog1 = MDDialog(text=A1 + ', your new password is submitted',buttons=[btn2],title="Your new Password:",size_hint=(0.5, 0.7))
						self.dialog1.open()
					else:
						self.dialog1 = MDDialog(text=A1 + ', your new password is not matched with the confirm password',buttons=[btn2],title="Your new password:",
												size_hint=(0.5, 0.7))
						self.dialog1.open()
						conn.close()
					break  # Exit the loop if the email is found
			if not email_found:
				self.dialog1 = MDDialog(text=A1 + ', Please check your Email',buttons=[btn2],title="Your new Password:",size_hint=(0.5, 0.7))
				self.dialog1.open()
				conn.close()

	def close_dialog1(self, instance):  # This is for the FORGOT page
		self.dialog1.dismiss()

	def checkin(self,text,text1):      # This is for LOGIN Page 
		btn1 = MDFlatButton(text = 'Close', on_release = self.close_dialog, md_bg_color=(1, 0, 0, 1) )
		conn = sqlite3.connect('your_database.db')
		cursor = conn.cursor()
		
		self.A = "SELECT email FROM my_data"
		cursor.execute(self.A)
		self.user = cursor.fetchall()
		
		self.B = "SELECT password FROM my_data"
		cursor.execute(self.B)
		self.password = cursor.fetchall()
		
		conn.commit()
		conn.close()
		
		if text == "" or text1 == "":
			self.dialog = MDDialog(text='please insert the data',buttons=[btn1],title="Login Error:",size_hint=(0.5, 0.7))
			self.dialog.open()
		else:
			self.p = False
			self.e = False
			for i in self.user:
				if(text in i):
					self.e = True
					print(text)
					for j in self.password:
						if(text1  in j):
							print(text1)
							self.p = True
							break
				if self.p:
					self.root.current = "main"
					break
					
			if not self.p:
				self.dialog  = MDDialog(text = "please check the email and password", buttons = [btn1],
											title = 'email and Password Check',size_hint = (0.5,0.7) )
				self.dialog.open()
	
	def close_dialog(self,instance):  # This is for LOGIN page
		self.dialog.dismiss()
		
	def exit(self):
		self.stop()
	
				

DemoApp().run()
