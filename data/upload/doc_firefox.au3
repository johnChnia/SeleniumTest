; Wait 10 seconds for the Upload window to appear

  WinWait("[CLASS:#32770]","",10)

; Set input focus to the edit control of Upload window using the handle returned by WinWait

  ControlFocus("文件上传","","Edit1")

  Sleep(2000)

; Set the File name text on the Edit field

  ControlSetText("文件上传", "", "Edit1", "E:\python_resources\code\test_zentao\data\upload\a.doc")

  Sleep(2000)

; Click on the Open button

  ControlClick("文件上传", "","Button1");