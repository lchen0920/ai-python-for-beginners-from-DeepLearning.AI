#!/usr/bin/env python
# coding: utf-8

# # Programming Assignment: Book Tracker 📚
# 
# Welcome to the programing assignment of the second module of this course! 
# 
# Get ready to put your Python skills to the test. In this assignment, you'll be a librarian, managing the book records. Let's get started! 🚀

# ## Before you begin 🚦

# If you **need a fresh copy of the assignment (reset)**, follow the [instructions](https://www.coursera.org/learn/ai-python-for-beginners/supplement/uW6bd/optional-downloading-your-notebook-downloading-your-workspace-and-refreshing) under the heading, "`Refreshing your Workspace`".
# 
# <h2 style="color:green; font-weight:bold;">INSTRUCTIONS FOR ATTEMPTING THE ASSIGNMENT:</h2>
# 
# - Before starting each exercise, read the instructions carefully. Look for the part called **Your Task**, it tells you exactly what you need to code and gives you all the details you need.
# 
# 
# - In each exercise cell, look for comments `### START CODE HERE ###` and `### END CODE HERE ###`. These show you where to write your code. **Do not add or change any code that is outside these comments, or add any extra code cells in the notebook.**
# 
# 
# - After you finish coding an exercise, there will be a test section that checks your work using a function called `test_your_code`. If everything is correct, you'll see a message saying "<span style="color: green;">All tests passed!</span>" and you can move on. <span style="color: red;">If there's a mistake, you'll see a red message explaining what went wrong, so you can fix it.</span>
# 
# 
# - **Before submitting your notebook for grading, ensure ALL exercises are complete (gotten All tests passed! for all of them)**. Save your work by clicking the 💾 icon at the top left, then click the <span style="color: blue; font-weight: bold;">Submit assignment</span> button at the top right.
# 
# <h2 style="color:green; font-weight:bold;">ASKING FOR HELP IN THE COMMUNITY FORUM:</h2>
# 
# - Sign up for our [Community Forum](https://www.coursera.org/learn/ai-python-for-beginners/supplement/No2f2/important-have-questions-issues-or-ideas-join-our-forum) if you haven't already. Once signed up, post your questions in the [AP4B category](https://community.deeplearning.ai/c/course-q-a/ai-python-for-beginners/463) with detailed information, such as the item's name, exercise number, or code cell. This helps others understand your issue better. Share screenshots if you can, but **don't post solution code publicly**; instead, share the error message you receive.
# 
# With that out of the way, let's begin!

# ## Table of Exercises
# 
# - [Exercise 1: The Bookworm's Inventory 📖](#1)
# - [Exercise 2: Is It On the Shelf? 🤔](#2)
# - [Exercise 3: On Hold or Overdue? ⏳](#3)
# - [Exercise 4: Tracking Down the Borrower 🔎](#4)
# - [Exercise 5: The LLM to the Rescue! 🤖](#5)

# ### Assignment Starts From Here
# 
# Before starting the assignment, run the cell below. It will bring in some helpful code to check if your solutions are correct and provide feedback if you need to make changes. You'll learn more about how this works as you progress through the course.
# 
# **IMPORTANT NOTE**:  Always run this cell when starting or resuming your assignment. **DO NOT include it in any other notebook cells.**

# In[1]:


import test_your_code


# <a name='1'></a>
# ## Exercise 1: The Bookworm's Inventory 📖
# 
# Imagine you're a librarian, and a request just came in for the classic novel "To Kill a Mockingbird". 🐦  Before you can tell the eager reader if it's available, you need to check your records.
# 
# You first need to represent a book's information using a Python dictionary. This dictionary will store the following details about the book:
# 
# - `title` (string): The title of the book.
# - `author` (string): The author of the book.
# - `on_shelf` (boolean): Whether the book is currently on the shelf (`True`) or checked out (`False`).
# - `borrower` (string): The name of the person who has borrowed the book (if it's checked out).
# - `overdue` (boolean): Whether the book is overdue (`True`) or not (`False`).
# - `on_hold` (boolean): Whether the book is on hold for another patron (`True`) or not (`False`).
# 
# 
# **Your Task:** Initialize the dictionary `book` with the following key/value pairs:
# 
# - `title`: To Kill a Mockingbird
# - `author`: Harper Lee
# - `on_shelf`: False
# - `borrower`: Arthur Dent
# - `overdue`: True
# - `on_hold`: False

# In[2]:


### START CODE HERE ###

