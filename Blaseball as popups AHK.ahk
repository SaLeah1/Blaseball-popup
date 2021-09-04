sleep, 10000
loop, read, C:\Users\tempo\PycharmProjects\pythonProject\windowsvista.txt
{
	MsgBox, , PLAY BLALL,%A_LoopReadLine%
	sleep, 3000
}
return