#!/usr/bin/env python
# coding: utf-8

"""
Virtual Library System - Python Assignment
虚拟图书馆系统 - Python作业
Optimized version with bilingual comments 中英文注释优化版
"""

import test_your_code

# ===== Exercise 1: Book Information 练习1: 书籍信息 =====
# Define variables for "Brave New World" book information 定义《美丽新世界》书籍信息变量
book_title = "Brave New World"
author = "Aldous Huxley" 
year_published = 1932
available_copies = 4

# Test variable definitions 测试变量定义
test_your_code.exercise_1a(book_title, author, year_published, available_copies)

# Print book information 打印书籍信息
print(f"Title: {book_title}")
print(f"Author: {author}") 
print(f"Published: {year_published}")
print(f"Available Copies: {available_copies}")

# Test print functionality 测试打印功能
test_your_code.exercise_1b()

# ===== Exercise 2: Checking Out a Book 练习2: 借出书籍 =====
# Reduce available copies (simulate book checkout) 减少可用副本数量（模拟借书）
available_copies = available_copies - 1

# Print checkout confirmation 打印借书确认信息
print(f"""
One copy of {book_title} checked out. There are now {available_copies} copies available.
""")

# Test checkout logic 测试借书逻辑
test_your_code.exercise_2(available_copies)

# ===== Exercise 3: Book Request 练习3: 书籍请求 =====  
# Handle request for unavailable book 处理缺书籍的请求
requested_book = "To Kill a Mockingbird"
print(f"""{requested_book} is currently unavailable. You can request it from the library.""")

# Test request functionality 测试请求功能
test_your_code.exercise_3(requested_book)
