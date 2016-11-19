import webbrowser
import time

i=0
while(i<=2):
	time.sleep(5)				# time should ideally be approx 3 hours
	print("Please take some timeout to see your favorite video")
	time.sleep(2)
	webbrowser.open("https://www.youtube.com/watch?v=Jwgf3wmiA04")
	i+=1
