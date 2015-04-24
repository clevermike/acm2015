#!/usr/bin/env python
# coding:utf-8
#author:dongchen


class CodeMaker:

    def __init__(self, Code):
        self.text = Code.text
        self.team = Code.team.account.username
        self.seat = Code.team.seat_id
        self.fileName = self.team + '_' + unicode(Code.submit_time)
        self.header = self.team + '(' + self.seat + ')' + \
                      '                                                '
        self.pageRow = 55 #根据具体页面情况作调整，这是字体为12时候的

    def make(self):
        self.code_render()
        self.save_file()

    def code_render(self):
        text = self.text.split('\n')
        self.rows = len(text)
        self.pageNum = (self.rows + self.pageRow - 1) / self.pageRow
        self.renderText = ''
        for i in range(1, self.pageNum + 1):
            self.renderText += self.header + 'page:' + str(i) + '/' + str(self.pageNum)
            start = (i - 1) * self.pageRow + 1
            end = self.pageRow * i if self.pageRow * i < self.rows else self.rows
            self.renderText += '\n\n' + str.join('\n',text[start:end]) + '\n'

    def save_file(self):
        try:
            open('static/tasks/'+self.fileName, 'w').write(self.renderText)
        except Exception:
            print Exception

