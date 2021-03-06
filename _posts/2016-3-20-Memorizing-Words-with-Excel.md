---
layout: post
title: Memorizing words with Excel
---
使用Excel背单词的一些设置以及一些注意点。(因为装的是中文版Office所以就用中文写了) <br/>
[王陆语料库横向练习C3T1-C3T5](/attachments/160320-corpus.xlsx?raw=true "王陆语料库")

# 目的
背单词有三种：1.看到英文能想起释义，2.听到英文能写出单词，3.看到释义能写出单词。而本方法适用于后两种。主要价值在于，让电脑自动帮你判断写出来的单词是否正确。

# 效果
如图所示 <br/>
![最终效果](/images/160320-demo.png "最终效果") <br/>
测试时，可以隐藏B列和D列，在C列中打出拼写，A列会自动判断拼写结果。


# 设置方法 [MS Office]

## 输入公式
在A2中输入公式: `=IF(C2="","空",IF(B2:B200=C2:C200,"正确","错误"))` <br/>
然后选中A2，把鼠标移动到右下角的实心点处，当鼠标变为黑色十字时，按住并向下拖动，扩充到你需要的范围。

## 设置错误为红色提示
如下图所示，使用条件格式实现此功能。
![条件格式-新建规则](/images/160320-conditional-format-new.png "条件格式-新建规则")
![条件格式-特殊文本](/images/160320-conditional-format-text.png "条件格式-特殊文本")
(如果有大神会使用公式确定的方法，请一定告诉我)

## __关闭自动提示与拼写纠正__
这是很重要的一点，因为我们是要训练拼写，所以需要关掉这两个功能。
![文件-选项](/images/160320-options.png "文件-选项")
![校对-自动更正](/images/160320-autocorrect.png "校对-自动更正")
![高级-记忆式键入](/images/160320-auto-complete.png "高级-记忆式键入")

## 强烈建议更改字体
默认的宋体显示英文简直不能看，强烈建议选择BC两列，并把字体设置为"Times New Roman"等英文字体。

# 使用
第一次需要把正确的英文输入B列中，一列一个，建议释义可以先不用写。根据录音听写前先选中B列，设置字体颜色为白色，这样就达到了隐藏的效果，然后就可以听录音做听写了。对于错的比较多的单词再补充它的释义上去。

# 设置 [LibreOffice]

```
Tools -> AutoCorrect Options -> Replacements and exceptions for language: [All] 
Tools -> Cell Contents -> AutoInput.
```


