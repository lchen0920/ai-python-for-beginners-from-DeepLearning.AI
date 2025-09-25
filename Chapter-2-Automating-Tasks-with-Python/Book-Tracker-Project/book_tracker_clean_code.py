#!/usr/bin/env python
# coding: utf-8

# # Programming Assignment: Book Tracker 📚 书籍追踪器编程作业

import test_your_code

# <a name='1'></a>
# ## Exercise 1: The Bookworm's Inventory 📖 练习1：书虫的库存

# Initialize book dictionary with required properties 使用所需属性初始化书籍字典
book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "on_shelf": False,
    "borrower": "Arthur Dent",
    "overdue": True,
    "on_hold": False
}

test_your_code.exercise_1(book)

# <a name='2'></a>
# ## Exercise 2: Is It On the Shelf? 🤔 练习2：书在架上吗？

# Check if book is available for borrowing 检查书籍是否可供借阅
if book["on_shelf"] == True and book["on_hold"] == False:
    print("Book is available to be borrowed")
else:
    print("Book is not available to be borrowed")

test_your_code.exercise_2()

# <a name='3'></a>
# ## Exercise 3: On Hold or Overdue? ⏳ 练习3：已预约还是逾期？

# Handle overdue book or place on hold 处理逾期书籍或设置为预约状态
if book["overdue"] == True: 
    print(f"Book is overdue - Contact {book['borrower']} to return it")
else:    
    book["on_hold"] = True
    print("Book has been put on hold")

test_your_code.exercise_3()

# <a name='4'></a>
# ## Exercise 4: Tracking Down the Borrower 🔎 练习4：追踪借书人

# Borrower contact information 借书人联系信息
borrowers_list = [
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@dlailibrary.com",
        "phone": "+1111111111"
    },
    {
        "name": "Bob Smith",
        "email": "bob.smith@dlailibrary.com",
        "phone": "+2222222222"
    },
    {
        "name": "Arthur Dent",
        "email": "arthur.dent@dlailibrary.com",
        "phone": "+3333333333"
    },
    {
        "name": "Diana Prince",
        "email": "diana.prince@dlailibrary.com",
        "phone": "+4444444444"
    }
]

# Find borrower's email in the list 在列表中查找借书人的邮箱
for borrower in borrowers_list:
    if book['borrower'] == borrower['name']:
        borrower_email = borrower['email']

print(f"{book['borrower']}'s email is: {borrower_email}")

test_your_code.exercise_4(borrower_email)

# <a name='5'></a>
# ## Exercise 5: The LLM to the Rescue! 🤖 练习5：LLM来帮忙！

# Prepare data for LLM prompt 为LLM提示准备数据
person_name = book['borrower']
book_name = book['title']
book_author = book['author']
due_date = "16 November 2024"

# Create prompt for email generation 创建用于生成邮件的提示
prompt = f"""
Please write a polite email to {person_name}, reminding them to return the book {book_name} by {book_author}.  The book was due on {due_date}.
"""

print(prompt)

test_your_code.exercise_5(prompt)

# Optional: Generate LLM response 可选：生成LLM响应
from helper_functions import get_llm_response

print(get_llm_response(prompt))
