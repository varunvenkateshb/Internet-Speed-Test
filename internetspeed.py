import flet as ft
import speedtest
from time import sleep

def main(page: ft.Page):
    page.title="Internet SpeedTest"
    page.padding=30
    page.window.bgcolor="blue"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.theme_mode="dark"
    page.bgcolor="black"
    page.fonts={
        "SourceCodePro-Bold":"fonts/SourceCodePro-Bold.ttf",
        "SourceCodePro-BoldItalic":"fonts/SourceCodePro-BoldItalic.ttf",
        "RoosterPersonalUse":"fonts/ROOSTER PERSONAL USE.ttf"
    }

    page.auto_scroll = True

    st = speedtest.Speedtest()
    
    #lines 
    line_1=ft.Text("> Press Start...",font_family="SourceCodePro-BoldItalic",color="white")
    line_2=ft.Text("",font_family="SourceCodePro-BoldItalic",color="#1aff1a")
    line_3=ft.Text("",font_family="SourceCodePro-BoldItalic",color="#1aff1a")
    progressBar_1=ft.ProgressBar(width=400,color="#0080ff",bgcolor="#eeeeee",opacity=0)
    progressBar_text_1=ft.Text("   ",font_family="SourceCodePro-BoldItalic",opacity=0)
    progressBar_row_1=ft.Row([progressBar_1,progressBar_text_1])
    line_4=ft.Text("",font_family="SourceCodePro-Bold",color="#ffff00")
    line_5=ft.Text("",font_family="SourceCodePro-BoldItalic",color="#1aff1a")
    progressBar_2=ft.ProgressBar(width=400,color="#0080ff",bgcolor="#eeeeee",opacity=0)
    progressBar_text_2=ft.Text("   ",font_family="SourceCodePro-BoldItalic",opacity=0)
    progressBar_row_2=ft.Row([progressBar_2,progressBar_text_2])
    line_6=ft.Text("",font_family="SourceCodePro-BoldItalic",color="#1aff1a")
    line_7=ft.Text("",font_family="SourceCodePro-Bold",color="#ffff00")
    line_8=ft.Text("",font_family="SourceCodePro-BoldItalic",color="#ffffff")
    terminal_text=ft.Column([line_1,line_2,line_3,progressBar_row_1,line_4,line_5,progressBar_row_2,line_6,line_7,line_8])



    #app title
    appTitle=ft.Row(
        controls=[
        ft.Text("Internet",font_family="RoosterPersonalUse",style="displayLarge",color="red"),
        ft.Text(" Speed",font_family="RoosterPersonalUse",style="displayLarge",color="yellow"),
        ],
        alignment="center"
    )
    # terminal container
    getSpeed = ft.Container(
        content = terminal_text,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut"),
    )

    # terminal animation
    def animate_getSpeed(e):
        progressBar_row_1.opacity = 0
        progressBar_1.opacity = 0
        progressBar_1.value = None
        progressBar_row_2.opacity = 0
        progressBar_2.opacity = 0
        progressBar_2.value = None
        line_1.value = ""
        line_1.update()
        line_2.value = ""
        line_2.update()
        line_3.value = ""
        line_3.update()
        line_4.value = ""
        line_4.update()
        line_5.value = ""
        line_5.update()
        line_6.value = ""
        line_6.update()
        line_7.value = ""
        line_7.update()
        line_8.value = ""
        line_8.update()
        getSpeed.update()
        getSpeed.width = 700
        getSpeed.height = 400
        line_1.value = "> calculating download speed, please wait..."
        getSpeed.update()
        sleep(1)
        line_1.update()
        ideal_server = st.get_best_server() 
        print(ideal_server) # this will find out and connect to the best possible server
        city = ideal_server["name"] # for getting the city name
        country = ideal_server["country"] # for getting the country name
        cc = ideal_server["cc"] # for getting the country code
        line_2.value = f"> finding the best possible servers in {city}, {country} ({cc})"
        line_2.update()
        getSpeed.update()
        sleep(2)
        line_3.value = "> connection established, status OK, fetching download speed"
        line_3.update()
        progressBar_row_1.opacity = 1
        progressBar_1.opacity = 1
        getSpeed.update()
        download_speed = st.download()/1024/1024 # bytes/sec to Mbps
        progressBar_1.value = 1
        line_4.value = f"> the download speed is {str(round(download_speed,2))} Mbps"
        line_4.update()
        getSpeed.update()
        line_5.value = "> calculating upload speed, please wait..."
        line_5.update()
        getSpeed.update()
        sleep(1)
        line_6.value = "> executing upload script, hold on"
        line_6.update()
        progressBar_row_2.opacity = 1
        progressBar_2.opacity = 1
        getSpeed.update()
        upload_speed = st.upload()/1024/1024 # bytes/sec to Mbps
        progressBar_2.value = 1
        line_7.value = f"> the upload speed is {str(round(upload_speed,2))} Mbps"
        line_7.update()
        getSpeed.update()
        sleep(1)
        line_8.value = f"> task completed successfully)"
        line_8.update()
        getSpeed.update()

    # page components
    page.add(
        appTitle,
        getSpeed,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_getSpeed, icon_color="#1aff1a", icon_size=50),
    )

ft.app(target=main,assets_dir="assets")