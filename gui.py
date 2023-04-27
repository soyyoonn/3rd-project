import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("UI초안.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.first = False

        # 시작화면 고정
        self.stackedWidget.setCurrentIndex(2)

        # 초기화면 : 입장하기 버튼 누를시 chatbot 함수 실행
        self.go_btn.clicked.connect(self.chatbot)

        # chatbot화면
        # 종료버튼 누를시 finish 함수 실행
        self.exit_btn.clicked.connect(self.finish)
        # 전송버튼 누를시 send_data 함수 실행
        self.send_btn.clicked.connect(self.send_data)
        # 엔터키 눌렀을 때 send_data 함수 실행
        self.lineEdit.returnPressed.connect(self.send_data)

        # 종료화면 : 대화종료 후 각각의 감정버튼 눌렀을 떄
        self.happy_btn.clicked.connect(self.happy)
        self.sad_btn.clicked.connect(self.sad)
        self.pleasure_btn.clicked.connect(self.pleasure)
        self.depressed_btn.clicked.connect(self.depressed)

        self.setWindowTitle("AI 챗봇")

    # chatbot 화면 실행
    def chatbot(self):
        self.stackedWidget.setCurrentIndex(0)
        # 사용자가 감정을 선택할 수 있도록 하기
        self.textBrowser.setAlignment(Qt.AlignLeft)
        self.textBrowser.append(f"🤖 : 현재 느끼는 감정의 번호를 입력해주세요\n\n       1.행복  2.슬픔  3.기쁨  4.우울\n")
        self.first = True

    # 전송버튼 눌렀을 때, 입력한 내용 텍스트 브라우저에 띄움
    def send_data(self):
        # 감정 번호 입력시 답변 정리
        if self.first == True:
            text = self.lineEdit.text()
            self.textBrowser.setAlignment(Qt.AlignRight)
            self.textBrowser.append(f" {text} : 😀\n")

            # 감정 번호 입력했을시 답변, DB에 저장해야함.
            if text == '1':
                self.textBrowser.setAlignment(Qt.AlignLeft)
                self.textBrowser.append(f"🤖 : 저도 함께 행복할 수 있을까요? 당신의 이야기가 듣고싶어요😁\n")

            elif text == '2':
                self.textBrowser.setAlignment(Qt.AlignLeft)
                self.textBrowser.append(f"🤖 : 슬픔은 나누면 반이되요! 당신의 슬픔을 함께 나눌 수 있을까요?\n")

            elif text == '3':
                self.textBrowser.setAlignment(Qt.AlignLeft)
                self.textBrowser.append(f"🤖 : 기분이 굉장히 좋아보이시네요! 저에게도 이야기해주실래요?\n")

            elif text == '4':
                self.textBrowser.setAlignment(Qt.AlignLeft)
                self.textBrowser.append(f"🤖 : 많이 힘드셨나봐요😭\n")

            self.lineEdit.clear()
            self.first = False

        # 그 이후 대화이어가기(AI 넣기)
        else :
            text = self.lineEdit.text()
            self.textBrowser.setAlignment(Qt.AlignRight)
            self.textBrowser.append(f" {text} : 😀\n")
            self.lineEdit.clear()


    # 대화후 감정 상태 누를수 있는 화면이동
    def finish(self):
        self.stackedWidget.setCurrentIndex(1)

    # 각 버튼 눌렀을 때 DB에 저장해야함.
    # 1. 행복버튼 눌렀을 때
    def happy(self):
        QMessageBox.information(self, "알림","AI 챗봇과의 대화 후 당신의 감정은 '행복'입니다.\nAI 챗봇을 이용해주셔서 감사합니다.",QMessageBox.Close)
        QCoreApplication.instance().quit()

    # 2. 슬픔버튼 눌렀을 때
    def sad(self):
        QMessageBox.information(self, "알림", "AI 챗봇과의 대화 후 당신의 감정은 '슬픔'입니다.\nAI 챗봇을 이용해주셔서 감사합니다.")
        QCoreApplication.instance().quit()

    # 3. 기쁨버튼 눌렀을 때
    def pleasure(self):
        QMessageBox.information(self, "알림", "AI 챗봇과의 대화 후 당신의 감정은 '기쁨'입니다.\nAI 챗봇을 이용해주셔서 감사합니다.")
        QCoreApplication.instance().quit()

    # 4. 우울버튼 눌렀을 때
    def depressed(self):
        QMessageBox.information(self, "알림", "AI 챗봇과의 대화 후 당신의 감정은 '우울'입니다.\nAI 챗봇을 이용해주셔서 감사합니다.")
        QCoreApplication.instance().quit()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()