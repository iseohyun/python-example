### 프로그램 시작시 입력값(옵션) 받아오기 ###

import sys

print(sys.argv[1])

# 입력값(인자, argument)는 사용자가 직접 입력하거나, 다른 프로그램으로부터 받아올 수 있다.

# 전통적으로 입력값(개별)은 argv(Variable), 입력값의 갯수는 argc(Count), 입력값들은 (ARGumentS, args)라는 약어를 사용한다.

# 방법1: 1회 실행한다(오류 무시)  > 콘솔창에서 방향키(↑)를 누른 뒤, 띄어쓰기 후 아무 글자나 적는다.

# 예시: > ....05_Arguments.py Abcde

# 방법2: vscode에서 자동으로 입력값을 설정 할 수 있다. 이는 반복적으로 동일한 입력값을 테스트 할 때 필요하며, 명령줄에서 ">Debug: Add Configuration..."을 통해 세팅값을 추가/변경할 수 있다.

# ctrl + f5: 디버깅 모드로 수행한다. launch.json의 debugpy의 설정을 따른다.

### 예시 ###
# {
#   // Use IntelliSense to learn about possible attributes.
#   // Hover to view descriptions of existing attributes.
#   // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
#   "version": "0.2.0",
#   "configurations": [
    
#     {
#       "name": "Python Debugger: Current File",
#       "type": "debugpy",
#       "request": "launch",
#       "program": "${file}",
#       "console": "integratedTerminal",
#       "args": [
#         "arg1",
#         "arg2"
#       ]
#     }
#   ]
# }