# Create the dictionary, "book", with key/value pairs as mentioned above
# Please be sure to use the same upper/lower case spellings structure
# Add your code here
book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "on_shelf": False,
    "borrower": "Arthur Dent",
    "overdue": True,
    "on_hold": False
}

### END CODE HERE ###


# In[3]:


# Test your code!
test_your_code.exercise_1(book)


# **Important Note:** If you see <span style="color: green;">All tests passed!</span>, you can proceed to the next step. If there's an error message <span style="color: red;">in red</span>, follow the instructions to fix it, then re-run the exercise and test cells until you get the <span style="color: green;">All tests passed!</span> message. Repeat this process for all exercises in the assignment.

# <a name='2'></a>
# ## Exercise 2: Is It On the Shelf? 🤔
# 
# The moment of truth has arrived!  The eager reader is waiting to hear if "To Kill a Mockingbird" is available.  You need to check the `book` dictionary to see if it's available for checkout. 
# 
# **Your Task:**
# 
# Write an `if/else` statement that determines whether the book is available to borrow. 
# 
# - **If** the book is `on_shelf` (meaning `on_shelf` is `True`) **and** it's **not** `on_hold` (meaning `on_hold` is `False`), print: `"Book is available to be borrowed"`. 
# - **Else**, print: `"Book is not available to be borrowed"`.
# - Use the same `book` variable you defined in Exercise 1.
# 
# Notice that these two messages are static (you don't need to change them according to the value of a certain variable). **Because of this use regular strings and NOT f-strings.** It is a good practice to only use f-strings when necessary.

# In[20]:


### START CODE HERE ###

# Create an if/else statement
# Check if "book['on_shelf']" equals "True" and "book['on_hold']" equals "False" (do this in the same line)
# Add your if statement here
if book["on_shelf"] == True and book["on_hold"] == False:
    # Print "Book is available to be borrowed"
    print("Book is available to be borrowed")
    # Add your print here
    
# Add your else statement here
else:
    # Print "Book is not available to be borrowed"
    print("Book is not available to be borrowed")
    # Add your print here

### END CODE HERE ###


# #### Expected Output:
# 
# ```
# Book is not available to be borrowed
# ```

# In[21]:


# Test your code!
test_your_code.exercise_2()


# <a name='3'></a>
# ## Exercise 3: On Hold or Overdue? ⏳
# 
# Sadly, it turns out that "To Kill a Mockingbird" is currently checked out. 😩  However, the interested reader would like to be next in line!  You need to put the book on hold for them, but first, you want to check if it's overdue.
# 
# **Your Task:**
# 
# Write an `if/else` statement that does the following:
# 
# - **If** the book is `overdue` (meaning `overdue` is `True`), print: `"Book is overdue - Contact <Borrower's name> to return it"` (make sure to replace `<Borrower's name>` with the actual borrower's name from the dictionary `book`). **You should use an f-string to insert the borrower's name**. 
# - **Else**:
#     - Set the `on_hold` status of the book to `True` because you're now placing it on hold for the next reader.
#     - Print: `"Book has been put on hold"`.
# - Use the same `book` variable you defined in Exercise 1.    
# 
# Notice that one of these two messages is static, while the other needs to change according to the name of the borrower. **Because of this use a regular string for one and an f-string for the other**. Remember, it is a good practice to only use f-strings when necessary.

# In[6]:


### START CODE HERE ###

# Create an if/else statement
# Check if "book['overdue']" equals "True"
# Add your if statement here
if book["overdue"]  == True: 
    print(f"Book is overdue - Contact {book['borrower']} to return it")
    # Print "Book is overdue - Contact <Borrower's name> to return it"
    # Hint: Use print with f-string to get "book['borrower']"'s name
    # Add your print here
else:    
# Add your else statement here
    book["on_hold"]=True
    print("Book has been put on hold")
    # Set "book['on_hold']" to "True"
    # Add your print here
    
    # Print "Book has been put on hold"
    # Add your print here

### END CODE HERE ###


# #### Expected Output:
# 
# ```
# Book is overdue - Contact Arthur Dent to return it
# ```

# In[7]:


# Test your code!
test_your_code.exercise_3()


# <a name='4'></a>
# ## Exercise 4: Tracking Down the Borrower 🔎
# 
# "To Kill a Mockingbird" is indeed overdue! It seems Arthur Dent has been enjoying it a little too long. You need to send him a friendly reminder email. However, you only have his name – you need to find his email address from the library's records.
# 
# You have a list called `borrowers_list` (provided below) that contains dictionaries. Each dictionary in the list represents a borrower and has their `name`, `email`, and `phone`. Your task is to find Arthur Dent's email address from this list. Run the cell below to load the list.

