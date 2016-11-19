import webbrowser
import time

total_breaks=3
count=0
while(count<total_breaks):
	time.sleep(5)				# time should ideally be approx 3 hours
	print("Please take some timeout to see your favorite video")
	time.sleep(2)
	webbrowser.open("https://www.youtube.com/watch?v=Jwgf3wmiA04")
	count+=1