# In[8]:


# List of dictionaries with borrower contact information
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


# **Your Task:** Get `Arthur Dent`'s email from your records of `borrowers_list`
# 
# * Use a **for** loop to iterate through `borrowers_list`.
# * Check **if** the name in `book['borrower']` matches with a "name" present in the `borrowers_list`
#     - If the name matches, store the corresponding "email" in a variable `borrower_email`
# * Use the same `book` variable you defined in Exercise 1.    

# In[9]:


### START CODE HERE ###

# Iterate through the borrowers_list
# Look for 'borrower' in `borrowers_list`
# Add your 'for' loop here
for borrower in borrowers_list:
    if book['borrower'] == borrower['name']:
    # Check if the name "book['borrower']" equals "borrower['name']"
    # Add your if statement here
        
        # Set "borrower_email" equals "borrower['email']"
        borrower_email = borrower['email']

### END CODE HERE ###

# Print the information
print(f"{book['borrower']}'s email is: {borrower_email}")


# #### Expected Output:
# ```
# Arthur Dent's email is: arthur.dent@dlailibrary.com
# ```

# In[10]:


# Test your code!
test_your_code.exercise_4(borrower_email)


# <a name='5'></a>
# ## Exercise 5: The LLM to the Rescue! 🤖
# 
# You've got Arthur's email address – great! Now, it's time to write him that overdue notice. To make your life easier, you decide to use an LLM (Large Language Model) to generate the email for you. LLMs are excellent at understanding instructions and crafting text. 
# 
# First, let's collect all of the information you want your `prompt` to include for the LLM to generate the email. Run the next cell to do that.

# In[11]:


# Name of the borrower
person_name = book['borrower']

# Name of the book
book_name = book['title']

# Name of book's author
book_author = book['author']

# Due Date
due_date = "16 November 2024"


# **Your Task:** 
# 
# Write a `prompt` that asks the LLM to generate an email to `person_name`, requesting them to return the book `book_name` by `book_author` before the `due_date`.
# 
#     You have the flexibility to structure your prompt and wording as you see fit. The key is to include all four pieces of information (`person_name`, `book_name`, `book_author`, and `due_date`) naturally within the `prompt`'s instructions. 
# 
#     For example, your prompt could look something like this: 
#     "Please write a polite email to [person_name], reminding them to return the book [book_name] by [book_author].  The book was due on [due_date]."

# In[15]:


### START CODE HERE ###

prompt = f"""
# Add your code here
Please write a polite email to {person_name}, reminding them to return the book {book_name} by {book_author}.  The book was due on {due_date}.
"""


### END CODE HERE ###

print(prompt)


# #### Expected Output
# ```
# Your prompt containing the following details of:
# - Arthur Dent
# - To Kill a Mockingbird
# - Harper Lee
# - 16 November 2024
# 
# ```
# 
# **Note:** You will fail the below test if your prompt excludes any one of the above mentioned details.

# In[16]:


# Test your code!
test_your_code.exercise_5(prompt)


# ### Submission Note:
# If you have passed all the tests up to this point, you can submit your assignment for grading.
# 
# **But before you submit your assignment, re-run the assignment just in case there are any unexpected errors present in the notebook once it goes for grading.** To do so, follow these steps:
# 
# 1. Restart the `Kernel` and select the `Restart & Clear Output` option. You can do this by clicking on the `Kernel` menu at the top of the notebook.
# ![Kernel Restart Image](kernel_restart.png)
# 2. Once the kernel restarts and all outputs are clear, run the cells from top to bottom again up to this point.
# 
# If you have followed these steps and still pass all of the tests, you can submit your assignment for grading. If you encounter any errors, please fix them before submitting.
# 
# To submit your assignment for grading, save your work by clicking the 💾 icon at the top left, then click the <span style="color: blue; font-weight: bold;">Submit assignment</span> button at the top right. Good luck!
# 
# Everything below this is OPTIONAL and will not affect your grading in anyway.

# Time to use the LLM! Let's import the `get_llm_response` function from the helper functions file.

# In[17]:


from helper_functions import get_llm_response


# Pass your `prompt` to the `get_llm_response` function, and print the response.

# In[18]:


print(get_llm_response(prompt))


# **Congratulations on finishing this module's assignment!** 🎉 You've successfully used your Python skills to help the librarian manage book records, find borrower information, and even draft an email using an LLM. Great work! 
